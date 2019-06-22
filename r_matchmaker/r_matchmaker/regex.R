library(readr) ; library(dplyr); library(tidyr); library(dbplyr)
library(stringr); library(odbc); library(DBI)
bir_origin <- read_csv("C:/webDev/pycharm/matchmaker/data/bir_origin.txt")

myco_table <- data.frame(bir_origin)

myco_table$term <- str_extract(myco_table$X1, "(^[A-Z]{3,} [A-Z]{3,}\\(?S?\\)?|^[A-Z]{3,})")
myco_table$content <- str_extract(myco_table$X1, "(?!^[A-Z]{3,} [A-Z]{3,}\\(?S?\\)?|^[A-Z]{3,})(  .*$)")

rearranged <- tidyr::spread(myco_table, term, )

dplyr::tbl_df(myco_table)

#"(^[A-Z]{3,} [A-Z]{3,}\\(?S?\\)?|^[A-Z]{3,})"
# text <- OFdata$duration
# minutes <- as.numeric(str_extract(text, '\\d\\.\\d\\d|\\d\\.\\d|\\d'))
# seconds.colon <- as.numeric(substr(str_extract(text, ':\\d\\d' ),2,3))/60
# seconds.s <- as.numeric(substr(str_extract(text, '\\d\\ds' ),1,2))/60

View(myco_table)