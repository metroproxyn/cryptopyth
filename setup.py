from setuptools import setup, find_packages
"""
The setup.py file is the build script for your package. 
The setup function from Setuptools will build your package for upload to PyPI. 
Setuptools includes information about your package, your version number, 
and which other packages are required for users.
"""
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

# TBS: