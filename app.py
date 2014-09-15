#!/usr/bin/python

from namezilla import Namezilla


def main():
    namez = Namezilla()
    namez.render_options()
    namez.capture_option()
    namez.generate_name()
    print namez
    if namez.render_repeater():
        main()


if __name__ == '__main__':
    main()
