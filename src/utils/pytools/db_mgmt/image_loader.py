import database_handle
import sys
import os

sys.path.insert(0, "..")
from config import load_config
from image_processing import file_handler

config_path = "../../config/config.ini"
image_path = "/home/bryancrisso/Pictures/photoportfolio_pic_store/processed/"
exif_path = "/home/bryancrisso/Pictures/photoportfolio_pic_store/exif_data/"

# connect to database
db = database_handle.Database(**load_config(config_path, "postgresql"))

# create new album
album_id = db.insert_album(
    "La Rochelle Film",
    "August 2024",
    "La Rochelle, France",
    "La Rochelle Film/000020430008.JPG",
    "Family trip to the city of La Rochelle in southwestern France",
)
print(album_id)

# get image data
files = file_handler.create_hierarchy(image_path + "La Rochelle Film")
image_data = [
    (
        album_id,
        os.sep.join(fpath[len(image_path.split(os.sep)) - 1 :]),
        "",
        file_handler.read_json_string(
            exif_path
            + os.sep.join(fpath[len(image_path.split(os.sep)) - 1 :])
            + ".json"
        ),
    )
    for fpath in files
]

# add images to database
db.insert_images(image_data)

db.close()
