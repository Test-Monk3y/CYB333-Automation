import sys, argparse
from psa.strength import grade

def main():
    p = argparse.ArgumentParser()
    p.add_argument("password", help="password to score")
    args = p.parse_args()
    print(grade(args.password))

if __name__ == "__main__":
    main()
# This script is the command-line interface for the password strength assessment tool.
# It uses argparse to handle command-line arguments and calls the grade function from the psa.strength