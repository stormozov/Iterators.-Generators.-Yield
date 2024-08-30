class FlatIterator:
    """Iterator for nested lists"""
    def __init__(self, list_of_list: list[list]) -> None:
        """Constructor for FlatIterator class.

        Args:
            list_of_list (list[list]): A list of lists.

        Attributes:
            list_of_list (list[list]): A list of lists.
            outer_cursor (int): The current position in the outer list.
            inner_cursor (int): The current position in the inner list.
        """
        self.list_of_list = list_of_list
        self.outer_cursor = 0
        self.inner_cursor = 0

    def __iter__(self) -> 'FlatIterator':
        """Returns the iterator object itself.

        This is required to allow the class to be used as an iterator.

        Returns:
            FlatIterator: The iterator object itself.
        """
        return self

    def __next__(self) -> object:
        """Gets the next item from nested lists.

        Returns:
            object: The next item from nested lists.
        Raises:
            StopIteration: When there are no more items in nested lists.
        """
        if self.outer_cursor >= len(self.list_of_list):
            raise StopIteration

        inner_list = self.list_of_list[self.outer_cursor]
        if self.inner_cursor >= len(inner_list):
            self.outer_cursor += 1
            self.inner_cursor = 0
            return self.__next__()

        item = inner_list[self.inner_cursor]
        self.inner_cursor += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert (
        list(FlatIterator(list_of_lists_1))
        == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    )


if __name__ == '__main__':
    test_1()
