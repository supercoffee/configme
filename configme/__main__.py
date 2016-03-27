__author__ = 'ben'

from configme import load_config, make_args, ConfigMe

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