#!/usr/bin/env python3

from setuptools import setup, find_packages

REPOSITORY:str = "https://www.github.com/cosasdepuma/XPLOITV"

def readme() -> str:
    return "Xploitv"

def requirements() -> list:
    pass

setup(
    name='xploitv',
    version='0.1.0',
    description='An automated Xploitv grabber',
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="WTFPL",
    keywords="xploitv facebook grabber hacking",
    author='Kike Fontan (@CosasDePuma)',
    author_email='kikefontanlorenzo@gmail.com',
    url="https://fsundays.tech/",
    project_urls={
        "Bug Tracker": f"{REPOSITORY}/issues",
        "Documentation": REPOSITORY,
        "Source Code": REPOSITORY
    },
    packages=find_packages(),
    zip_safe=True,
    install_requires=requirements(),
    python_requires=">=3.8",
    platforms=["any"],
    entry_points={ 'console_scripts': ['xploitv=xploitv:cli'] },
    classifiers=[
        "Environment :: Console",
        "License :: Free For Educational Use",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Education :: Testing",
        "Topic :: Games/Entertainment",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Security",
        "Topic :: Utilities"
    ]
)
