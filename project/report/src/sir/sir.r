library (readr)
library("COVID19")
require(deSolve)
usa_data <- covid19('USA')
par(mfrow=c(1,4))   
plot(x = usa_data$date, y = 326687501 - usa_data$deaths - usa_data$confirmed - usa_data$recovered, type = 'l', col = 4,xlab = "Time/month", ylab = 'Population', main = 'Susceptible')
plot(x = usa_data$date, y = usa_data$confirmed - usa_data$recovered - usa_data$deaths, type = 'l',col = 2, xlab = "Time/month", ylab = 'Population', main = 'Infected')
plot(x = usa_data$date, y = usa_data$recovered, type = 'l',col = 3, xlab = "Time/month", ylab = 'Population', main = 'Recovered')

plot(x = usa_data$date, y = 326687501 - usa_data$deaths - usa_data$confirmed - usa_data$recovered,
     type = 'l',col = 2, xlab = "Time/month", ylab = 'Population', main = 'COVID-19 case',
     ylim = c(0, 3.3*10E7)
     ,yaxs = "i"
     )
lines(x = usa_data$date, y = usa_data$confirmed - usa_data$recovered - usa_data$deaths, col = 4)
lines(x = usa_data$date, y = usa_data$recovered, col = 3)
legend("left", legend=c("Susceptible", "Infected","Recovered"),
       col=c("red", "blue", "green"), lty=1)
