from setuptools import setup
with open('Readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='polywrapper',
    version='0.1.4',
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
