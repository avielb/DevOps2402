# my_range = list(range(5))
# print(my_range)
#
# for i in range(-9, 5, 2):
#     print(i)

names = ["yekutiel", "ginat", "adi", "elisaf", "ariel"]
for name in names:
    if name == "elisaf":
        continue
    print(name)
    if name == "adi":
        print("I've found adi, exiting...")
        break
else:
    print("loop finished successfully")

a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("done")

for i in range(5):
    print(i)
else:
    print("done")

if "moshe" in names:
    print("moshe is in names")
#
# for i in range(len(names)):
#     print(names[i])
#
# a = 0
# while a < 5:
#     print(a)
#     a = a + 1
a = 4
if a == 0:
    pass
else:
    print("a is not 0")
