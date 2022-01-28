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


from setuptools import setup, find_packages
from pystark import __version__
from pystark import __description__

with open("README.md", encoding="utf-8") as f:
    long_description = "\n".join([x for x in f.read().split("\n") if not x.startswith('>')])

with open("requirements.txt", encoding="utf-8") as r:
    install_requires = [i.strip() for i in r]

packages = find_packages()
version = __version__
description = __description__

setup(
    name='PyStark',
    packages=packages,
    version=version,
    license='GPLv3+',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='StarkProgrammer',
    author_email='starkbotsindustries@gmail.com',
    url='https://github.com/StarkBotsIndustries/PyStark',
    keywords=['telegram', 'bot', 'pyrogram', 'python', 'telegram-bot'],
    install_requires=install_requires,
    zip_safe=False,
    python_requires=">=3.6",
    dependency_links=['https://github.com/pyrogram/pyrogram/tarball/master'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Natural Language :: English',
        'Topic :: Communications :: Chat',
        'Topic :: Education :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    project_urls={
        "Support": "https://t.me/StarkBotsChat",
        "Community": "https://t.me/StarkBots",
        "Updates": "https://t.me/pystark",
        "Documentation": "https://pystark.codes/",
    },
    entry_points={
        'console_scripts': [
            'pystark = pystark.console:main',
        ],
    },
)
