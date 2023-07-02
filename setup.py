from gitfs import __version__
from setuptools import setup, find_packages

REQUIREMENTS = [line.strip() for line in open("requirements.txt").readlines()]

setup(
    name="pessiumus-gitfs",
    version=__version__,
    platforms="any",
    description="Version controlled file system.",
    author="Presslabs",
    author_email="gitfs@presslabs.com",
    url="http://www.presslabs.com/gitfs/",
    packages=find_packages(exclude=["tests", "tests.*"]),
    entry_points={"console_scripts": ["gitfs = gitfs:mount"]},
    zip_safe=False,
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
