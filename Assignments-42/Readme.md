# KNN Algorithm Implementation and Evaluation

This project demonstrates the implementation and evaluation of the K-Nearest Neighbors (KNN) algorithm on a combined dataset of male and female measurements. The process includes preprocessing the dataset, splitting it into training and testing sets, evaluating the KNN algorithm with different values of `k`, and calculating the confusion matrix for the test dataset.

## Steps

1. **Preprocess Dataset**
   - Convert the unit of weight from pounds to kilograms.
   - Convert the unit of height from inches to centimeters.
   - Convert the datatype of gender from categorical to numerical.

2. **Split Dataset**
   - Split the dataset into training and testing sets with 80% for training and 20% for testing.

3. **Evaluate KNN Algorithm**
   - Evaluate the KNN algorithm on the test dataset with different values of `k = 3, 5, 7`.
   - The table below shows the accuracy for each value of `k`.

   | k  | Accuracy of ``object oriented KNN algorithm`` (%) | 
   |----|--------------|
   | 3  |  [83] |
   | 5  |  [84] |
   | 7  |  [83] |

4. **Calculate Confusion Matrix**
   - Calculate the confusion matrix for the test dataset.

5. **KNN Implementation using Scikit-Learn**
   - Perform the above steps using the Scikit-Learn library to ensure correctness and compare results.
   - The table below shows the accuracy for each value of `k`.

   | k  | Accuracy of ``scikit-learn KNN algorithm`` (%) | 
   |----|--------------|
   | 3  |  [83] |
   | 5  |  [84] |
   | 7  |  [83] |
## Result
As expected, the accuracy of the two algorithms were similar.