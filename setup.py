from setuptools import setup, find_packages

setup(
    name='fast-style-transfer',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=[''],
    url='https://github.com/GalDude33/fast-neural-style-keras',
    author='GalDude33',
    author_email=''
)
