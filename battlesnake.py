#! /usr/bin/env python3

import bottle
import logging


@bottle.get('/')
def info():
    return {
        "apiversion": "1",
        "author": "johdicks",
        "color": "#1B1B1B",
        "head": "default",
        "tail": "default",
    }


if __name__ == '__main__':
    bottle.run()
