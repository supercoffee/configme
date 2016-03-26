__author__ = 'ben'

import sys
from termcolor import colored
import yaml


class ConfigMe():

    def deploy(self, environment):
        filename = '{}.yml'.format(environment)
        try:
            with open(filename, 'r') as configfile:
                config = yaml.load(configfile)
        except IOError:
            exit(colored('Config file {} does not exist'.format(filename), 'red'))


def main():
    args = sys.argv
    command = args[1]
    cfg_manager = ConfigMe()
    method = getattr(cfg_manager, command)
    if method is not None:
        method(*args[2:])

if __name__ == "__main__":
    main()