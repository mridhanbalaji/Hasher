import random
from re import S
# selectorder = []
# for i in range(5):
#     order = input("PLace your order:")
#     selectorder.append(order)
# Order = random.choice(selectorder)
# print("Your order is:" + Order)

vals = [7,8,1,4,11,5,24]

def findnumber(vals):

    vals.sort()

    a = vals[0]
    b = vals[1]
    last = vals[-1]

    sums_ab = a + b

    c = last - sums_ab

    return a, b, c


findnumber(vals)






