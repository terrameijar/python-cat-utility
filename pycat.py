# A program similar to the cat utility. Outputs file contents to
# standard output.

import sys
import argparse


def handle_input(args):
    parser = argparse.ArgumentParser(
            prog="pycat",
            description="Output file contents to standard output.",
            usage="%(prog)s [FILE]")
    parser.add_argument(
            "FILE", help="Output FILE's contents"
            )
    parser.add_argument(
            "-b", "--number_nonblank",
            action="store_true", help="number nonempty output lines")
    return parser.parse_args(args)


def main(args):
    try:
        parser_object = handle_input(args)
        filename = parser_object.FILE
        try:
            with open(filename, 'rt') as fobj:
                if parser_object.number_nonblank:
                    line_num = 0
                    for line in fobj:
                        if line not in ['\n', '\r\n']:
                            line_num += 1
                            print '     ', line_num, line,
                else:
                    output = fobj.read()
                    print(output)
        except IOError:
            print(sys.argv[0] + ' No such file or directory')
    except KeyboardInterrupt as kberror:
        print kberror


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
