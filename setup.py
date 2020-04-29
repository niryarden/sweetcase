import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sweetcase",
    version="0.0.3",
    author="Nir Yarden",
    author_email="niryar@gmail.com",
    description="Simple and light-weight module allowing the use of a switch-case alike syntax in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niryarden/sweetcase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    python_requires=">=3.0"
)
