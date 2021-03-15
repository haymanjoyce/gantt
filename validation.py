#!/usr/bin/env python3

import loggers
import utils


def test(entry):
    if entry == entry:
        return True


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))
