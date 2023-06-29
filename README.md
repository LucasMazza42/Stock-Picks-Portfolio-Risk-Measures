# QuantResearch

This project is mostly aimed at my learning to use the QuantStat package in Python but also introduced me to some learning on quantitative analysis of stock data.
  - Resources: https://pypi.org/project/QuantStats/ and https://medium.com/the-modern-scientist/introduction-to-quant-investing-with-python-c215d1014a25

- Stocks studied in this section: Apple, Tesla, Disney, AMD

- Section 1: Cumulative returns:
<img width="1787" alt="Screenshot 2023-06-27 at 11 23 49 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/05e2031d-e836-4b49-9494-a3f9265f00fd">
<img width="1786" alt="Screenshot 2023-06-27 at 11 24 11 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/594f5271-6cef-40a4-a6cb-853fb91d7828">
<img width="1776" alt="Screenshot 2023-06-27 at 11 24 30 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/e029add1-dc3a-4451-bf8a-ce58f462a79b">
<img width="1792" alt="Screenshot 2023-06-27 at 11 24 45 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/2d554b71-d830-4682-bd64-c4ed6dd83a7b">

- SECTION 2: Daily returns

<img width="1002" alt="Screenshot 2023-06-28 at 6 57 37 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/a62b0d51-2f8b-4d7f-b022-4bf7afa7542f">

<img width="988" alt="Screenshot 2023-06-28 at 7 00 14 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/6f82a1f6-c1ab-42de-81f5-c0cc6ab269a8">

<img width="993" alt="Screenshot 2023-06-28 at 7 00 59 PM" src="https://github.com/LucasMazza42/QuantResearch/assets/47802441/922cc46f-49b6-4c18-ad2d-1bfd0b937552">

- SECTION 3: Kurtosis values

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
