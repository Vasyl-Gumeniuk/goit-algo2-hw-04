from typing import Dict, List, Optional, Callable
import functools

class TrieNode:
    """
    Вузол для префіксного дерева (Trie).
    """
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.value: Optional[str] = None
        self.is_end_of_word: bool = False


def validate_key(func: Callable) -> Callable:
    """
    Декоратор для перевірки коректності вхідного ключа.
    """
    @functools.wraps(func)
    def wrapper(self, key: str, *args, **kwargs):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument: key = {key} must be a non-empty string")
        return func(self, key, *args, **kwargs)
    return wrapper


class Trie:
    """
    Реалізація префіксного дерева (Trie).
    """
    def __init__(self):
        self.root: TrieNode = TrieNode()
        self.size: int = 0

    @validate_key
    def put(self, key: str, value: Optional[str] = None) -> None:
        """
        Додає ключ-значення в Trie.
        """
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    @validate_key
    def get(self, key: str) -> Optional[str]:
        """
        Повертає значення за ключем або None, якщо ключа немає в Trie.
        """
        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    @validate_key
    def delete(self, key: str) -> bool:
        """
        Видаляє ключ із Trie. Повертає True, якщо ключ видалено, False - якщо ключа не існує.
        """
        def _delete(node: TrieNode, key: str, depth: int) -> bool:
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    return len(node.children) == 0
                return False

            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, key, 0)

    def is_empty(self) -> bool:
        """
        Перевіряє, чи Trie порожній.
        """
        return self.size == 0

    @validate_key
    def longest_prefix_of(self, s: str) -> str:
        """
        Знаходить найдовший префікс серед ключів у Trie, що збігається з вхідним рядком.
        """
        current = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

    @validate_key
    def keys_with_prefix(self, prefix: str) -> List[str]:
        """
        Повертає список усіх ключів, що починаються із заданого префікса.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result: List[str] = []
        self._collect(current, list(prefix), result)
        return result

    def _collect(self, node: TrieNode, path: List[str], result: List[str]) -> None:
        """
        Рекурсивно збирає всі ключі з Trie.
        """
        if node.value is not None:
            result.append("".join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys(self) -> List[str]:
        """
        Повертає список усіх ключів у Trie.
        """
        result: List[str] = []
        self._collect(self.root, [], result)
        return result

    @validate_key
    def insert(self, word: str) -> None:
        """
        Вставляє слово в Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
