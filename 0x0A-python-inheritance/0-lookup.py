#!/usr/bin/python3
"""Defines an object attribute lookup func"""


def lookup(obj):
    """Returns a list of an objects available attributes"""
    return (dir(obj))
