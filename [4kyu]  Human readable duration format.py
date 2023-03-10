# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    words = ['year', 'day', 'hour', 'minute', 'second']
    time = [seconds // 31536000]
    time.append(seconds % 31536000 // 86400)
    time.append(seconds % 31536000 % 86400 // 3600)
    time.append(seconds % 31536000 % 86400 % 3600 // 60)
    time.append(seconds % 31536000 % 86400 % 3600 % 60)

    duration = []

    for x, i in enumerate(time):
        if i == 1:
            duration.append(f"{i} {words[x]}")
        elif i > 1:
            duration.append(f"{i} {words[x]}s")

    if seconds == 0:
        return 'now'
    elif len(duration) == 1:
        return duration[0]
    elif len(duration) == 2:
        return f"{duration[0]} and {duration[1]}"
    else:
        return ", ".join(duration[:-1]) + " and " + duration[-1]