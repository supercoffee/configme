__author__ = 'ben'

from jinja2 import Environment, FileSystemLoader, Template
from os import getcwd, path, walk
import sys
from termcolor import colored
import yaml


def load_config(environment):
    filename = '{}.yml'.format(environment)
    try:
        with open(filename, 'r') as configfile:
            return yaml.load(configfile)
    except IOError:
        exit(colored('Config file {} does not exist'.format(filename), 'red'))

class ConfigMe():


    def deploy(self, environment):
        config = load_config(environment)
        template_paths = path.join(getcwd(), 'templates')
        env = Environment(loader=FileSystemLoader(template_paths))
        for template_name in env.list_templates('.j2'):
            template = env.get_template(template_name)
            print 'Rendering template: {}'.format(template_name)
            output = template.render(config)
            print output

def main():
    args = sys.argv
    command = args[1]
    cfg_manager = ConfigMe()
    method = getattr(cfg_manager, command)
    if method is not None:
        method(*args[2:])

if __name__ == "__main__":
    main()