import file_handler
import os
from PIL import Image


def resize_image(img: Image.Image, target_mp: int) -> Image.Image:
    current_mp = (img.width * img.height) / 1000000
    shrink_factor = (current_mp / target_mp) ** 0.5
    return img.resize(
        (int(img.width / shrink_factor), int(img.height / shrink_factor)),
        Image.Resampling.LANCZOS,
    )


dir = "/home/bryancrisso/Pictures/photoportfolio_pic_store/originals/"
target_mp = 2

files = file_handler.create_hierarchy(dir)

jpegs = file_handler.select_jpegs(files)

for jpg in jpegs:
    original_i = jpg.index("originals")
    new_jpg = jpg.copy()
    new_jpg[original_i] = "processed"
    os.makedirs("/".join(new_jpg[:-1]), exist_ok=True)
    print("Resizing: " + "/".join(jpg[original_i + 1 :]))
    with Image.open("/".join(jpg)) as img:
        resized_img = resize_image(img, target_mp)
        resized_img.save("/".join(new_jpg))
