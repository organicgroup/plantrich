from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in plantrich/__init__.py
from plantrich import __version__ as version

setup(
	name="plantrich",
	version=version,
	description="Empowering Farmers",
	author="sammish",
	author_email="sammish.thundiyil@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
