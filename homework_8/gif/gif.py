import os
import imageio

file_list = os.listdir("homework_8/gif/images")


IMAGES = []
for file_name in file_list:
    file_path = "homework_8/gif/images" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("homework_8/gif/my_output.gif", IMAGES)
print("Gif is Ready!!!")