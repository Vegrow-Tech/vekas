from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requires = f.read().splitlines()
except IOError:
    with open('vekas.egg-info/requires.txt') as f:
        requires = f.read().splitlines()

with open('VERSION') as f:
    version = f.read().strip()

setup(
    # If name is changed be sure to update the open file path above.
    name="vekas",
    version=version,
    packages=find_packages(),
    package_dir={'vekas': 'vekas'},
    author='vekas',
    description='Database Layer access used across vekas',
    license="PSF",
    include_package_data=True,
) 
