cost_price=float(input("Enter the cost Price of an Item :"))
selling_price=float(input("Enter the Selling Price of an Item :"))
if (selling_price > cost_price):
	profit = selling_price - cost_price
	print("Profit :",profit)
elif( cost_price > selling_price):
	loss = cost_price - selling_price
	print("Loss :",loss)
else:
	print("No Profit No Loss")90
 900