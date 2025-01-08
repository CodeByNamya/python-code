buy=int(input("buy value="))
sell=int(input("sell value="))
if buy==sell:
    print("breakeven")
elif buy<sell:
    print('profit')
else:
    print("loss")