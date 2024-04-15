#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Bootcamp 2024                    April 15, 2024

source: unit-testing/backtrace/main.py
author: @misael-diaz

Copyright (c) 2024 Misael Díaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = (f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity " +
           f"for a total of {total} stats.")
    return msg
