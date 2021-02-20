import random
import time


def scrambler():
    moves = ["L", "L2", "L'",
             "R", "R2", "R'",
             "F", "F2", "F'",
             "B", "B2", "B'",
             "U", "U2", "U'",
             "D", "D2", "D'"]

    cnt = 0
    output = []
    prev = 'ZZ'

    while cnt < 20:
        pos = random.randrange(18)
        if moves[pos][0] != prev[0]:
            output.append(moves[pos])
            prev = moves[pos]
            cnt += 1

    print()
    print('Here is a scrambler for you. Solve Fast!!!')
    print()
    print(' '.join(output))
    print()


def timer():
    e = input('press ENTER to start timer')
    t1 = time.time()
    print()
    print('TIMER STARTED')
    print()
    e = input('press ENTER to stop timer')
    t2 = time.time()
    print()
    print('TIMER STOPPED')
    print()
    m = int(t2 - t1) // 60
    s = int(t2 - t1) % 60
    mm = ''
    ss = ''
    if len(str(m)) == 1:
        mm = '0' + str(m)
    else:
        mm = str(m)

    if len(str(s)) == 1:
        ss = '0' + str(s)
    else:
        ss = str(s)

    print('Solve Time: ' + mm + ':' + ss)
    print()


def start():
