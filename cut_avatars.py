from PIL import Image

image = Image.open("./lesson4/monro.jpg")

red_image, green_image, blue_image = image.split()

width_image = red_image.width
height_image = red_image.height
shift = 100

middle_coordinates = (shift/2, 0, width_image - shift/2,height_image)
left_coordinates = (shift, 0, width_image,height_image)
right_coordinates = (0, 0, width_image - shift,height_image)

cropped_left_red_image = red_image.crop(left_coordinates)
cropped_middle_red_image = red_image.crop(middle_coordinates)
shifted_red_image = Image.blend(cropped_left_red_image, cropped_middle_red_image, 0.5)

cropped_right_blue_image = blue_image.crop(right_coordinates)
cropped_middle_blue_image = blue_image.crop(middle_coordinates)
shifted_blue_image = Image.blend(cropped_middle_blue_image, cropped_right_blue_image, 0.5)

cropped_middle_green_image = green_image.crop(middle_coordinates)

new_shifted_image = Image.merge("RGB", (shifted_red_image, cropped_middle_green_image, shifted_blue_image))

new_shifted_image.thumbnail((80, 80))
new_shifted_image.save("avatar_monro.jpg")
