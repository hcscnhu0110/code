data <- read.csv(NewTaipeiCity.csv, sep = ",")
NewTaipeiCity.csv <- file.path("C:/Users/user/Desktop/程式/R語言/NewTaipeiCity.csv") 

library(ggplot2)
draw_ratio_of_loan_burden <- function() {
    year <- data[, 1]
    taiwan <- data[, 2]
    ntc <- data[, 3]
    plot(x = year, y = taiwan, type = "l", main = "貸款負擔率"
        , xlab = "年(91~109)" , ylab = "貸款負擔率(%)", ylim = c(20, 60))
    lines(x = year, y = ntc, type = "l")
}



draw_ratio_of_house_price_to_income <- function(){ 
    year <- c(91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109) 
    taiwan <- data[,4] 
    ntc <- data[,5]
    plot(x = year, y = taiwan , type = "l", main = "貸款負擔率"  
        , xlab = "年(91~109)" , ylab = "貸款負擔率(%)", ylim = c(20,60)) 
    lines(x = year, y = ntc , type = 'l') 
}
draw_ratio_of_loan_burden()


norm <- function(){ 

    par(mfrow = c(3,2))

    #全國貸款負擔率
    qqnorm(data$全國貸款負擔率,main = "全國貸款負擔率") # 
    qqline(data$全國貸款負擔率,col = "Red")
    print(shapiro.test(data$全國貸款負擔率))

    #新北市貸款負擔率
    qqnorm(data$新北市貸款負擔率,main = "新北市貸款負擔率")
    qqline(data$新北市貸款負擔率,col = "Orange")
    print(shapiro.test(data$新北市貸款負擔率))

    #全國房價所得比
    qqnorm(data$全國房價所得比,main = "全國房價所得比")
    qqline(data$全國房價所得比,col = "Green")
    print(shapiro.test(data$全國房價所得比))

    #新北市房價所得比
    qqnorm(data$新北市房價所得比,main = "新北市房價所得比")
    qqline(data$新北市房價所得比,col = "Blue")
    print(shapiro.test(data$新北市房價所得比))

    #全國總生育率
    qqnorm(data$全國總生育率,main = "全國總生育率")
    qqline(data$全國總生育率,col = "Pink")
    print(shapiro.test(data$全國總生育率))

    #新北市總生育率
    qqnorm(data$新北市總生育率,main = "新北市總生育率")
    qqline(data$新北市總生育率,col = "Purple")
    print(shapiro.test(data$新北市總生育率))
}


#
#draw_ratio_of_house_price_to_income()
#norm()

#ntc_ratio_of_loan_burden <- data$新北市貸款負擔率
#ntc_born <- data$新北市總生育率 
#LM <- lm(ntc_ratio_of_loan_burden ~ ntc_born,data = data)
#dev.off() 
#ggplot(data,aes(x = data$新北市貸款負擔率, y = data$新北市總生育率)) + 
        #geom_point(shape = 10,size = 5) + geom_smooth(method = lm)