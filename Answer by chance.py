import random as r
abcd=["a","b","c","d"]
da=r.choice("abcd")
print(da)
while True:
    enter=input("回车以继续")
    da=r.choice("abcd")
    print(da)
