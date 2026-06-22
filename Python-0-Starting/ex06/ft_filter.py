def ft_filter(function_to_apply, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """

    if function_to_apply is None:
        # List comprehension when list is None
        result = [item for item in iterable if item]
    else:
        # List comprehension when there is a function
        result = [item for item in iterable if function_to_apply(item)]

    return iter(result)
