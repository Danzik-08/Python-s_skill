def brackets(n):
    cnt_open = 0
    cnt_close = 0
    arr = list()

    def generate(cnt_open, cnt_close, arr, n):
        if cnt_open + cnt_close < 2 * n:
            if cnt_open < n:
                arr.append('(')
                yield from generate(cnt_open + 1, cnt_close, arr, n)
                arr.pop()
            if cnt_open > cnt_close:
                arr.append(')')
                yield from generate(cnt_open, cnt_close + 1, arr, n)
                arr.pop()
        else:
            yield ''.join(map(str, arr))
    yield from generate(cnt_open, cnt_close, arr, n)


if __name__ == "__main__":
    n = int(input())
    for i in brackets(n):
        print(i)
