import json
import logging
from random import choice

log = logging.getLogger(__name__)

def info():
    return {
        "apiversion": "1",
        "author": "johdicks",
        "color": "#1B1B1B",
        "head": "default",
        "tail": "default",
    }


def move(r):
    h = r['board']['height']
    w = r['board']['width']
    s = r['you']

    moves = [
        "up",
        "down",
        "left",
        "right"
    ]

    moves = avoid_edges(s, moves, h, w)
    moves = avoid_self(s, moves)

    log.debug(moves)
    nextMove = choice(moves)
    log.debug(nextMove)
    return nextMove


def avoid_self(s, moves):
    head = s['head']

    for body in s['body']:
        if 'left' in moves and body['y'] == head['y'] and body['x'] == head['x']-1:
            moves.remove('left')

        if 'right' in moves and body['y'] == head['y'] and body['x'] == head['x']+1:
            moves.remove('right')

        if 'down' in moves and body['x'] == head['x'] and body['y'] == head['y']-1:
            moves.remove('down')

        if 'up' in moves and body['x'] == head['x'] and body['y'] == head['y']+1:
            moves.remove('up')

    return moves


def avoid_edges(s, moves, w, h):
    head = s['head']

    if head['x'] == 0:
        log.debug("AT LEFT EDGE")
        moves.remove('left')

    if head['x'] == (w-1):
        log.debug("AT RIGHT EDGE")
        moves.remove('right')

    if head['y'] == 0:
        log.debug("AT BOTTOM EDGE")
        moves.remove('down')

    if head['y'] == (h-1):
        log.debug("AT TOP EDGE")
        moves.remove('up')

    return moves
