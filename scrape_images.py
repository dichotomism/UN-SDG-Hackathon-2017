from google import google, images
import pandas as pd

with open("priority_countries.txt", "r") as f:
	countries = f.read().split("\n")

with open("search_topics.txt", "r") as f:
	topics = f.read().split("\n")

# setting default settings for image search
def reset_options():
	options = images.ImageOptions()
	options.color_type = 'color'
	options.license = 'f'
	options.larger_than = images.LargerThan.MP_12
	return options

with open("search_results.txt", "r") as past_results:
	past_results = past_results.readlines()
	past_queries = {t.split(",", 1)[0][1:-1] for t in past_results}

result_file = open("search_results.txt", "a")
results = []
for i, country in enumerate(countries):
	for j, topic in enumerate(topics):
		options = reset_options()

		if 'face' in topic:
			options.image_type = images.ImageType.FACE

		image_query = '{} {}'.format(country, topic)
		if image_query in past_queries:
			continue

		print("\rSearching for: %s (%d out of %d)".ljust(100) \
				%(image_query, i * len(topics) + j + 1, len(topics) * len(countries)), 
				end = "")

		search_results = google.search_images(image_query)
		result_file.writelines(['"{}", {}, "{}"\n'.format(image_query, s.index, s.link) for s in search_results])

result_file.close()