# Installation
Production installation instructions to come when ready to release

# Usage
```
usage: configme [-h] [-o PROJECTPATH] {deploy} config

positional arguments:
  {deploy}
  config                Configuration file in YAML format to load template
                        variables from

optional arguments:
  -h, --help            show this help message and exit
  -o PROJECTPATH, --projectpath PROJECTPATH
                        Project root path. All templates will be output
                        relative to this.

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

