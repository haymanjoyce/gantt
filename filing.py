#!/usr/bin/env python3

import logging
import json
import sys
import os


LOG_FILE = "app.log"
CONFIG_FILE = "config.json"


def get_path(filename):
    """Provides path to app if bundled into one .exe file."""
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'


def get_config_data():
    try:
        file = open(get_path(CONFIG_FILE), "r")
        data = file.readline()
        if data:
            return json.loads(data)
        else:
            return dict()
    except FileNotFoundError:
        logging.debug("Configuration file not found.")
        file = open(get_path(CONFIG_FILE), "w")
        file.close()
        logging.debug("Configuration file created.")
        return dict()


def save_config_data(data):
    with open(get_path(CONFIG_FILE), "w") as file:
        file.write(json.dumps(data))
    # logging.debug("Configuration data saved.")


def wipe_config_file():
    with open(get_path(CONFIG_FILE), "w") as file:
        file.truncate(0)
    logging.debug("Configuration file wiped.")


def get_log():
    with open(get_path(LOG_FILE), "r") as log_file:
        log = str(log_file.read())
    return log


def wipe_log():
    with open(get_path(LOG_FILE), "r+") as file:
        file.truncate(0)  # erase log file


def append_log(text):
    with open(get_path(LOG_FILE), "a") as file:
        file.write(text)
