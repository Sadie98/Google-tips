import random


def run(numbers, first, last):
    if first > last:
        return  # потому что хотим найти середину, они не должны наслоиться

    i, j = first, last
    pivot = numbers[random.randint(first, last)]  # точка опоры - случайный элемент

    while i <= j:
        while numbers[i] < pivot:
            i += 1  # хотим найти первый элемент слева, который не отсортирован, т.е. больше опорного
        while numbers[j] > pivot:
            j -= 1  # аналогично, хотим найти тот элемент, меньше опорного

        if i <= j:  # если ещё не вышли за границу
            numbers[i], numbers[j] = numbers[j], numbers[i]  # меняем элементы их местами
            i, j = i + 1, j - 1  # двигаем дальше
        run(numbers, first, j)
        run(numbers, i, last)


if __name__ == "__main__":
    nums = [2, 5, 12, 32, 64]
    run(nums, 0, len(nums) - 1)
    print(nums)
