x = [ i for i in range (12, 26)]

x = list(map(lambda x: 10 if x < 18 else(x),x))
print(x)
