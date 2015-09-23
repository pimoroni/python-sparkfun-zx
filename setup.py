import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="zx",
    version="0.0.1",
    author="Phil Howard",
    description="A library for the Sparkfun ZX Distance and Gesture sensor",
    license="BSD",
    keywords=[
        "raspberrypi",
        "gpio",
    ],
    url="https://github.com/pimoroni/zx",
    packages=find_packages(),
    install_requires=[
        "RPi.GPIO",
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
