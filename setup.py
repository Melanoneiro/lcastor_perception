#!/usr/bin/env python3

import os
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup


def parse_package_requirements():
    requirements_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
    with open(requirements_file, "r") as fh:
        return [x.strip() for x in fh.readlines()]


setup_args = generate_distutils_setup(
    packages=['lcastor_perception'],
    package_dir={'': 'src'},
    install_requires=parse_package_requirements(),
)

setup(**setup_args)
