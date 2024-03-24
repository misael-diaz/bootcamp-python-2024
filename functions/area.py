#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Bootcamp 2024                    March 23, 2024

source: area.py
author: @misael-diaz

Copyright (c) 2024 Misael Díaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

def area(radius):
    from numpy import pi
    area = pi * radius * radius
    return area

sword_length = 1
spear_length = 2

sword_attack_area = area(sword_length)
spear_attack_area = area(spear_length)

print(f"Sword length [m]: {sword_length}")
print(f"Sword attack area [m^2]: {sword_attack_area:.2f}")

print(f"Spear length [m]: {spear_length}")
print(f"Spear attack area [m^2]: {spear_attack_area:.2f}")
