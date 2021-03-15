#!/usr/bin/env python3

import loggers
import utils


def dimension_field(*args):
    if args[2].isdigit():
        return True
    elif args[2] == "":
        return True
    else:
        return False


def date_field(*args):
    return True


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))
