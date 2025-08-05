from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hdd-cdd-calculator",
    version="0.1.0",
    author="Ryan Kmetz",
    author_email="consultrmk@gmail.com",
    description="A Python library for calculating Heating Degree Days (HDD) and Cooling Degree Days (CDD) using NWS API data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmkenv/hdd_cdd_calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.900",
        ],
    },
)
