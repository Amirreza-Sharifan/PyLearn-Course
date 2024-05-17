import os
import cv2
import matplotlib.pyplot as plt

input_path = 'F:/Python/Projects/PyLearn-Course/Assignments-37/Data_Set_Numbers/image.png'
output_base_path = 'F:/Python/Projects/PyLearn-Course/Assignments-37/Data_Set_Numbers/crops'

img = cv2.imread(input_path, 0)
plt.imshow(img, cmap='gray')

rows, cols = img.shape
numbers = []
for i in range(10):
    target_nums = img[int(rows * (i/10)): int(rows * ((i+1)/10)), :]
    numbers.append(target_nums)

counter = 0
for i in range(len(numbers)): 
    newpath = os.path.join(output_base_path, f"{i}")
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    rows, cols = numbers[i].shape
    
    for j in range(5):
        for k in range(100):
            target_num = numbers[i][int(rows * (j/5)): int(rows * ((j+1)/5)), int(cols * (k/100)): int(cols * ((k+1)/100))]
            
            cv2.imwrite(os.path.join(newpath, f"{counter}.jpg"), target_num)
            counter += 1
    counter = 0
