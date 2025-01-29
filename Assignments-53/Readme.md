# Machine Learning Projects: 5 Animals & 17 Flowers Classification

## Project Overview
This documentation outlines the steps and procedures for training Convolutional Neural Networks (CNNs) to classify images of animals and flowers. Two separate datasets, '5 Animals' and '17 Flowers', are used for respective models. Each project includes data preprocessing, model training, performance evaluation, and integration with a Telegram bot for real-time classification.

---

## 5 Animals Classification

### Data Preprocessing
- The data is augmented using `ImageDataGenerator` with rescaling, rotation, zoom, and horizontal flip to enhance the dataset for better model training.

### Model Architecture
- A CNN with layers designed to extract features and classify among five different animal categories: cat, dog, elephant, giraffe, and panda.

### Training
- The model is trained using the augmented data, monitoring loss and accuracy on both training and validation sets.

### Performance Evaluation
- After training, the model's performance is evaluated using a confusion matrix to understand its classification accuracy across different animal types.

### Inference
- An example code snippet shows how to read an image, preprocess it, and use the model to predict the animal class, displaying the corresponding emoji.

## Project 1 Requirements:
- Image display area for loss and accuracy plots
- Table for recording model metrics (Train, Validation, and Test Loss/Accuracy)

## Tables for Model Metrics

**5 Animals Model Metrics:**

| Metric       | Train | Validation |
|--------------|-------|------------|
| **Loss**     | 0.26  |   0.91     | 
| **Accuracy** |  1.3  |   0.70     |

![Image](Results\1.png)
![Image](Results\2.png)
![Image](Results\3.png)
---

## 17 Flowers Classification

### Data Preprocessing
- Initial training without data augmentation to establish a baseline.
- Introduction of data augmentation techniques for improved model generalization.

### Model Architecture
- Similar CNN architecture adapted to classify 17 different types of flowers.

### Training and Evaluation
- The model is trained first without and then with augmentation. Comparisons are made to see the effect of augmentation on model performance.
- A confusion matrix is plotted to visualize the model's performance on the validation set.

### Bot Integration
- The trained model is connected to a Telegram bot, allowing real-time image classification of flowers sent by users, the `telegram bot id` is: `@amirreza_pybot`.

### Advanced Usage
- Example code is provided to show model inference on new flower images, detailing the preprocessing steps and prediction method.

## Project 2 Requirements:
- Image display area for loss and accuracy plots
- Table for recording model metrics (Train, Validation, and Test Loss/Accuracy)


## Tables for Model Metrics
**17 Flowers Model Metrics:**

| Metric       | Train | Validation | Test  |
|--------------|-------|------------|-------|
| **Loss**     | 0.13  |  320.7     |  1.58 |
| **Accuracy** | 0.96  |   0.68     |  0.69 |

![Image](Results\4.png)
![Image](Results\5.png)
![Image](Results\6.png)
![Image](Results\7.png)
![Image](Results\8.png)
![Image](Results\9.png)