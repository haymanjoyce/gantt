#!/usr/bin/env python3

import loggers
import utils


def dimension_field(*args):
    if len(args[2]) > 5:
        return False
    elif args[2].isdigit():
        return True
    elif args[2] == "":
        return True
    else:
        return False


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))
