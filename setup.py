from setuptools import setup
import os
file_path = "Readme.md"
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        long_description = f.read()
else:
    print(f"File '{file_path}' does not exist.")
    long_description = "https://pypi.org/project/polywrapper/"

setup(
    name='polywrapper',
    version='0.1.5',
    author='David',
    author_email='dwatnip123@gmail.com',
    description='A wrapper for interacting with Polygon DB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['polywrapper'],
    install_requires=[
        'websocket-client',
    ],
)
