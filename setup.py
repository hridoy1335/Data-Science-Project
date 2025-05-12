from typing import List
from setuptools import setup, find_packages

HIPEN_E_DOT = "-e ."

def get_requirement_list()->List[str]:
    with open("requirements.txt", "r") as f:
        requirement_list = [line.strip() for line in f.readlines()]
        if HIPEN_E_DOT in requirement_list:
            requirement_list.remove(HIPEN_E_DOT)
            return requirement_list

setup(
    name="DataScience",
    version="1.0",
    author="Hridoy Khan",
    author_email="rkredoy1335@gmail.com",
    description="Data Science Project",
    url="https://github.com/hridoy1335/Data-Science-Project",
    packages=find_packages(),
    install_requires=get_requirement_list()
)