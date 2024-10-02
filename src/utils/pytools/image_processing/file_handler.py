import os
from typing import List


def create_hierarchy(dir: str) -> List[List[str]]:
    list = []
    for root, _, files in os.walk(dir):
        path = root.split(os.sep)
        for file in files:
            list.append(path + [file])
    return list


def select_jpegs(files: List[List[str]]) -> List[List[str]]:
    return [file for file in files if file[-1].lower().endswith(".jpg")]


def read_json_string(filepath: str):
    with open(filepath, "r") as file:
        return file.read()
