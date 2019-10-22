import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmd_fanyi_raojinlin",
    version="0.0.1",
    author="raojinlin",
    author_email="1239015423@qq.com",
    description="command line translate tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raojinlin/cmd-fanyi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
