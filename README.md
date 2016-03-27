# Configme
#### One config file to rule them all

1. Create one YAML config file for each environment. This holds all the variables to template the config files.
2. Create a `templates` directory and make Jinja2 templates for each config file you want to generate
3. Run `configme myconfig.yml` to generate all config files using variables in the `myconfig.yml` file. Configme
will automatically populate your project with the generated configs.

The directory structure of your `templates` directory should mirror the relative path of the final config file.
If you want to make a config file `app/config/database.php`,
you should have a `app/config/database.php.j2` file in your `templates` directory.

See `example` folder for more project structure and sample use cases.

# Installation

`pip install configme`

# Usage
```
usage: configme [-h] [-o PROJECTPATH] [-t TEMPLATEPATH] [-f] config

positional arguments:
  config                Configuration file in YAML format to load template
                        variables from

optional arguments:
  -h, --help            show this help message and exit
  -o PROJECTPATH, --projectpath PROJECTPATH
                        Project root path. All templates will be output
                        relative to this. Defaults to current directory
  -t TEMPLATEPATH, --templatepath TEMPLATEPATH
                        Path to templates directory. Defaults to ./templates
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

# generate configs in example project
cd example
configme -f dev.yml

```

