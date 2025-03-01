from setuptools import setup, find_packages

setup(
    name="mycli",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "inquirer"
    ],
    entry_points={
        "console_scripts": [
            "mycli=mycli.main:main",  # Adjust according to your project structure
        ],
    },
)
