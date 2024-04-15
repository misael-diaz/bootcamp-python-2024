#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Bootcamp 2024                    April 15, 2024

source: unit-testing/magic-damage/main.py
author: @misael-diaz

Copyright (c) 2024 Misael Díaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

def take_magic_damage(health, resist, amp, spell_power):
    max_damage = amp * spell_power
    total_damage = max_damage - resist
    return max(0, health - total_damage)
