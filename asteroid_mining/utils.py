import numpy as np
import pandas as pd

def clean_spec(x):
    """Returns a string cleant"""
    x = str(x).replace(':', '')
    x = str(x).replace('(IV)', '')
    return x

