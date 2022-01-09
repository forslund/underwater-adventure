# Copyright (c) 2019 Åke Forslund
#
# This file is part of Underwater-adventure
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
from setuptools import setup

setup(
    name='underwater-adventure',
    version='0.1.0',
    packages=['underwater_adventure'],
    install_requires=[],
    package_data={'underwater_adventure': ['locale/***']},
    include_package_data=True,
    url='https://github.com/forslund/underwater-adventure',
    license='Apache-2.0',
    author='forslund',
    author_email='ake.forslund@gmail.com',
    description='A short underwater adventure',
    long_description=('A text adventure where you\'re trapped inside a sunken '
                      'ship. Explore the ship and find the tools needed to '
                      'escape.'),
    long_description_content_type='text/x-rst',
    entry_points={
        'console_scripts': {
            ('underwater-adventure=underwater_adventure.__main__:'
             'main')
        }
    }
)
