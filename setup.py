#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = []

with open("requirements_dev.txt") as f:
    tests_require = [ req.strip() for req in f.readlines() ]

with open("requirements.txt") as f:
    install_requires = [ req.strip() for req in f.readlines() ]

setup(
    author="Kyle Alexander Pena",
    author_email='kp1197@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3 :: Only",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',   
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing',
        'Topic :: Utilities' 
    ],
    description="readyregex contains a wide range of customizable and ready-made regex patterns for everyday use",
    install_requires=install_requires,
    license="Apache Software License 2.0",
    include_package_data=True,
    keywords='readyregex',
    name='readyregex',
    packages=find_packages(exclude=['tests']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/kyle-pena-nlp/readyregex',
    version='0.0.1',
    zip_safe=False,
)
