def chain_loop(args):
    it = list()
    for i in args:
        it.append(iter(i))
    while it:
        arr = list()
        for i in it:
            try:
                yield next(i)
                arr.append(i)
            except StopIteration:
                pass
        it = arr
