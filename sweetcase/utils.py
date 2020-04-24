def length(value):
    try:
        return len(value)
    except TypeError:
        return 0
