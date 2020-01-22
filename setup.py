import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kdfconn", # Replace with your own username
    version="0.0.1",
    author="Jason Wu",
    author_email="rewreu@gmail.com",
    description="A library to connect pandas with Kinetica",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rewreu/kdfconn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)