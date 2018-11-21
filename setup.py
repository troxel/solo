import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solo",
    version="1.0",
    author="Steven Troxel",
    author_email="troxel@perlworks.com",
    description="Stop all other instances of a program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/troxel/solo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
