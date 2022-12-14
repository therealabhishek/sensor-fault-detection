from setuptools import find_packages,setup

setup(
    name="sensor",
    version="0.0.1",
    author="Abhishek",
    author_email="kul.abhishake@gmail.com",
    packages = find_packages(),
    install_requires= ["pymongo[srv]==4.2.0"]
)
