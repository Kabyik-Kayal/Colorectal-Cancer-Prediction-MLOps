"""Setup script for the Anime Recommendation System package."""
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Colorectal Cancer Prediction",
    version="0.1",
    author="Kabyik",
    packages=find_packages(),
    install_requires = requirements,
)