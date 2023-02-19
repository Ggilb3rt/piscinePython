kata = (2019, 9, 25, 3, 30)


def give_interval(nb: int, min: int, max: int) -> int:
    return ((nb - min) % max) + min


if __name__ == "__main__":
    print(
        f'{give_interval(kata[1], 1, 12):02}/'
        f'{give_interval(kata[2], 1, 31):02}/'
        f'{kata[0]} '
        f'{give_interval(kata[3], 0, 12):02}:'
        f'{give_interval(kata[4], 0, 60):02}'
    )
