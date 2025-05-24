#day16 - Functions in Python
def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a,b):
  if(a>b):
    print("First number is greater than second no.")
  else:
    print("Second number is greater than first no. or equal")

def isLesser(a, b):
  pass

a = 10
b = 20
calculateGmean(a, b)
isGreater(a,b)

c = 45
d = 23
calculateGmean(c, d)
isGreater(c,d)