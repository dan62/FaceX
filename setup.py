import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FaceX",
    version="0.0.1",
    author="Daniel Goncalves",
    author_email="danielgoncalves62@gmail.com",
    description="A package that performs complex 3D computations on the human face",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dan62/FaceX",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
