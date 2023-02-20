from random import randint
amount=0
order=input("   What do you want ?   ")
pick=order.split(",") 
for me in pick: 
    cost=randint(42,3000) 
    print(me + "        {}UAH".format(cost))
    amount+=cost
print("total amount      {}UAH".format(amount))