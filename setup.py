# https://github.com/rdegges/skele-cli/blob/master/setup.py
from configme import __version__
from setuptools import find_packages, setup

# http://stackoverflow.com/questions/6947988/when-to-use-pip-requirements-file-versus-install-requires-in-setup-py
REQUIREMENTS = [
    'Jinja2',
    'MarkupSafe',
    'PyYAML',
    'termcolor'
]

setup(
    name = 'configme',
    version = __version__,
    description = 'A template based config file generator for general purposes.',
    author = 'Benjamin Daschel',
    author_email = 'coffeemaxed@gmail.com',
    url='https://github.com/supercoffee/configme',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['tests']),
    install_requires=REQUIREMENTS,
    entry_points = {
        'console_scripts': [
            'configme=configme.__main__:main',
    ],
},
)
