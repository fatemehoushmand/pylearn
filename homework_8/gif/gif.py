import os
import imageio


file_list = os.listdir("new")

IMAGES = []
for file_name in file_list:
    file_path = "new/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("my_ouswdsewtput.gif/", IMAGES)
print("Gif is Ready!!!")

# import cv2
# import os
# # Path to the folder containing images
# folder_path = "images"

# # List all files in the folder
# files = os.listdir(folder_path)

# # Loop through each file in the folder
# for file in files:
#     # Read the image
#     image = cv2.imread(os.path.join(folder_path, file))
    
#     # Resize the image to 300x300 pixels
#     resized_image = cv2.resize(image, (300, 300))
    
#     # Save the resized image in a new folder
#     save_path = "new/" + file
#     cv2.imwrite(save_path, resized_image) 

# print("Images resized and saved successfully!")