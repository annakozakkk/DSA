import unittest
from src.trie import Trie, build_trie


class MyTestCase(unittest.TestCase):

    def test_searching_in_trie_if_word_is_in_trie(self):
        patterns = ["red", "redirect", "redux", "container", "consist", "command"]
        trie = build_trie(patterns)
        result = trie.search('red')

        self.assertEqual(True, result)

    def test_searching_in_trie_if_word_is_not_in_trie(self):
        patterns = ["red", "redirect", "redux", "container", "consist", "command"]
        trie = build_trie(patterns)
        result = trie.search('rad')

        self.assertEqual(False, result)

    def test_finding_prefix_if_exists(self):
        patterns = ["red", "redirect", "redux", "container", "consist", "command"]
        trie = build_trie(patterns)
        result = trie.find_prefix('red')
        self.assertEqual(True, result)

    def test_finding_prefix_if_not_exists(self):
        patterns = ["red", "redirect", "redux", "container", "consist", "command"]
        trie = build_trie(patterns)
        result = trie.find_prefix('can')
        self.assertEqual(False, result)
