from os import path

from setuptools import find_packages, setup


def read(fname):
    this_directory = path.abspath(path.dirname(__file__))
    return open(path.join(this_directory, fname), encoding="utf-8").read()


setup(
    name="pytest-tests-completion",
    version="0.0.1",
    description="Bash completion for pytest tests",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="http://github.com/wolkenarchitekt/pytest-tests-completion",
    author="Ingo Fischer",
    author_email="mail@ingofischer.de",
    license="GPL",
    packages=find_packages(exclude=("tests",)),
    zip_safe=True,
    python_requires=">=3.7.0",
    install_requires=["pytest"],
)
