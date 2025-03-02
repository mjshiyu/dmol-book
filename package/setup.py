import os
from glob import glob
from setuptools import setup

setup(
    name="dmol-book",
    version="1.3.2",
    description="Style and Imports for dmol Book",
    author="Andrew D White",
    author_email="andrew.white@rochester.edu",
    url="https://dmol.pub",
    license="MIT",
    packages=["dmol"],
    install_requires=[
        "jupyter-book==0.13.1",
        "matplotlib",
        "numpy",
        "ipython!=8.7.0",
        "jax",
        "jaxlib",
        "pandas",
        "tensorflow>=2.7",
        "seaborn",
        "tabulate",
        "scikit-learn",
        "pydot",
        "pillow>=8.3.2",
        "mordred[full]",
        "moviepy",
        "networkx",
        "MDAnalysis",
        "emlp==1.0.3",
        "tensorflow-probability",
        "dm-haiku",
        "selfies",
        "tensorflowjs",
        "exmol",
        "rdkit>=2022",
        "sympy",
        "e3nn",
        "torch==1.12",  # note - if you want to change this, change the github action too
        "simpletransformers==0.63.9",
        "linkify-it-py",
    ],
    test_suite="tests",
    long_description="""
# Style and Imports for dmol Book

This is the style and imports for deep learning for molecules and materials
written by Andrew White. Please see the [dmol book](https://dmol.pub) or
root package at [github](https://github.com/whitead/dmol-book).
""",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Typing :: Typed",
    ],
)
