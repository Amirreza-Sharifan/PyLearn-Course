import os
import imageio
file_list = sorted(os.listdir("F:\Python\Projects\PyLearn-Course\Assignments-8\image"))
IMAGES = []
for file_name in file_list:
    file_path = "F:/Python/Projects/PyLearn-Course/Assignments-8/image/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)
imageio.mimsave("F:/Python/Projects/PyLearn-Course/Assignments-8/1.gif",IMAGES)