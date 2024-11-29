from picli.cli_setup import setup_cli
from picli import crop_module
from picli import compress_module
from picli import config_module

def main():
    parser = setup_cli()
    args = parser.parse_args()

    commands = {
        "help": lambda: parser.print_help(),
        "crop": lambda: crop_module.main(args),
        "compress": lambda: compress_module.main(args),
        "config": lambda: config_module.main(args)
    }

    unknown_command = commands["help"]
    commands.get(args.command, unknown_command)()

if __name__ == "__main__":
    main()