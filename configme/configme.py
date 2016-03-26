__author__ = 'ben'

import argparse
from jinja2 import Environment, FileSystemLoader, Template
from os import getcwd, makedirs, path
from termcolor import colored
import yaml

DEFAULT_EXTENSION = '.j2'
DEFAULT_TEMPLATE_PATH = 'templates'
USAGE = 'Usage: python configme.py deploy <environment>'


def load_config(filename):
    try:
        with open(filename, 'r') as configfile:
            return yaml.load(configfile)
    except IOError:
        raise Exception(colored('Config file {} does not exist'.format(filename), 'red'))


def get_template_path(template_path=''):
    if path.isabs(template_path):
        return template_path
    if not template_path:
        template_path = path.join(getcwd(), DEFAULT_TEMPLATE_PATH)
    else:
        template_path = path.join(getcwd(), template_path)

    if not path.exists(template_path):
        raise Exception(colored('Template path does not exist', 'red'))
    return template_path


class ConfigMe():

    def __init__(self, template_vars, project_path):
        self.template_vars = template_vars
        self.project_path = project_path

    def _create_output_path(self, output_path):
        """
        Create directory structure recursively if not existing
        :param output_path: path of directories to create
        :return:
        """
        if not path.exists(path.dirname(output_path)):
            makedirs(path.dirname(output_path))

    def save_output(self, rel_path, contents):
        """
        :param rel_path: file output path relative to project path
        :param contents: output of rendered template
        :return:
        """
        output_path = path.join(self.project_path, rel_path)
        if path.exists(output_path):
            print colored('Skipping file; File already exists: {}'.format(path), 'yellow')
            return
        self._create_output_path(output_path)
        with open(output_path, 'w') as outfile:
            outfile.write(contents)

    def deploy(self):
        template_paths = path.join(getcwd(), 'templates')
        env = Environment(loader=FileSystemLoader(template_paths))
        for template_name in env.list_templates(DEFAULT_EXTENSION):
            template = env.get_template(template_name)
            print 'Rendering template: {}'.format(template_name)
            output = template.render(self.template_vars)
            self.save_output(path.splitext(template_name)[0], output)


def make_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['deploy'])
    parser.add_argument('config', help='Configuration file in YAML format to load template variables from')
    parser.add_argument('-o', '--projectpath',
                        help='Project root path. All templates will be output relative to this.', default=getcwd())
    return parser.parse_args()

def main():
    args = make_args()
    config = load_config(args['config'])
    cfg_manager = ConfigMe(config, args['projectpath'])
    method = getattr(cfg_manager, args['command'])
    try:
        if method is not None:
            method()
    except Exception as e:
        print e


if __name__ == "__main__":
    main()