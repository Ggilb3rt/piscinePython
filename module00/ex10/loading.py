import sys
import time


def ft_progress(lst: list):
    max_lst = max(lst)
    start_time = time.perf_counter()
    for i in lst:
        pourcent = round(i * 100 / max_lst)
        print(
            f'ETA: {time.perf_counter() - start_time:.2f}s '
            f'[{pourcent:3d}%]'
            f'[{("="*round(pourcent / 5) + ">"):21}] '
            f'{i}/{max_lst} | '
            f'elapsed time ??s'
            , end="\r"
        )
        yield i


if __name__ == "__main__":
    # listy = range(3334)
    # ret = 0
    # for el in ft_progress(listy):
    #     ret += el
    #     time.sleep(0.005)
    # print()
    # print(ret)
    listy = range(1001)
    ret = 0
    for el in ft_progress(listy):
        ret += (el + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
