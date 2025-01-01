x = 5
if (type(x) is int):
    print ('True')
else:
    print ('False')
x = 5.0
if (type(x) is not float):
    print ('True')
else:
    print ('False')
x = 20
y = 20
if (x is y):
    print ('Variable x and variable y are the same.')
else:
    print ('Variable x and variable y are different.')
y = 30
if (x is not y):
    print ('Variable x and variable y are different.')
else:
    print ('Variable x and variable y are the same.')

    