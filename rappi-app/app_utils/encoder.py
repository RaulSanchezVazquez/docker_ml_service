#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Raul Sanchez-Vazquez
"""
import os
import json


from app_utils import config


# Path were to store the encoder
ENCODER_PATH = os.path.join(
    config.ARTIFACTS_PATH,
    'encoder.json')

# Aux. variable used to load once the object
_categ_enc = None


def save(categ_enc):
    """Save the encoder object.

    Parameters
    -----------
    categ_enc: dict
        Dictionary containing feature names of categorical features than a map
        of string and values.
    """

    with open(ENCODER_PATH, 'w') as f:
        f.write(json.dumps(categ_enc))


def get():
    """Fetch the encoder object.

    Returns
    --------
    categ_enc: dict
        Dictionary containing feature names of categorical features than a map
        of string and values.
    """

    with open(ENCODER_PATH, 'r') as f:
        categ_enc = json.loads(f.read())

    return categ_enc


def load():
    """Load the encoder object in to memory.

    This is done once regardless of how many times this method is invoqued.
    """
    global _categ_enc

    if _categ_enc is None:
        _categ_enc = get()
