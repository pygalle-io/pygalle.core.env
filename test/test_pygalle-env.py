#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---
This file is part of pygalle.core.env
Copyright (c) 2018 SAS 9 Février.
Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).
---
"""

import unittest
import inspect
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join('..','src')))

from pygalle.core.env import PygalleEnv


class PygalleEnvTest(unittest.TestCase):
    """ Unit tests for PygalleEnvTest.
    """

    def test_isclass(self):
        """ Is {PygalleEnv} really a class ? """
        self.assertEqual(inspect.isclass(PygalleEnv), True)

    def test_create_instance(self):
        """ Create a new instance of {PygalleEnv} """
        self.assertIsInstance(PygalleEnv(), PygalleEnv)

def main():
    """ Entry point.
    """
    unittest.main()

if __name__ == '__main__':
    main()

