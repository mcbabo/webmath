from setuptools import setup, find_packages

# requirements = ["aiohttp >= 3.6.0", "urllib3"]
requirements = []

with open('requirements.txt') as f:
  requirements = f.read().splitlines()
  
# See note below for more information about classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="web_math",
    version="1.0.14",
    description="For online math api",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mcbabo/webmath",
    author="Moritz Joksch",
    license="MIT",  # note the American spelling
    classifiers=classifiers,
    keywords="discord discord-calc calculator easy-calc simple-calculator discord.py pycord python math",  # used when people are searching for a module, keywords separated with a space
    packages=find_packages(),
    install_requires=requirements,  # a list of other Python modules which this module depends on.  For example RPi.GPIO
    include_package_data=True
)
