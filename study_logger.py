#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   study_logger.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   12.10.2014
# =============================================================================
"""Functions and classes for logging study sessions."""

__all__ = ['StudyDB', 'load_database']

#############
#  Imports  #
#############
import os
import datetime as dt

import picklefile as PF

################
#  File names  #
################
CATEGORY_FILE = 'categories.dat'

####################
#  Database class  #
####################


class StudyDB(object):
    """Container for study logs."""
    def __init__(self, categories):
        self._logs = []
        self._categories = [cat.lower() for cat in categories]

    def __iter__(self):
        return iter(self._logs)

    @staticmethod
    def load(file_name):
        """Load DB from file.

        :param file_name: File to load from.
        :type file_name: str

        :returns: Database.
        :rtype: StudyDB

        :raises: OSError: If file_name doesn't exist
        :raises: TypeError: If the pickle file is not of type StudyDB

        """
        if not os.path.exists(file_name):
            raise OSError("Cannot find StudyDB file -> %s" % file_name)
        db_obj = PF.load(file_name)
        if not isinstance(db_obj, StudyDB):
            raise TypeError("Loaded object is not StudyDB!")
        return db_obj

    def save(self, file_name):
        """Save DB to disk.

        :param file_name: File to save to.
        :type file_name: str

        """
        PF.write(self, file_name)

    def get_categories(self):
        """Get list of allowed categories.

        :rtype: list

        """
        return self._categories

    def add_category(self, category):
        """Add category to list of allowed categories.

        The category will be converted to lower case.

        :param category: Category to add.
        :type category: str

        :returns: True if added, False if already present.
        :rtype: bool

        """
        category = category.lower()
        if category in self._categories:
            return False
        else:
            self._categories.append(category)
            return True

    def add_entry(self, duration, category, date):
        """Add entry to log.

        :param duration: Duration of entry (in hours).
        :type duration: float
        :param category: Category of study entry.
        :type category: str
        :param date: Date of study.
        :type date: datetime.date

        :raises: ValueError: If category is unknown.
        :raises: TypeError: If date is not datetime.date.

        """
        if not category.lower() in self._categories:
            raise ValueError("Unknown category -> %s" % category)
        if not isinstance(date, dt.date):
            raise TypeError("date object needs to be datetime.date")
        self._logs.append((duration, category, date))


##############
#  Shortcut  #
##############

load_database = StudyDB.load


# EOF
