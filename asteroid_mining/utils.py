import numpy as np
import pandas as pd


def clean_spec(x):
    """Returns a string cleant"""
    x = str(x).replace(':', '')
    x = str(x).replace('(IV)', '')
    return x

def clean_diameter_acc(x):
    items = x.split('-')
    
    items_new = []
    for i in items:
        items_new.append(int(i.strip()))
    
    return sum(items_new) / len(items_new)

