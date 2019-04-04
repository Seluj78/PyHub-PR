#!/usr/bin/env python3

import setuptools

with open("README.md") as readme:
    long_description = readme.read()

setuptools.setup(
    name="pyhub_pr",
    version='0.0.1',
    description="Will create an issue from the command line with given parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jules Lasne",
    author_email="jules.lasne@gmail.com",
    url="https://github.com/seluj78/pyhub_pr",
    packages=["pyhub_pr"],
    package_dir={"pyhub_pr": "pyhub_pr"},
    entry_points={"console_scripts": ["pyhub_pr=pyhub_pr.pyhub_pr:main"]},
    include_package_data=True,
    install_requires=["requests"],
    license="MIT license",
    zip_safe=False,
    keywords="pyhub_pr",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
