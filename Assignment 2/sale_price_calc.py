# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input('Enter Cost Price :'))
discount = int(input('Enter Discount (in %) :'))
discount_amt = cost_price * (discount/100)
selling_price = cost_price - discount_amt
print(f'Selling Price is {selling_price} rs.')

