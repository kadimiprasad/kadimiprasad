list= []

def Ratios(vect1, vect2):

  for i in range(0, len(vect1)):
    list.append(vect1[i] / vect2[i])
  return list
try:
    print(Ratios([5,6,7], [4,5,6]))
except:
    print("exception find")
else:
    print("proper running")
finally:
    print("final")
