from setuptools import setup
import os


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='gdrive_deploy',
    version='1.0',
    packages=['gdrive_deploy'],
    url='https://www.github.com/keni7385/gdrive-deploy',
    license='MIT',
    author='keni7385',
    author_email='andrea.corsini@outlook.com',
    description='Tiny utility to deploy file by name to google drive',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=['googleapiclient', 'httplib2', 'google-api-python-client']
)
