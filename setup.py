from setuptools import setup, find_packages

setup(
    name="mycli",
    version="1.0",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "inquirer",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "mycli=mycli.main:main",  # Adjust according to your project structure
        ],
    },
      author="Mohd.Rushaad Buxy",
    author_email="m.rushaadq@gmail.com",
    description="A simple CLI tool for project setup automation made to make me look cool.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rushaad2911/Mycli",  # Your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
