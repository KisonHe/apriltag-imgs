import argparse
import os
import sys
import subprocess

# Thanks to https://stackoverflow.com/a/54547257
def dir_path(file_path):
    if os.path.isdir(file_path):
        return file_path
    else:
        raise argparse.ArgumentTypeError(f'Supplied argument "{file_path}" is not a valid folder path.')


parser = argparse.ArgumentParser()

parser.add_argument(
    'family_path', type=dir_path, 
    help='The path to the apriltag png you want to convert.'
)

parser.add_argument(
    'percent', type=int, 
    help='percent% you want to scale'
)

parser.add_argument(
    'start', type=int, 
    help='start num to convert'
)

parser.add_argument(
    'end', type=int, 
    help='end num to convert'
)

def main():
    args = parser.parse_args()
    family_path = args.family_path
    percent = args.percent
    start = args.start
    end= args.end

    # switch family path 
    prefix = 'tag52_13_'
    subprocess.run(['mkdir', 'output'])

    for i in range(start,end):
        filename = '{}{:05d}.png'.format(prefix, i)
        print(filename)
        # Popen will crash running out of mem! 
        subprocess.run(['convert', os.path.join(family_path,filename), '-scale', f'{percent}%', f'./output/{filename}' ])

if __name__ == "__main__":
    main()

