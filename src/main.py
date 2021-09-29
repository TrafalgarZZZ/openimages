import pandas as pd
import os
from openimages.download import download_dataset

class_list = []

descriptions_csv_file_path = os.path.join("/openimages", "class-descriptions-boxable.csv")
with open(descriptions_csv_file_path) as f:
    lines = f.readlines()
    for line in lines:
        class_list.append(line.strip().split(',')[1])

print(class_list)

download_dataset(dest_dir="/openimages", class_labels=class_list, meta_dir="/openimages")