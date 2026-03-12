subtotal = 0.00

for i in range(1,4):
 print(f"Item {i}")
 while True:
  price = float(input(f"Enter price for item {i}: "))
  quantity = int(input(f"Enter quantity for item {i}: "))
  break 
   except ValueError:
    print("Invalid input! Please enter numbers only (e.g., 50 or 10.5).")
    item_total = price * quantity
    subtotal += item_total

discount = subtotal * 0.10 if subtotal > 1000 else 0.0
final_total = subtotal - discount

print(f"\nSubtotal: {subtotal:,.2f}")
print(f"Discount: {discount:,.2f}")
print(f"Final Total: {final_total:,.2f} pesos")

