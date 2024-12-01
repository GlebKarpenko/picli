from setuptools import setup, find_packages

version = {}
with open("picli/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="picli",
    version=version["__version__"],
    author="Gleb Karpenko",
    author_email="glebkarpenko1@gmail.com",
    description="A CLI toolset for automated image editing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GlebKarpenko/picli",
    packages=find_packages(),
    entry_points={
        # CLI command mapped to main.py's main() function
        "console_scripts": [
            "picli=picli.main:main",
        ],
    },
    package_data={
        "": ["resources/*.yaml"],
    },
    install_requires=[
        "pyyaml",
        "Pillow",
        "pytest",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
