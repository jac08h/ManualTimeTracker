from parse_cl_args import get_args, process_date_args
import sys


def main():
    args = get_args(sys.argv[1:])
    d = process_date_args(args)
    print(list(d.daterange))


if __name__ == '__main__':
    main()
