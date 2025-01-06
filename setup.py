from setuptools import setup, find_packages

setup(
    name="ds-ml-toolkit",
    version="0.1.0",
    description="A toolkit Python package with helper functions",
    author="Praneet Nigam",
    author_email="praneet.nigamil@tide.co",
    url="https://github.com/PraneetNigamTide/ds-ml-toolkit",
    packages=find_packages(),
    install_requires=[
        "pyspark",
        "snowflake-connector-python",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)