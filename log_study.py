#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   log_study.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   12.10.2014
# =============================================================================
"""Log a study session."""

from argparse import ArgumentParser
import datetime as dt

from study_logger import load_database

DB_NAME = 'quant_db.db'


def parse_date(date_str):
    """Parse date string.

    :param date_str: String representing the date.
    :type date_str: str

    :returns: datetime.date

    :raises: ValueError: If string is not a valid date.

    """
    delimiters = ['-', '.', '/']
    for delimiter in delimiters:
        if delimiter in date_str:
            date_tuple = [int(element) for element in date_str.split(delimiter)][::-1]
            if len(date_tuple) != 3:
                raise ValueError("Cannot parse date string")
            return dt.date(*date_tuple)
    raise ValueError("Cannot parse date")

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--db', action='store', type=str, default=DB_NAME, help="Database file to use")
    parser.add_argument('--date', action='store', type=str, help="Date of study")
    parser.add_argument('-c', '--cat', action='store', type=str, help="Category of study")
    parser.add_argument('hours', action='store', type=float, help="Hours of study")
    args = parser.parse_args()
    # Now let's do things
    if not args.date:
        date = dt.date.today()
    else:
        date = parse_date(args.date)
    # Load DB
    database = load_database(args.db)
    database.add_entry(args.hours, args.cat, date)

# EOF
