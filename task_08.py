#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Dictionary Comprehensions."""

import data
from data import FRUIT


shoplist = {'White Peach': 4, 'Asian Pear': 24, 'Navel Orange': 6}

def get_cost_per_item(dictionary):
    """DOCSTRING"""
    fruit_cost = {price for name, price in data.FRUIT.iteritems()}
    item_cost = {v * price for k,v in shoplist.iteritems()
                 if k in data.FRUIT.keys()}
    return item_cost

def get_total_cost(dictionary):
    """DOCSTRING"""
    sum(get_total_cost(shoplist))
