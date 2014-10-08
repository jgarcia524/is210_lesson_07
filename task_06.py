#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 07, Task 06"""


import data

SUPER_SIDEKICKS = {}
for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    SUPER_SIDEKICKS[HERO] = data.SUPERHEROES.get(HERO).get('pet', 'None')
