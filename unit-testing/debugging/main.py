#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Bootcamp 2024                    April 15, 2024

source: unit-testing/debugging/main.py
author: @misael-diaz

Copyright (c) 2024 Misael Díaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

def unlock_achievement(before_xp, achievement_xp, achievement_name):
    xp = before_xp + achievement_xp
    msg = f"Achievement Unlocked: {achievement_name}"
    return xp, msg
