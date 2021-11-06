from setuptools import setup, find_packages

requirements = []

with open("requirements.txt", "r") as f:
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
    version="1.1.3",
    description="For online math api",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mcbabo/webmath",
    author="Moritz Joksch",
    license="MIT",
    classifiers=classifiers,
    keywords="discord discord-calc calculator easy-calc simple-calculator discord.py pycord python math",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True
)
