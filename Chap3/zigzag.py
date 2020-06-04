import time,sys
indent = 0
indentIncreasing = True
try:
    while True:
        i=0
        while i <= indent:
            print('a', end='')
            i = i+1
        print('********')
        time.sleep(0.1)
    if indentIncreasing:
        indent = indent + 1
        if indent == 20:
            indentIncreasing = False
    else:
        indent = indent-1
        if indent == 0:
            indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()