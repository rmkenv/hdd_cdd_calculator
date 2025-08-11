from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hdd-cdd-calculator",
    version="0.1.3",  # Updated to match __init__.py
    author="Ryan Kmetz",
    author_email="consultrmk@gmail.com",
    description="A Python library for calculating Heating Degree Days (HDD) "
                "and Cooling Degree Days (CDD) using NWS API data, "
                "with support for other weather data sources like Meteostat.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmkenv/hdd_cdd_calculator",
    packages=find_packages(exclude=["tests*", "docs*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28",
        "pandas>=1.3",
        "meteostat>=1.6.5",
        "python-dateutil>=2.8",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    include_package_data=True,
    license="MIT",
)
