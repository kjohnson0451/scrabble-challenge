# -*- coding: utf-8 -*-

from .context import scrabble_challenge

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_hmm(self):
        self.assertEqual(scrabble_challenge.get_hmm(), 'hmmm...')


if __name__ == '__main__':
    unittest.main()
