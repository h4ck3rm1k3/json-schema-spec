# -*- coding: utf-8 -*-

"""
"""

__status__ = "alpha"
__version__ = "1.0.0a"
__maintainer__ = (u"James Michael DuPont <jamesmikedupont@gmail.com>", )
__author__ = (u"James Michael DuPont <jamesmikedupont@gmail.com>", )

# Setup tools
from setuptools import setup, find_packages


setup(
    name = 'json-schema-spec-python',
    use_scm_version=True,
    packages = find_packages(),
    author = "James Michael DuPont <jamesmikedupont@gmail.com>",
    maintainer = "James Michael DuPont <jamesmikedupont@gmail.com>",
    description = "JSON Schema Spec",
    keywords = ['json', 'schema',],
    license = 'BSD',
    url = 'http://json-schema.org',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires = [
    ],
    setup_requires = [ 'versiontools >= 1.3.1', ],
    tests_require = [ 'unittest2 >= 0.5.1' ],
    zip_safe = True)

