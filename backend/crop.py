from os import name
from os.path import exists
from PIL import Image


directory = "Siskiyou_CA/"
filename = "SiskiyouCA_"
cropped_directory = "Siskiyou_cropped/"
for i in range(11,21):
    file_exists = exists(directory+filename+str(i)+".png")
    if(not file_exists):
        continue
    im = Image.open(directory+filename+str(i)+".png")

    def crop_center(pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                            (img_height - crop_height) // 2,
                            (img_width + crop_width) // 2,
                            (img_height + crop_height) // 2))

    def crop_max_square(pil_img):
        return crop_center(pil_img, min(pil_img.size)-35, min(pil_img.size)-35)

    im = crop_max_square(im)

    im.save(cropped_directory+filename+str(i)+".png", quality=100)