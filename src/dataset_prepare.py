import os
import shutil
from tqdm import tqdm

path = "/Users/zhxu/Workspace/datasets/openimages"
entries = os.listdir(path)

for entry in entries:
    entry_path = os.path.join(path, entry)
    if os.path.isfile(entry_path):
        continue

    entry_images_path = os.path.join(entry_path, "images")
    images = []
    if os.path.exists(entry_images_path):
        images = os.listdir(entry_images_path)

    print(images)
    if len(images) == 0:
        shutil.rmtree(entry_path)
    else:
        for image in images:
            src_path = os.path.join(entry_images_path, image)
            dest_path = os.path.join(entry_path, image)
            shutil.move(src_path, dest_path)
        shutil.rmtree(entry_images_path)