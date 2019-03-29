def max_odd(x, y, z):
 odd_nums = []
 if x % 2 == 1:
  odd_nums.append(x)
 if y % 2 == 1:
  odd_nums.append(y)
 if z % 2 == 1:
  odd_nums.append(z)
 if odd_nums == []:
  return "No odd numbers"
 else:
  return max(odd_nums)
print(max_odd(11,22,33))