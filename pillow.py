from PIL import Image

# filename = 'house.png'
# with Image.open(filename) as img:
#     img.load()

# print(type(img))
# print(isinstance(img, Image.Image))
# img.show()

# You can explore these using the Image class attributes .format, .size, and .mode
# print('the image format is {} with size {} and model {}'.format(img.format,  img.size, img.mode))

#.crop() and .resize():
# cropped_img = img.crop((300, 150, 700, 1000))
# print(cropped_img.size)
# cropped_img.show()

# ow_res_img = cropped_img.resize(
#    (cropped_img.width // 4, cropped_img.height // 4)
#  )

# ow_res_img.show()
# low_res_img = cropped_img.reduce(4)
# low_res_img.show()
# cropped_img.save("cropped_image.png")

# converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
# converted_img = img.transpose(Image.TRANSPOSE)
# converted_img = img.transpose(Image.ROTATE_270)
# converted_img = img.transpose(Image.TRANSVERSE)
# converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# converted_img.show()

# rotated_img = img.rotate(125)
# rotated_img = img.rotate(45, expand=True)
# rotated_img.show()

filename = "strawberry.jpg"
with Image.open(filename) as img:
    img.load()

# img.show()
# cmyk_img = img.convert("CMYK")
# gray_img = img.convert("L")

#cmyk_img.show()
# gray_img.show()
# print(img.getbands())
# print(cmyk_img.getbands())
# print(gray_img.getbands())

red, green, blue = img.split()
print(red)
print(red.mode)