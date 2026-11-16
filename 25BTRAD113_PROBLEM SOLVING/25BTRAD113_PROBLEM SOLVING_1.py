# Bill Generator 
customer input ("Enter customer name: ") item1 = input("Enter item 1 name: ") 
qty1= int(input("Enter quantity: ")) 
price1 = float (input("Enter unit price: ")) 
= 
item2 input("Enter item 2 name: ") 
qty2 = int(input("Enter quantity: ")) 
price2 = float (input("Enter unit price: ")) 
totall = qty1 * pricel 
total2 = qty2 * price2 
subtotal = total1 + total2 
gst subtotal * 0.05 
grand_total = subtotal + gst 
print(" 
" + "="*40) 
print(" 
print("="*40) 
RETAIL INVOICE 
") 
print (f"Customer: {customer}") 
print("-"*40) 
print (f"{'Item': <15}{'Qty':<8}{'Price': <8} { 'Total'}") print("-"*40) 
print (f" {item1: <15} {qty1: <8} {price1: <8.2f} {total1:.2f}") print (f" {item2: <15} {qty2:<8} {price2: <8.2f} {total2:.2f}") print("-"*40) 
print (f"Subtotal: {subtotal:.2f}") 
print (f"GST (5%): {gst:.2f}") 
print (f"Grand Total: {grand_total: .2f}") print("="*40)
