import types


def flat_generator(list_of_list: list) -> list:
    """Generator that handles lists with any level of nesting.

    Args:
        list_of_list (list): List with nested lists.

    Yields:
        list: A flat list.

    Example:
        >>> list_of_lists_2 = [
        ...     [['a'], ['b', 'c']],
        ...     ['d', 'e', [['f'], 'h'], False],
        ...     [1, 2, None, [[[[['!']]]]], []]
        ... ]
        >>> list(flat_generator(list_of_lists_2))
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    Notes:
        The generator uses recursive calls to handle lists
            with any level of nesting.
    """
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert (
            list(flat_generator(list_of_lists_2))
            == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    )

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
