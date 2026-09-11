def calculate_final_price(price,discount=10):
    discount_amount=price*discount*0.01
    final_price=price-discount_amount
    return discount_amount,final_price
da,fp=calculate_final_price(1000,discount=10)
print(da,fp)

da,fp=calculate_final_price(1000,20)
print(da,fp)