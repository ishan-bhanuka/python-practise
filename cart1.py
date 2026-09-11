def calculate_total(cart_dict,tax_rate=5):
    sub_total=cart_dict["apple"]+cart_dict["milk"]+cart_dict["bread"]
    tax=sub_total*tax_rate*0.01
    final_total=sub_total+tax
    return sub_total,final_total
cart={"apple":150,"milk":400,"bread":190}
s,f=calculate_total(cart)
print(f"Sub total:Rs.{s},Final total with tax:Rs.{f}")