class FlatIterator:
    """An iterator that flattens a list of lists into a single list."""
    def __init__(self, list_of_list: list[list]) -> None:
        """Initialize a FlatIterator instance.

        Args:
            list_of_list (list[list]): A list of lists to be iterated over.

        Returns:
            None
        """
        self.list_of_list = list_of_list

    def __iter__(self) -> 'FlatIterator':
        """Return an iterator over the list of lists.

        Returns:
            FlatIterator: An iterator over the list of lists.
        """
        self.stack = [iter(self.list_of_list)]
        return self

    def __next__(self) -> list:
        """Return the next item in the list of lists.

        Returns:
            list: The next item in the list of lists.
        """
        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue
            if isinstance(item, list):
                self.stack.append(iter(item))
            else:
                return item
        raise StopIteration


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert (
        list(FlatIterator(list_of_lists_2))
        == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    )


if __name__ == '__main__':
    test_3()
