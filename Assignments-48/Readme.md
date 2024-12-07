# Multi-Layer Perceptron Neural Network Implementation

## Project Overview
This project implements a simple multi-layer perceptron (MLP) neural network for digit classification using the Scikit-Learn digits dataset. The implementation includes:
- A custom-built MLP class using object-oriented programming.
- A custom `OneHotEncoder` and `OneHotDecoder` to handle label encoding and decoding, compared with Scikit-Learn's `OneHotEncoder`.
- Training, testing, and evaluation of the MLP with a focus on tracking loss and accuracy.
- Visualization of the loss and accuracy over epochs.
- A functionality to predict handwritten digits provided as input images.

---

## Features and Implementation
### Data Preparation
- Used Scikit-Learn's digits dataset.
- Implemented custom one-hot encoding for labels.
- Split data into training and testing sets.

### MLP Architecture
- Three-layer neural network:
  - **Input Layer**: 64 neurons (8x8 flattened image).
  - **Hidden Layers**: Configured with 128 and 32 neurons.
  - **Output Layer**: 10 neurons (digit classes from 0 to 9).
- **Activation Functions**: Sigmoid for hidden layers, Softmax for the output layer.

### Training and Testing
- Backpropagation for weight and bias updates.
- Tracked and logged training/test loss and accuracy over 50 epochs.

### Visualization
- Plotted loss and accuracy for training and testing data over the epochs.

### Handwritten Digit Prediction
- Processed custom handwritten digit images (grayscale, resized to 8x8).
- Made predictions using the trained MLP model.

---

## Results
### Training and Testing Performance
- **Final Training Accuracy**: 81.7%
- **Final Test Accuracy**: 80.8%
- **Final Training Loss**: 0.1620
- **Final Test Loss**: 0.1668

### Visualization
- Loss and accuracy graphs show consistent improvement over epochs:

![Loss and Accuracy Plots](result\output.png)

### Handwritten Image Prediction
- Successfully predicted custom handwritten digits.
- Example result: Predicted digit **1** for a sample input image.

---

## Screenshots
### Epoch-wise Training and Testing Results
![Training and Testing Logs](ax-2.jpg)

### Handwritten Image Prediction
![Handwritten Image](result\output-2.png)
