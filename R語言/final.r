getData <- function(){
    csvFile <- file.path("C:/Users/user/Desktop/united-states-rates-of-covid-19-deaths-by-vaccination-status-by-vaccine.csv")
    data <- read.csv(csvFile , encoding = 'utf-8')
}
data <- getData()
library(Hsimc)
cor.target <- cor(data)
cor.target