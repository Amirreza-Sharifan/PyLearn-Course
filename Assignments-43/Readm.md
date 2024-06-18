# Assignments-43
## 1-Finding Nemo & Dory
In this project we will predict the position of two fishes that they name are ``Nemo`` & ``Dory``.
the results of this project have prepared blow:
### Steps and Results
1. Original Image
- The original image of a clownfish in its natural habitat is displayed below.

2. Image Thresholding
- The image is converted to a binary image using thresholding. This step highlights the fish by distinguishing it from the background based on pixel intensity.


3. Masked Image
- The binary mask is applied to the original image to isolate the clownfish. This step helps in visualizing only the relevant parts of the image, making the fish stand out.


4. Alternative Image
- Another image of a clownfish is processed to demonstrate consistency in results across different images.


5. Alternative Image Thresholding
- Thresholding is applied to the alternative image to create a binary mask.


6. Alternative Masked Image
- The binary mask is applied to the alternative original image, isolating the clownfish.

-
| Nemo 1(train) | Nemo 2(test) | Dory 1(train) | Dory 2(test) |
|---------|---------|---------|---------|
| ![Image 1](nemo0.jpg) | ![Image 2](nemo3.jpg) | <img src="Dory-Flickr-Image-scaled.jpg" width="300" /> | ![Image 4](images.jpg) ||---------|---------|---------|---------|
| ![Image 1](1.png) | ![Image 2](2.png) | <img src="3.png" width="500" /> | ![Image 4](4.PNG) ||---------|---------|---------|---------|
| ![Image 1](5.png) | ![Image 2](6.png) | <img src="7.png" width="500" /> | ![Image 4](8.PNG) |

## 2-Iris data set
IN this project we calculate and predict of Iris data set from ``skite-learn`` and the algorithm of machine learning that we use is KNN moreover, the value of K are 3,5 and 7. At the below we can see the confusion matrix and the score of each algorithm.

| K | Accuracy of ``Amirreza`` (%) | Accuracy of ``Skite-learn`` (%) | canfusion matrix |
|---------|---------|---------|---------|
|3 |[97]|[97]|<img src="9.png" width="300" />|
|5 |[100]|[100]|<img src="10.png" width="300" />|
|7 |[100]|[100]|<img src="11.png" width="300" />|
## 3-Breast Cancer data set
IN this project we calculate and predict of Brest Cancer data set from ``skite-learn`` and the algorithm of machine learning that we use is KNN moreover, the value of K are 3,5 and 7. At the below we can see the confusion matrix and the score of each algorithm.

| K | Accuracy of ``Amirreza`` (%) | Accuracy of ``Skite-learn`` (%) | canfusion matrix |
|---------|---------|---------|---------|
|3 |[90]|[90]|<img src="12.png" width="300" />|
|5 |[90]|[90]|<img src="13.png" width="300" />|
|7 |[90]|[90]|<img src="14.png" width="300" />|