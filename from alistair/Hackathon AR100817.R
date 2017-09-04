# code fragment
# load csv from url, url is known csv

# ### 
# ### 
# ### step 1 -- install RCurl package and library
# ###
# ###

# note: see also: https://stackoverflow.com/questions/23028760/download-a-file-from-https-using-download-file

install.packages("bitops")
library(bitops)

install.packages("RCurl")
library(RCurl)

# ###
# ###
# step 2 -- confirm install of RCurl package and library
# ###
# ###

# initialise console with Cntl-L
# note: see also https://www.r-bloggers.com/list-of-user-installed-r-packages-and-their-versions/
# note: see also https://stackoverflow.com/questions/2851015/convert-data-frame-columns-from-factors-to-characters
# note: see also https://www.r-bloggers.com/r-sorting-a-data-frame-by-the-contents-of-a-column/

cat("\014")
catalog_installed <- as.data.frame(installed.packages()[,c(1,3:4)], stringsAsFactors=FALSE)
rownames(catalog_installed) <- NULL
catalog_installed <- catalog_installed[is.na(catalog_installed$Priority),1:2,drop=FALSE]
colnames(catalog_installed) <- c('name', 'version')
catalog_installed <- catalog_installed[order(catalog_installed$name),]
View (catalog_installed)

# yes ok -- 

# ###
# ###
# step 3 -- try initial install
# ###
# ###

# note: see also: https://stackoverflow.com/questions/23028760/download-a-file-from-https-using-download-file

options(RCurlOptions = list(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl")))   
URL <- "https://unstats.un.org/sdgs/indicators/database/?area=BMU#"
region_4 <- getURL(URL)
head(region_4)

# result

# Error in function (type, msg, asError = TRUE)  : 
# Received HTTP code 407 from proxy after CONNECT

# copy from downloaded csv instead

region_4 <- read.csv (file = "~/Network-Shares/J-Drive-WLG-Shared/S_SM/Admin Data Investigations/Hackathon/SDG Indicators — SDG Indicators -- Bermuda.csv", 
                      header = TRUE, 
                      sep = ",")

View (region_4)

# works

