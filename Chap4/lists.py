spam = ['cat','bat','rat','elephant']
print(spam[0])
print(spam[2])
print('Hello lovely, ' + spam[0] + ' the one who ate the ' + spam[2])
spam = [['cat','rat'],[1,2,3,4,5]]
print(spam[0])
print(spam[0][1])
print(spam[1][3])
spam = ['cat','bat','rat','elephant']
print(spam[-2])
print(spam[0:4])
print(spam[0:-1])
print(spam[:2])
print(spam[:])
print(len(spam))
spam[2] = 'aardvark'
print(spam)
print([1,2,3]+['X','Y','Z'])
print(spam + ['X','Y','Z'])
del spam[2]
print(spam)