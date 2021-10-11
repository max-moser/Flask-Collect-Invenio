# -*- coding: utf-8 -*-
#
# This file is part of Flask-Collect-Invenio.
# Copyright (C) 2012 - 2016 Kirill Klenov.
# Copyright (C) 2021        TU Wien.
#
# Flask-Collect-Invenio is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""
Flask-Collect-Invenio
---------------------

Setup module.

"""
import os
import sys

from os import path

from setuptools import setup, find_packages


def _read(fname):
    try:
        return open(path.join(path.dirname(__file__), fname)).read()
    except IOError:
        return ''

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("flask_collect", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)

install_requires = [
    "Flask>=0.10.1",
]

tests_require = [
    "black>=21.9b0",
    "check-manifest>=0.42",
    "coverage>=5.3,<6",
    "pytest>=6,<7",
    "pytest-cov>=2.10.1",
    "pytest-flask>=1.0.0",
    "pytest-isort>=1.2.0",
    "pytest-pycodestyle>=2.2.0",
    "pytest-pydocstyle>=2.2.0",
]

extras_require = {
    "docs": ["Sphinx>=3",],
    "tests": tests_require,
}

extras_require["all"] = []
for reqs in extras_require.values():
    extras_require["all"].extend(reqs)


META_DATA = dict(
    name='Flask-Collect-Invenio',
    version=version,
    license="BSD",
    description=_read('DESCRIPTION'),
    long_description=_read('README.rst'),
    platforms=('Any'),
    keywords="flask static deploy".split(),
    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url=' http://github.com/klen/Flask-Collect',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=[
        'pytest-runner',
    ] if needs_pytest else [],
)


if __name__ == "__main__":
    setup(**META_DATA)
