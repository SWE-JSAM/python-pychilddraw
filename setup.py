# Authors: Jörgen Samuelsson <samuelssonjorgen@gmail.com>
# Barnkladd is a gamine clone see http://gnunux.info/projets/gamine/
# This is a total re-implementation but now in python.
# Most of the game assets are from gamine, see license
# The application is reimplemented by JSAM-SWE
# 
# barnkladd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# barnkladd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with barnkladd. If not, see <http://www.gnu.org/licenses/gpl.html>.


import os
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

def add_data():
    try:
        data_files = [('share/applications', ['extra/barnkladd.desktop']),
                ('share/pixmaps', ['extra/barnkladd.png'])]
        return data_files
    except:
        return

if os.name == 'posix':
    data_files = add_data()
else:
    data_files = None

setup(
    name = 'barnkladd',
    version = '0.5.0',
    author='Jörgen Samuelsson',
    author_email='samuelssonjorgen@gmail.com',
    install_requires=['setuptools', 'pygame>=1.9.1'],
    url = 'https://github.com/SWE-JSAM/barnkladd',
    description = 'A small children drawing program',
    long_description=long_description,
    license='GPLv3',
    packages = ['barnkladd'],
    include_package_data=True,
    data_files=data_files,
    zip_safe=False,
    classifiers=[
        'Development Status :: Beta',
        'Environment :: X11 Applications',
        'Intended Audience :: Children',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Drawing',
    ],
    entry_points={
        'gui_scripts': [
            'barnkladd = barnkladd.barnkladd:main',
            ]
        },
)
