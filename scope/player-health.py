#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Bootcamp 2024                    April 15, 2024

source: player-health.py
author: @misael-diaz

Copyright (c) 2024 Misael Díaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

def get_max_health(modifier, level):
    return modifier * level

my_modifier = 5
my_level = 10

max_health = get_max_health(my_modifier, my_level)

print(f"max_health is: {max_health}")

