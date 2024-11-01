# Summary of the ML project

In this project, I intend to use different machine learning models to predict the electricity price, which can help the market participants reduce their cost for operation. This project used data from the California Independent System Operator (CAISO). It oversees the operation of California's bulk electric power system, transmission lines, and electricity market generated and transmitted.

Electricity markets are complex decision-making processes that seek to coordinate generation, transmission, and consumption resources at multiple timescales. The following picture shows a simplified version of the actitivies in eletricity markets.

![Markets flow of power and money](https://learn.pjm.com/-/media/pjm-learn/images/electricity-basics/markets-flow-of-power-and-money.ashx?la=en)

The total percentage of electricity from renewable sources in California is 31%. For example, the generation of wind energy in US increased from almost zero to 30 million megawatthours per month from 2001 to 2019. 

![CA's renewable energy usage](https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fft-ig-shorthand-editorial-prod-uk%2Fspecial-reports%2Frenewable-energy%2Fmedia%2Fenergy_nudhrtr.png?source=commercial-content-lambda)

Among all the renewable energy sources, wind energy is account for 29% of the renewable energy. Because the wind energy generation have strong fluctuation during the 24 hours of the day, the electricity price has a strong fluctuation as well. 

![CA's renewable energy usage category](https://www.calwea.org/sites/default/files/image001_0.jpg)

In the electricity market, Real Time price is the electricity price with 5-min intervals. The day ahead market is the price 24 hours ahead values with 1 hour intervals. Therefore, predicting electricity price can potentially save significant amount of money for manufacturing companies.

## Setup
To set up, install the required packages:

pip install -r requirements.txt
