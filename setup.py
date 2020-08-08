import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Binod", # Replace with your own username
    version="0.2.0",
    author="Jayanta Banik",
    author_email="sciencenerd1609@gmail.com",
    description="Binod",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jayanta-banik/IProgress",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4'
)