from trie import Trie
from typing import List


class LongestCommonWord(Trie):
    """
    Клас для знаходження найдовшого спільного префікса серед набору слів.
    """
    def find_longest_common_word(self, strings: List[str]) -> str:
        """
        Знаходить найдовший спільний префікс серед всіх слів у списку.
        """
        if not strings:
            return ""

        for word in strings:
            self.insert(word)

        prefix = ""
        node = self.root
        while node:
            # Якщо вузол має рівно одного нащадка і це не кінець слова, продовжуємо будувати префікс
            if len(node.children) == 1 and not node.is_end_of_word:
                char = next(iter(node.children))  # Отримуємо єдиного нащадка
                prefix += char
                node = node.children[char]
            else:
                break

        return prefix


if __name__ == "__main__":
    # Тести
    try:
        trie = LongestCommonWord()
        strings = ["flower", "flow", "flight"]
        assert trie.find_longest_common_word(strings) == "fl"

        trie = LongestCommonWord()
        strings = ["interspecies", "interstellar", "interstate"]
        assert trie.find_longest_common_word(strings) == "inters"

        trie = LongestCommonWord()
        strings = ["dog", "racecar", "car"]
        assert trie.find_longest_common_word(strings) == ""

        print("All tests are successful")
        
    except AssertionError as e:
        print("Some tests failed!")
    
