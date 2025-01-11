from setuptools import setup, find_packages

setup(
    name="blog_formatter",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
