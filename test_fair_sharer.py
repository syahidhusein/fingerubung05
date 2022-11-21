# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:12:54 2022

@author: ASUS
"""

from fair_sharer import fair_sharer

def test_fair_sharer():
    test_list = [0, 1000, 800, 0]
    num_iter = 2
    fair_sharer(test_list,num_iter)
    assert max(test_list) == 890
