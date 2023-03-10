# https://www.codewars.com/kata/5629db57620258aa9d000014

def mix(s1, s2):
    hist = {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        s1_count, s2_count = s1.count(i), s2.count(i)
        if max(s1_count, s2_count) > 1:
            max_count = "1" if s1_count > s2_count else "2" if s2_count > s1_count else "="
            hist[i] = (-max(s1_count, s2_count), max_count + ":" + i * max(s1_count, s2_count))
    return "/".join(hist[i][1] for i in sorted(hist, key=lambda x: hist[x]))