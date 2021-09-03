import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", help="User name")
parser.add_argument("-p", "--pwd", help="User password")
parser.add_argument("extras", nargs='*', help="Extra arguments")
args = parser.parse_args()

user = ''
pwd = ''
extras = []

if args.user:
    user = args.user

if args.pwd:
    pwd = args.pwd

if args.extras:
    extras = args.extras

print(f'User: {user}    Pwd: {pwd}      Files: {extras}')