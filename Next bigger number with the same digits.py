def next_bigger(n):
    n_lst = list(str(n))
    i, j = len(n_lst) - 1, len(n_lst) - 1

    while i > 0 and n_lst[i - 1] >= n_lst[i]:
        i -= 1

    if i <= 0:
        return -1

    while n_lst[j] <= n_lst[i - 1]:
        j -= 1

    swap(n_lst, i - 1, j)
    j = len(n_lst) - 1
    while i < j:
        swap(n_lst, i, j)
        i += 1
        j -= 1
    return int("".join(c for c in n_lst))

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp