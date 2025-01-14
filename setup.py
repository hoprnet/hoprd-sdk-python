# coding: utf-8

"""
    hoprd-api

    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501

    OpenAPI spec version: 3.10.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "hoprd-sdk"
VERSION = "2.2.0-rc.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="hoprd-api",
    author_email="tech@hoprnet.org",
    url="https://github.com/hoprnet/hoprd-sdk-python",
    keywords=["Swagger", "hoprd-api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This Rest API enables developers to interact with a hoprd node programatically through HTTP.  # noqa: E501
    """
)
