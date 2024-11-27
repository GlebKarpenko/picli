from setuptools import setup, find_packages

setup(
    name="picli",
    version="1.0.0",
    author="Gleb Karpenko",
    author_email="glebkarpenko1@gmail.com",
    description="A CLI toolset for automated image editing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GlebKarpenko/image-editor",
    packages=find_packages(),
    entry_points={
        # CLI command mapped to main.py's main() function
        "console_scripts": [
            "picli=image_tools.main:main",
        ],
    },
    install_requires=[
        "Pillow",
        "pytest"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
