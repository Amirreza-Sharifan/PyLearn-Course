# Titanic Survival Prediction

## Overview
This project aims to predict whether a passenger on the Titanic would survive based on various features using different machine learning models. The primary goal is to implement a Multi-Layer Perceptron (MLP) neural network for classification and evaluate its performance alongside other models.

## Dataset
The dataset used is the Titanic dataset, containing information about passengers such as:
- `Pclass`: Passenger class (1st, 2nd, 3rd)
- `Sex`: Gender of the passenger (encoded as 0 for female, 1 for male)
- `Age`: Age of the passenger
- `SibSp`: Number of siblings/spouses aboard
- `Parch`: Number of parents/children aboard
- `Fare`: Ticket fare

## Steps in the Project
1. **Data Preprocessing**:
    - Missing values in the `Age` column were filled with the mean value.
    - Categorical values (e.g., `Sex`) were encoded into numerical values.

2. **Feature Selection**:
    - Features used for prediction: `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`.
    - Target variable: `Survived`.

3. **Model Implementation**:
    - Implemented a Multi-Layer Perceptron (MLP) using TensorFlow/Keras.
    - Other models such as KNN and Perceptron were also tested for performance comparison.

4. **Evaluation**:
    - Accuracy, precision, and recall metrics were computed.
    - Comparison of model performance on the test dataset.

5. **Prediction**:
    - The trained model was used to predict survival for hypothetical passengers, Jack and Rose.

## Results Table
| Model       | Accuracy |
|-------------|----------|
| MLP         |   96%    |
| KNN         |   66%    |
| Perceptron  |   64%    |