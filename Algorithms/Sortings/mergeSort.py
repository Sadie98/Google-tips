import operator


def merge_sort(l, compare=operator.lt):
    if len(l) < 2:
        return l
    else:
        middle = len(l) // 2  # находим серединку
        left = merge_sort(l[:middle], compare)  # сортируем один кусок
        right = merge_sort(l[middle:], compare)  # сортируем второй кусок
        return merge(left, right, compare)  # сливаем куски вместе


def merge(left, right, compare):
    result = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):  # находим меньшее
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


if __name__ == "__main__":
    nums = [2, 5, 235, 1, 12, 32, 64]
    nums = merge_sort(nums)
    print(nums)
