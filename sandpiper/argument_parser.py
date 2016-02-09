
import sys
import argparse


class ArgumentParser(object):
    """
    Parses input arguments
    """

    def start(self):
        print ('sys.argv')
        print (sys.argv)

        parser = argparse.ArgumentParser()
        parser.add_argument('--level', help='logging level')
        args = parser.parse_args()

        if args.level:
            print('arg: logging level: ' + args.level)

        return args.level

