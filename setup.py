from setuptools import setup, find_packages

setup(
    name="short_link_sdk",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "requests",
        "setuptools",
    ],
    author="kurama784",
    description="Short link SDK client for Python",
    url="https://github.com/kurama784/short_link_python_sdk",
)