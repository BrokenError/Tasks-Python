from functools import reduce
def sum_of_intervals(intervals):
    if not intervals:
        return 0
    sum = 0
    intervals.sort(key = lambda e: e[0])
    cursor = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= cursor[1]:
            cursor = (cursor[0], max(cursor[1], intervals[i][1]))
        else:
            sum += cursor[1] - cursor[0]
            cursor = intervals[i]
    sum += cursor[1] - cursor[0]
    return sum