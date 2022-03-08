def counterDict(d, v):
    if v in d:
        d[v] += 1
    else:
        d[v] = 1


def XORSubarray(arr, target):
    solution = 0
    runningXOR = 0
    d = {}
    for i in arr:
        runningXOR ^= i
        if runningXOR ^ target in d:
            solution += d[runningXOR ^ target]
        counterDict(d, runningXOR)
    if target in d:
        solution += d[target]
    return solution


array = [25, 79, 59, 63, 65, 6, 46, 82, 28, 62]
target = 94
print("Solution:", XORSubarray(array, target))
