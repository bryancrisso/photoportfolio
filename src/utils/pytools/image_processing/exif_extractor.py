import os
import json
import exif
import file_handler

dir = "/home/bryancrisso/Pictures/photoportfolio_pic_store/originals/"
files = file_handler.create_hierarchy(dir)
jpegs = file_handler.select_jpegs(files)
chosen_tags = set(
    [
        "make",
        "model",
        "datetime",
        "exposure_time",
        "f_number",
        "photographic_sensitivity",
        "focal_length",
        "lens_model",
    ]
)


def get_exif(filepath: str) -> dict:
    exif_data = {tag: None for tag in chosen_tags}
    with open(filepath, "rb") as file:
        img_exif = exif.Image(file)
        for tag in img_exif.list_all():
            if tag in chosen_tags:
                exif_data[tag] = img_exif.get(tag)
    return exif_data


def write_dict_to_json(data: dict, filepath: str):
    with open(filepath, "w") as file:
        json.dump(data, file)


for jpg in jpegs:
    new_dir = list(dir.split(os.sep)[:-2]) + ["exif_data"]
    new_jpg = new_dir + jpg[len(new_dir) :]
    os.makedirs("/".join(new_jpg[:-1]), exist_ok=True)
    exif_data = get_exif("/".join(jpg))
    write_dict_to_json(exif_data, "/".join(new_jpg[:-1] + [jpg[-1] + ".json"]))
