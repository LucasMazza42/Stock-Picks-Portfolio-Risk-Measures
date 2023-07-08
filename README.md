# QuantResearch

This project is mostly aimed at my learning to use the QuantStat package in Python but also introduced me to some learning on quantitative analysis of stock data.
  - Resources: https://pypi.org/project/QuantStats/ and https://medium.com/the-modern-scientist/introduction-to-quant-investing-with-python-c215d1014a25

- Stocks studied in this section: Apple, Tesla, Disney, AMD

# Section 1: Cumulative returns:
<img width="1787" alt="Screenshot 2023-06-27 at 11 23 49 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/05e2031d-e836-4b49-9494-a3f9265f00fd">
- Fairly steady growth, big jumps starting in 2019
<img width="1786" alt="Screenshot 2023-06-27 at 11 24 11 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/594f5271-6cef-40a4-a6cb-853fb91d7828">
- The most interesting of all the stocks here is Tesla, 🚀 
<img width="1776" alt="Screenshot 2023-06-27 at 11 24 30 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/e029add1-dc3a-4451-bf8a-ce58f462a79b">
- Most stagnant of the listed is Disney
<img width="1792" alt="Screenshot 2023-06-27 at 11 24 45 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/2d554b71-d830-4682-bd64-c4ed6dd83a7b">
- AMD is another pretty shakey stock like TSLA

# SECTION 2: Daily returns

<img width="1002" alt="Screenshot 2023-06-28 at 6 57 37 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/a62b0d51-2f8b-4d7f-b022-4bf7afa7542f">

<img width="988" alt="Screenshot 2023-06-28 at 7 00 14 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/6f82a1f6-c1ab-42de-81f5-c0cc6ab269a8">

<img width="993" alt="Screenshot 2023-06-28 at 7 00 59 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/922cc46f-49b6-4c18-ad2d-1bfd0b937552">

# SECTION 3: Kurtosis values

Kurtosis values explained:
  - Kurtosis quantifies the heaviness of the tails of a distribution compared to a normal distribution. It measures the extent to which the distribution has outliers or extreme values.
  - Datasets with values less than 3 generally indicate fewer outliers, so lower peaks flatter tails
  - Datasets with values more than 3 generally indicate more outlier values, so higher peaks, and heavy-weighted tails
  - In the context of our data:
      - Values greater than three indicated a more volatile stock.
      - Values less than three indicated a less volatile stock.
   
Our data: 
Apple's kurtosis:  5.24
Tesla's kurtosis:  5.05
Disney's kurtosis:  10.98
AMD's kurtosis:  17.09

- All of our stocks would classify as stocks with more extreme price swings 
- The likelihood of having large swings is more likely for these companies 

# Skewness: 
  - Skewness in the context of our data: 
      - right skew, indicates a higher chance of larger returns -- values that are positive
      - left skew, indicates a lower change of larger returns or even negative -- values that are negative

Our data: 
Apple's skewness:  0.03
Tesla's skewness:  0.39
Walt Disney's skewness:  0.164
Advances Micro Devices' skewness:  0.001

- All of our stocks indicate right skew, meaning there is higher probability for larger returns 

# Standard deviation: 
  - stocks with higher standard deviation mean the price from day to day deviates from the normal distribution
  - Higher standard deviation = higher risk 

Our data: 

Apple's Standard Deviation from 2010 to 2023:  0.018

Tesla's Standard Deviation from 2010 to 2023:  0.036

Disney's Standard Deviation from 2010 to 2023:  0.016

AMD's Standard Deviation from 2010 to 2023:  0.036

- From this, we can say Disney has the smallest price fluctuations 
- We can also say Apple is a less risky investment than Tesla just based on this data

# Beta and alpha values: 
  - In beta and alpha values we are comparing the volatility of a stock in comparison to the general market 
  - In my case, I compared all of the stocks to the S&P500 
  - The beta value of less than 1 indicates that the stock is less volatile than the market 
  - The beta value of greater than 1 indicates that the stock is more volatile than the market 
  - A positive alpha value means that the stock has outperformed its beta value 
  - A negative alpha value means that the stock has underperformed its beta value 

Our data: 


