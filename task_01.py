from trie import Trie
from typing import List


class Homework(Trie):
    """
    Розширений клас Trie, що додає методи для пошуку суфіксів та перевірки префіксів.
    """
    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Підраховує кількість слів, що закінчуються на заданий суфікс.
        """
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")
        
        return sum(1 for key in self.keys() if key.endswith(pattern))

    def has_prefix(self, prefix: str) -> bool:
        """
        Перевіряє, чи є у Trie хоча б одне слово з вказаним префіксом.
        """
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")
        
        return bool(self.keys_with_prefix(prefix))


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    try:
        # Перевірка кількості слів, що закінчуються на заданий суфікс
        assert trie.count_words_with_suffix("e") == 1  # apple
        assert trie.count_words_with_suffix("ion") == 1  # application
        assert trie.count_words_with_suffix("a") == 1  # banana
        assert trie.count_words_with_suffix("at") == 1  # cat

        # Перевірка наявності префікса
        assert trie.has_prefix("app") is True  # apple, application
        assert trie.has_prefix("bat") is False
        assert trie.has_prefix("ban") is True  # banana
        assert trie.has_prefix("ca") is True  # cat
        
        print("All tests are successful")
        
    except AssertionError as e:
        print("Some tests failed!")

