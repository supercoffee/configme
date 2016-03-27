# Configme
#### One config file to rule them all

Create one YAML config file for each environment, and use it to template all your project config files.
Mirror your project directory structure for each config file you need to generate, and place this structure
inside a directory named `templates`. (Support for custom template directories coming soon).

Run `configme example.yml` to generate all config files using variables in the `yml` file.


# Installation

`pip install configme`

# Usage
```
usage: configme [-h] [-o PROJECTPATH] [-f] config

positional arguments:
  config                Configuration file in YAML format to load template
                        variables from

optional arguments:
  -h, --help            show this help message and exit
  -o PROJECTPATH, --projectpath PROJECTPATH
                        Project root path. All templates will be output
                        relative to this.
  -f, --force           Force overwrite files that already exist.

```

# Development


```
# create a virtual env
virtualenv env

# load virtualenv
source env/bin/activate

# install pip requirements 
pip install -e .

```

