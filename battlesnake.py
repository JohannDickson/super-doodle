#! /usr/bin/env python3

import bottle
import logging

my_snake = 'super_doodle'
snake = __import__(my_snake)
snakelog = logging.getLogger(snake.__name__)


logformat = "%(levelname)s - %(message)s"
formatter = logging.Formatter(logformat)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

snakelog.setLevel(logging.DEBUG)
snakelog.addHandler(ch)


@bottle.get('/')
def info():
    return snake.info()


@bottle.post('/start')
def start():
    log.info('Starting round %s', bottle.request.json['game']['id'])


@bottle.post('/move')
def move():
    log.info('Turn %s', bottle.request.json['turn'])
    nextMove = {
        'move': snake.move(bottle.request.json)
    }
    return nextMove


@bottle.post('/end')
def end():
    log.info('End round %s', bottle.request.json['game']['id'])


if __name__ == '__main__':
    log.info("Running snake %s", my_snake)
    bottle.run(
        host="0.0.0.0",
        reloader=True,
    )
