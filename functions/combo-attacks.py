#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Bootcamp 2024                    March 23, 2024

source: combo-attacks.py
author: @misael-diaz

Copyright (c) 2024 Misael Díaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

def calculate_damage(opening_attack, core_damage, finishing_move):
    total = (opening_attack + core_damage + finishing_move)
    return total

dmg_one = 2
dmg_two = 4
dmg_three = 3
dmg_four = 1
dmg_five = 10
dmg_six = 5

print(f"Getting damage for {dmg_one}, {dmg_two}, and {dmg_three} ...")
print(f"{calculate_damage(dmg_one, dmg_two, dmg_three)} points of damage dealt!")
print("=====================================")

print(f"Getting damage for {dmg_four}, {dmg_five}, and {dmg_six} ...")
print(f"{calculate_damage(dmg_four, dmg_five, dmg_six)} points of damage dealt!")
print("=====================================")
