__author__ = 'ben'

from jinja2 import Environment, FileSystemLoader, Template
from os import getcwd, makedirs, path
import sys
from termcolor import colored
import yaml

DEFAULT_EXTENSION = '.j2'

def load_config(environment):
    filename = '{}.yml'.format(environment)
    try:
        with open(filename, 'r') as configfile:
            return yaml.load(configfile)
    except IOError:
        exit(colored('Config file {} does not exist'.format(filename), 'red'))

def save_output(output_path, contents):
    if path.exists(output_path):
        print colored('Skipping file; File already exists: {}'.format(path), 'yellow')
        return
    if not path.exists(path.dirname(output_path)):
        makedirs(path.dirname(output_path))
    with open(output_path, 'w') as outfile:
        outfile.write(contents)

class ConfigMe():


    def deploy(self, environment):
        config = load_config(environment)
        template_paths = path.join(getcwd(), 'templates')
        env = Environment(loader=FileSystemLoader(template_paths))
        for template_name in env.list_templates(DEFAULT_EXTENSION):
            template = env.get_template(template_name)
            print 'Rendering template: {}'.format(template_name)
            output = template.render(config)
            save_output(path.splitext(template_name)[0], output)

def main():
    args = sys.argv
    command = args[1]
    cfg_manager = ConfigMe()
    method = getattr(cfg_manager, command)
    if method is not None:
        method(*args[2:])

if __name__ == "__main__":
    main()