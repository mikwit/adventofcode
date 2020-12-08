def load_txt(filename, sep=None):
    if sep is None:
        sep = '\n'
    with open(filename, 'r') as f:
        results = f.read().split(sep)

    for element in results:
        if len(element) == 0:
            results.remove(element)

    return results