import pandas as pd
import quantstats as qs
import plotly.express as px
import yfinance as yf
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Download stock data
aapl = yf.download('AAPL', start='2010-07-01', end='2023-02-10')
tsla = yf.download('TSLA', start='2010-07-01', end='2023-02-10')
dis = yf.download('DIS', start='2010-07-01', end='2023-02-10')
amd = yf.download('AMD', start='2010-07-01', end='2023-02-10')
sp500 = yf.download('^GSPC', start='2010-07-01', end='2023-02-10')

# Calculate cumulative returns
aapl_cumulative = (1 + aapl['Close'].pct_change()).cumprod() - 1
tsla_cumulative = (1 + tsla['Close'].pct_change()).cumprod() - 1
dis_cumulative = (1 + dis['Close'].pct_change()).cumprod() - 1
amd_cumulative = (1 + amd['Close'].pct_change()).cumprod() - 1

# Plot graphs
fig_aapl = px.line(aapl_cumulative, title='AAPL Cumulative Returns')
fig_aapl.update_yaxes(tickformat=".2%")  # Format y-axis as percentage

fig_tsla = px.line(tsla_cumulative, title='TSLA Cumulative Returns')
fig_tsla.update_yaxes(tickformat=".2%")  # Format y-axis as percentage

fig_dis = px.line(dis_cumulative, title='DIS Cumulative Returns')
fig_dis.update_yaxes(tickformat=".2%")  # Format y-axis as percentage

fig_amd = px.line(amd_cumulative, title='AMD Cumulative Returns')
fig_amd.update_yaxes(tickformat=".2%")  # Format y-axis as percentage


#fig_aapl.show()
#fig_tsla.show()
#fig_dis.show()
#fig_amd.show()


# Calculate daily returns
aapl_returns = aapl['Close'].pct_change().dropna()

plt.plot(aapl_returns)
plt.title('Apple Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
#plt.show()

# Calculate daily returns
tsla_returns = tsla['Close'].pct_change().dropna()

plt.plot(tsla_returns)
plt.title('Tesla Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
#plt.show()

# Calculate daily returns
dis_returns = dis['Close'].pct_change().dropna()

plt.plot(dis_returns)
plt.title('Disney Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
#plt.show()

# Calculate daily returns
amd_returns = amd['Close'].pct_change().dropna()

plt.plot(amd_returns)
plt.title('AMD Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
#plt.show()

# Plotting histograms
print('\nApple Daily Returns Histogram')
#qs.plots.histogram(aapl, resample = 'D')
 
print('\nTesla Inc. Daily Returns Histogram')
#qs.plots.histogram(tsla, resample = 'D')
 
print('\nThe Walt Disney Company Daily Returns Histogram')
#qs.plots.histogram(dis, resample = 'D')
 
print('\nAdvances Micro Devices, Inc. Daily Returns Histogram')
#qs.plots.histogram(amd, resample = 'D')


# Calculate kurtosis using scipy.stats
aapl_kurtosis = stats.kurtosis(aapl_returns)
print("Apple's kurtosis: ", round(aapl_kurtosis, 2))


tsla_kurtosis = stats.kurtosis(tsla_returns)
print("Tesla's kurtosis: ", round(tsla_kurtosis, 2))

dis_kurtosis = stats.kurtosis(dis_returns)
print("Disney's kurtosis: ", round(dis_kurtosis, 2))

amd_kurtosis = stats.kurtosis(amd_returns)
print("AMD's kurtosis: ", round(amd_kurtosis, 2))


# Measuring skewness with quantstats
print("Apple's skewness: ", qs.stats.skew(aapl).round(2)['Open'])
print("Tesla's skewness: ", qs.stats.skew(tsla).round(2)['Open'])
print("Walt Disney's skewness: ", qs.stats.skew(dis).round(3)['Open'])
print("Advances Micro Devices' skewness: ", qs.stats.skew(amd).round(3)['Open'])

# Calculating Standard Deviations
print("Apple's Standard Deviation from 2010 to 2023: ", aapl.std().round(3)['Open'])
print("\nTesla's Standard Deviation from 2010 to 2023: ", tsla.std().round(3)['Open'])
print("\nDisney's Standard Deviation from 2010 to 2023: ", dis.std().round(3)['Open'])
print("\nAMD's Standard Deviation from 2010 to 2023: ", amd.std().round(3)['Open'])

#Beta and alpha 

# Extract the adjusted close prices from AAPL
X = sp500['Close'].values.reshape(-1, 1)
y = aapl['Adj Close'].values.reshape(-1, 1)

# Perform linear regression
linreg = LinearRegression().fit(X, y)

# Retrieve beta and alpha coefficients
beta = linreg.coef_[0][0]
alpha = linreg.intercept_[0]

# Print the results
print('AAPL beta:', round(beta, 3))
print('AAPL alpha:', round(alpha, 3))


#Sharpe ratio
print("Sharpe Ratio for AAPL: ", qs.stats.sharpe(aapl).round(2)['Open'])
print("Sharpe Ratio for TSLA: ", qs.stats.sharpe(tsla).round(2)['Open'])
print("Sharpe Ratio for DIS: ", qs.stats.sharpe(dis).round(2)['Open'])
print("Sharpe Ratio for AMD: ", qs.stats.sharpe(amd).round(2)['Open'])