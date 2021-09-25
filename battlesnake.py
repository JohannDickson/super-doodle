#! /usr/bin/env python3

import bottle
import logging


logformat = "%(levelname)s - %(message)s"
formatter = logging.Formatter(logformat)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)


@bottle.get('/')
def info():
    return {
        "apiversion": "1",
        "author": "johdicks",
        "color": "#1B1B1B",
        "head": "default",
        "tail": "default",
    }


@bottle.post('/start')
def start():
    log.info('Starting round')


@bottle.post('/move')
def move():
    log.debug('Move')


@bottle.post('/end')
def end():
    log.info('End round')


if __name__ == '__main__':
    bottle.run(
        host="0.0.0.0",
        reloader=True,
    )
