from setuptools import setup

setup(
    name='printdate',
    version='1.0',
    author='Pavlov',
    packages=['printdate'],
    description='Print date to terminal',
    package_data={'': ['*.txt']},
    install_requires=[],
    entry_points={'console_scripts': ['printdate = printdate.printdate:main']},
)
