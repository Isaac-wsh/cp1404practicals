num_item = int(input("Number of items: "))
while num_item < 0:
    print("Invalid number of items!")
    num_item = int(input("Number of items: "))

total = 0
for i in range(num_item):
    price_item = float(input("Price of item: "))
    total = total + price_item

if total >100:
    total = total * 0.9
print(f"Total price for {num_item} items is ${total:.2f}")