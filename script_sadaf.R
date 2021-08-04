##Write a script that prints your name, your email, your slack username (with @) and your biostack, twitter_handle, hamming_distance in that order.##



name <- "Sadaf Raza"
email <- "sadafraza48@gmail.com"
biostack <- "Genomics"
slack_username <- "@sadaf"
twitter_handle <- "@svdvf"




data <- data.frame(Information=c(name, email, slack_username, biostack, twitter_handle))

cat(paste(data, collapse = ','))
