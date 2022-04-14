# a = int(input("enter first number"))
# b = int(input("enter second number"))
#
# from fibo import check_lower
#
# for i in range(5, 11):
#     check_lower(a, i)

a = [{"name": "asaf", "number": [1, 2, 3]}, {"name": "aviran", "number": [2, 5, 3]},
     {"name": "adi", "number": [10, 2, 14]}]

for p in a:
    for i in p["number"]:
        if i > 10:
            print(p["name"])
