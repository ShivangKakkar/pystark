# PyStark - Python add-on extension to Pyrogram
# Copyright (C) 2021-2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of PyStark.
#
# PyStark is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStark is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyStark. If not, see <https://www.gnu.org/licenses/>.


import os
import sys
import argparse
from pystark import __description__, __version__


def main():
    parser = argparse.ArgumentParser(
        prog='pystark',
        description=__description__,
        usage='%(prog)s [options]',
        epilog='Enjoy the program :)',
        allow_abbrev=False,
        add_help=False
    )
    cwd = os.getcwd()
    parser.add_argument('-v', '--version', help='check the current pystark version installed', action='store_true')
    parser.add_argument('-bp', '--boilerplate', help='create boilerplate in current folder', action='store_true')
    parser.add_argument('-bph', '--boilerplate-heroku', help='create boilerplate in current folder with added heroku support', action='store_true')
    parser.add_argument('-s', '--special', help=argparse.SUPPRESS, action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    if args.version:
        print(f'v{__version__}')
        return
    if args.boilerplate_heroku or args.boilerplate or args.special:
        if args.special:
            print('Generating Boilerplate (for Stark Bots)...')
            boilerplate(special=True)
        elif args.boilerplate_heroku:
            print('Generating Boilerplate (with Heroku Support)...')
            boilerplate()
        else:
            print('Generating Boilerplate...')
            boilerplate()
            files = ['app.json', 'Procfile', 'README.md', 'requirements.txt']
            for file in files:
                os.remove(cwd+'/boilerplate/'+file)
        print('Done. Boilerplate is ready!')


def boilerplate(special=False):
    os.system('pip install github-clone --quiet')
    if special:
        os.system('ghclone https://github.com/StarkBotsIndustries/PyStark/tree/master/boilerplate_starkbots')
    else:
        os.system('ghclone https://github.com/StarkBotsIndustries/PyStark/tree/master/boilerplate')
    os.system('pip uninstall github-clone --quiet -y')
