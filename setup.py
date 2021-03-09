from setuptools import setup, find_packages
import pathlib, inspect
import ptnet

long_description = pathlib.Path("README.md").read_text(encoding="utf-8")
description = inspect.cleandoc(ptnet.__doc__).splitlines()[0]

setup(name="ptnet",
      description=description,
      long_description=long_description,
      url="https://github.com/fpom/cunf-ptnet-py3",
      author="Franck Pommereau",
      author_email="franck.pommereau@univ-evry.fr",
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Topic :: Scientific/Engineering",
                   "Programming Language :: Python :: 3",
                   "Operating System :: OS Independent"],
      packages=find_packages(where="."),
      python_requires=">=3.7",
)
