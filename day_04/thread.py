#solution from: https://old.reddit.com/r/adventofcode/comments/3vdn8a/day_4_solutions/cxmucxi/
from hashlib import md5
from sys import argv
import multiprocessing


def day_4(key, zeroes):
    num = 0
    target = "00000000000000000000000000000000"[:zeroes]

    while not (md5((key + str(num)).encode()).hexdigest()[:zeroes] == target):
        num += 1
    return {"num": num, "hash": md5((key + str(num)).encode()).hexdigest()}


def worker(key, start, step, zeroes, target, result):
    while not (md5(key + str(start)).hexdigest()[:zeroes] == target):
        start += step
    result.put({"num": start, "hash": md5((key + str(start)).encode()).hexdigest()})


def day_4mt(key, zeroes):
    target = "00000000000000000000000000000000"[:zeroes]

    out = multiprocessing.Queue()
    step = multiprocessing.cpu_count()
    threads = []

    for i in range(0, step - 1):
        threads.append(multiprocessing.Process(target=worker, args=(key, i, step, zeroes, target, out)))
    for t in threads:
        t.start()

    result = out.get()

    # kill everything still churning
    for t in threads:
        t.terminate()
    return result


if len(argv) > 1:
    key, zeroes = argv[1], int(argv[2])
    if zeroes > 32:
        print("too many zeroes!")
    elif zeroes < 6:
        print(day_4(key, zeroes))
    else:
        print(day_4mt(key, zeroes))
else:
    print("ckczppom, 5:\t" + str(day_4("ckczppom", 5)))
    print("ckczppom, 6:\t" + str(day_4("ckczppom", 6)))
