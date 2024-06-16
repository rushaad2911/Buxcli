# setup.py

from setuptools import setup, find_packages

setup(
    name='mycli',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mycli = mycli.main:main',
        ],
    },
    author='Mohammed Rushaad Buxy',
    author_email='m.rushaadq@gmail.com',
    description='A comprehensive CLI tool to Automate Project Creation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rushaad2911/Mycli.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
