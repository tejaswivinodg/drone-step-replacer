# -*- coding: utf-8 -*-
__binary_name__ = "drone-step-replacer"
__author__ = "SRE-Developer-tools"
__author_email__ = "developer-tools-all@squarespace.com"
__description__ = "drone-step-replacer cli to make changes in drone config"
__version__ = "0.0.1"


from drone_replacer_cli import cli


def main():
    cli()


if __name__ == "__main__":
    main()
