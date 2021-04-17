from sfdnormalize import NAME, VERSION_STR
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=VERSION_STR,
    author="Caleb Maclennan",
    author_email="caleb@alerque.com",
    description="Discard GUI information from SFD files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alerque/sfdnormalize",
    entry_points = {'console_scripts': ['sfdnormalize = sfdnormalize.__main__:main'],},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
