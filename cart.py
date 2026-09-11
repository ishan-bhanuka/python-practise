cart = []

while True:
    goods = input("Enter the type of good you want to buy: ")
    
    # යූසර් 'done' ගැහුවොත් එසැණින් ලූප් එකෙන් එළියට පනින්න (append වෙන්න කලින්)
    if goods == 'done':
        break
        
    cart.append(goods)

print('Your shopping cart - ', end='')
for i in cart:
    print(i, end=', ')