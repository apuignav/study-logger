#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   picklefile.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   12.10.2014
# =============================================================================
"""Helpers for pickling files."""

import os

import cPickle


def load(file_name):
    """Load file stored as pickle.

    :param file_name: File to load.
    :type file_name: str

    :returns: Loaded pickled object
              or None if file doesn't exist
    :rtype: object or None

    """
    if not os.path.exists(file_name):
        return None
    with open(file_name) as file_:
        decoded = cPickle.load(file_)
    return decoded


def write(obj, file_name):
    """Save object as pickle.

    :param obj: Object to pickle.
    :type obj: object
    :param file_name: File name to save the pickle to.
    :type file_name: str

    """
    with open(file_name, 'w') as file_:
        cPickle.dump(obj, file_)

# EOF
