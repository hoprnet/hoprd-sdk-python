# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.2.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import find_packages, setup  # noqa: H301

NAME = "hoprd-sdk"
VERSION = "2.1.0"
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
    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501
    """
)
