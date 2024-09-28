# Tehran House Price Prediction

This notebook explores the prediction of house prices in Tehran using two different regression methods: Linear Least Squares (LLS) and Linear Regression.

## Description

The dataset contains information about house prices in Tehran, focusing on the most expensive properties. The goal of the project is to predict house prices using different machine learning models and evaluate their performance based on the following metrics:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### Data
The top 5 most expensive houses were as follows:

| Address        | Price(Toman)              |
|----------------|--------------------|
| Zaferanieh| 924,000,000,000    |
| Abazar    | 910,000,000,000    |
| Lavasan    | 850,000,000,000    |
| Ekhtiarieh | 816,000,000,000    |
| Niavaran  | 805,000,000,000    |

### Evaluation Metrics
The following metrics were used to evaluate the models:
- **MAE**: Mean Absolute Error
- **MSE**: Mean Squared Error
- **RMSE**: Root Mean Squared Error

### Results

The performance comparison between the two models is as follows:

| Metric  | LLS (Linear Least Squares) | Linear Regression |
|---------|----------------------------|-------------------|
| MAE     | 2,752,430,294.96            | 2,764,735,571.81  |
| MSE     | 2.63327e+19                 | 2.42788e+19       |
| RMSE    | 5,131,541,689.27            | 4,927,355,297.61  |

### Conclusion
Both models perform similarly, with Linear Regression slightly outperforming LLS in terms of RMSE and MSE. However, the difference in performance is minimal, and either model could be a viable option depending on the use case.

# Tehran House Price Prediction
# Dollar to Rial Price Analysis

This notebook examines the changes in the Dollar to Rial exchange rate during the presidencies of Ahmadinejad, Rouhani, and Raisi. The analysis includes both the highest and lowest prices recorded during each presidency, as well as the Mean Absolute Error (MAE) of the dollar prices.

## Description

The dataset focuses on the exchange rates of the Dollar to Rial during different presidential terms in Iran. The aim is to evaluate the fluctuations in dollar prices and compare the MAE for each presidency.

### Data

| President     | Highest Dollar Price (Rial) | Lowest Dollar Price (Rial) | MAE        |
|---------------|-----------------------------|----------------------------|------------|
| Ahmadinejad   | 39,700                       | 13,350                      | 48.4998    |
| Rouhani       | 99,950                       | 100,370                     | 475.1518   |
| Raisi         | 555,600                      | 206,210                     | 1279.6019  |

### Evaluation Metric

- **MAE (Mean Absolute Error)**: This metric indicates the average absolute difference between the predicted values and the actual values during each presidency.

### Results

- During Ahmadinejad's presidency, the dollar prices fluctuated between 13,350 and 39,700 Rials, with an MAE of 48.50.
- During Rouhani's presidency, the dollar prices fluctuated between 100,370 and 99,950 Rials, with an MAE of 475.15.
- During Raisi's presidency, the dollar prices fluctuated significantly between 206,210 and 555,600 Rials, with the highest MAE of 1279.60.

### Conclusion

The exchange rate fluctuations have been most significant during Raisi's presidency, with a notable increase in the highest and lowest prices compared to the previous presidencies. The MAE has also been the highest, reflecting greater unpredictability in the exchange rate during this period.
