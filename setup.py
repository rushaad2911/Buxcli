from setuptools import setup, find_packages

setup(
    name="buxcli",
    version="1.0.4",  
    packages=find_packages(),
    install_requires=[
        "inquirer",
        "rich",
        "click",
        "dotenv",
    ],
    entry_points={
        "console_scripts": [
            "buxcli=buxcli.main:cli",
        ],
    },
    author="Mohd. Rushaad Buxy",
    author_email="m.rushaadq@gmail.com",
    description="A simple CLI tool for alert you about your CLI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rushaad2911/Mycli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
