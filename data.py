#!/usr/bin/env python3

import loggers


class Data:
    pass


cli = loggers.Stream()
cli.info(f"Logger initialised in {__name__} module.")
gui = loggers.Stream()
cli.info(f"Logger initialised in {__name__} module.")
