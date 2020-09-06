#!/usr/bin/env python

import argparse

class ExtendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        """
        Concatenate each list of arguments into a single, flat, list.
        """
        items = getattr(namespace, self.dest) or []
        items.extend(values)
        setattr(namespace, self.dest, items)
