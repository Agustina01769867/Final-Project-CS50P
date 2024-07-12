# Stock Price Simulation and analysis
#### Video Demo:  https://youtu.be/pMzuz7v53tk
#### Description:


This Python script performs a comprehensive simulation and analysis of stock prices using historical data from Yahoo Finance. The primary goal is to predict future stock prices through a simple linear regression model and subsequently run a Monte Carlo simulation based on the Black-Scholes model.

To begin, ensure you have the required Python packages installed: Matplotlib, Numpy, and Pandas. Matplotlib is used for creating visualizations, Numpy for numerical computations, and Pandas for data manipulation and analysis. You can install these packages using pip.

The script is designed to be executed from the command line, with the company symbol provided as an argument. The format for running the script is python script_name.py 'COMPANY_SYMBOL', where COMPANY_SYMBOL is the ticker symbol of the company you want to analyze. For instance, to analyze Apple Inc., you would run python script_name.py AAPL.

The script begins by importing the necessary libraries. It includes libraries for plotting (matplotlib), numerical computations (numpy), random number generation (random), mathematical functions (math), data manipulation (pandas), and handling system-specific parameters and functions (sys). 

The script defines several functions. The calcular_beta1 function calculates the slope (beta1) of the linear regression line using the least squares method. The calcular_beta0 function calculates the intercept (beta0) of the linear regression line. The get_csv function fetches historical stock data for the specified company from Yahoo Finance by downloading a CSV file.

The main function orchestrates the workflow of the script. It starts by checking if a company symbol has been provided as a command-line argument. If not, it exits with an appropriate error message. It then fetches the historical stock data for the provided company symbol using the get_csv function. The closing prices are extracted from the data, and the days are enumerated.

Next, the script calculates the daily returns of the stock. It then determines the beta coefficients for linear regression by calling the calcular_beta1 and calcular_beta0 functions. These coefficients are used to identify a confidence interval for the data.

The script proceeds to run a Monte Carlo simulation to project future stock prices. It generates random performance paths for the stock using the calculated mean and standard deviation of the returns. The simulation runs 100 different paths over a period of 10 days, starting from the last observed closing price.

Finally, the script plots the results of the simulation. It generates a scatter plot of the daily returns and overlays the linear regression line. The plot provides a visual representation of the confidence interval and the projected future stock prices.

To summarize, this script provides a robust method for analyzing and predicting stock prices using historical data. It combines linear regression and Monte Carlo simulation techniques to generate future price projections, which are then visualized through plots. The script requires an active internet connection to fetch the stock data, and it's important to note that historical data formats and availability may change over time.

Ensure you have an active internet connection to fetch the stock data. Historical data may change in format or availability, which could affect the script's functionality. This approach leverages statistical and probabilistic methods to offer insights into stock price movements, aiding in investment decision-making and risk assessment.
