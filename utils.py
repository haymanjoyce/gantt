#!/usr/bin/env python3

import loggers
import json


def get_settings():
    try:
        file = open("config.json", "r")
        data = file.readline()
        if data:
            return json.loads(data)
        else:
            return dict()
    except FileNotFoundError:
        cli.info("Configuration file not found.")
        file = open("config.json", "w")
        file.close()
        cli.info("Configuration file created.")
        return dict()


def save_settings(data):
    with open('config.json', 'w') as file:
        file.write(json.dumps(data))


def wipe_settings():
    with open('config.json', 'w') as file:
        file.truncate(0)


cli = loggers.Stream()
