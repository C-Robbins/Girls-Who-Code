.# skeleton code for obamicon
from PIL import Image

# ===============================================================
# define colors as variables so we can recall them later:
# dark blue: (0, 51, 76)
# red: (217, 26, 33)
# light blue: (112, 150, 158)
# yellow: (252, 227, 166)
# ===============================================================

# ===============================================================
# define a function that obama-fies the image.
# this function will take your images' pixel list as a parameter.
# for each pixel in your image's pixel list, "obama-fy" it by 
# creating a new RGB value (dark blue, red, light blue, or yellow) 
# based on the intensity of that pixel. return a pixel list 
# containing the RGB values of the obamafied picture.
# ===============================================================

# ===============================================================
# ask the user for the image name and open the image
# ===============================================================

# ===============================================================
# convert the image into a list of pixel RGB values
# ===============================================================

# ===============================================================
# obamafy your image by calling your function
# ===============================================================

# ===============================================================
# create a new image and copy the new obama-fied pixel list into the image
# ===============================================================

# ===============================================================
# finally, show and save the image
# ===============================================================

darkblue = (0, 51, 76)
red = (217, 26, 33)
lightblue = (112, 150, 158)
yellow = (252, 227, 166)
def obamify(pixel_list):
	for index in range(len(pixel_list)):
		if pixel_list[index][0]+pixel_list[index][1]+pixel_list[index][2] < 182:
			pixel_list[index] = darkblue
		elif pixel_list[index][0]+pixel_list[index][1]+pixel_list[index][2] <=364 and pixel_list[index][0]+pixel_list[index][1]+pixel_list[index][2] >= 182:
			pixel_list[index] = red
		elif pixel_list[index][0]+pixel_list[index][1]+pixel_list[index][2] <= 546 and pixel_list[index][0]+pixel_list[index][1]+pixel_list[index][2] > 364:
			pixel_list[index] = lightblue
		else:
			pixel_list[index] = yellow
	return pixel_list

image = input("What image do you want? ")
im = Image.open(image +".jpg")
x = obamify(list(im.getdata()))
obamify
im.putdata(x)
im.save(image+"_obamafied.jpg")
im.show()




# (list(im.getdata()))


