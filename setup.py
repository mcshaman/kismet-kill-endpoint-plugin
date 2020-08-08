#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='kismet-kill-endpoint-plugin',
    version='1.0.0',
    description='Kill Kismet service',
    author='McShaman',
    author_email='info@mcshaman.com',
    python_requires='>=3.2',
    install_requires=['psutil', 'kismetexternal'],
    scripts=['bin/kismet-kill-endpoint-plugin'],
)
