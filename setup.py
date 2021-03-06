#!/usr/bin/env python
#coding=utf-8

from setuptools import setup

setup(name='SpikeSort',
      version='0.1',
      description='Python Spike Sorting Package',
      author='Bartosz Telenczuk',
      author_email='bartosz.telenczuk@gmail.com',
      url='http://neuroscience.telenczuk.pl',
      packages=['spike_sort', 
                'spike_sort.core', 
                'spike_sort.ui',
                'spike_sort.io', 
                'spike_beans',
                'spike_analysis',
                ],
      package_dir = {"": "src"},
      install_requires=[
          'matplotlib',
          'tables',
          'numpy >= 1.4.1',
          'scipy'
        ]
      
     )

