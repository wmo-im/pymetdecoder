from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = "pymetdecoder-wmo",
    version          = "0.1.11",
    author           = "Tim Barnes",
    author_email     = "tdba@bas.ac.uk",
    description      = "Python module to decode/encode met reports e.g. SYNOPs, adapted for use for the synop2bufr module.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url              = "https://github.com/wmo-im/pymetdecoder",
    license          = "Open Government License v3.0",
    packages         = [
        "pymetdecoder",
        "pymetdecoder.synop"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3"
    ]
)
