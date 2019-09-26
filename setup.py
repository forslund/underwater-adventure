# Copyright (c) 2019 Åke Forslund
#
# This file is part of Mycroft Skills Manager
# (see https://github.com/MatthewScholefield/mycroft-light).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from setuptools import setup

setup(
    name='underwater-adventure',
    version='0.8.3',
    packages=['underwater_adventure'],
    install_requires=[],
    url='https://github.com/forslund/underwater-adventure',
    license='Apache-2.0',
    author='forslund',
    author_email='ake.forslund@gmail.com',
    description='A short underwater adventure',
    entry_points={
        'console_scripts': {
            ('underwater-adventure=underwater_adventure.adventure:'
             'simple_game_loop')
        }
    },
    #data_files=[('underwater-adventure')]
)
