import setuptools

from translate import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmd_fanyi",
    version=__version__,
    author="raojinlin",
    author_email="1239015423@qq.com",
    description="command line translate tool",
    keywords="translate chinese english translate translator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raojinlin/cmd-fanyi",
    packages=setuptools.find_packages(),
    scripts=[
        "bin/fanyi"
    ],
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
