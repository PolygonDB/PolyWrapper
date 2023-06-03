from setuptools import setup

setup(
    name='polywrapper',
    version='0.1.2',
    author='David',
    author_email='dwatnip123@gmail.com',
    description='A wrapper for interacting with Polygon DB',
    packages=['polywrapper'],
    install_requires=[
        'websocket-client',
    ],
)
