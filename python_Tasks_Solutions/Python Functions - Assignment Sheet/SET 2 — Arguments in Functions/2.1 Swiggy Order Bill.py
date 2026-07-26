#Write place_order(customer, *items, **charges).
#place_order("Ravi", "Biryani", "Coke", "Gulab Jamun",delivery=40, gst=25, discount=50)
# Output:
# Customer : Ravi
# Items ordered (3):
#   1. Biryani
#   2. Coke
#   3. Gulab Jamun
# Charges:
#   delivery : 40
#   gst      : 25
#   discount : 50
def place_order(customer,*items,**charges):
    print('Customer :',customer)
    print(f"Items Ordered({len(items)}):")
    for i in range(len(items)):
        print(f" {i+1}. {items[i]}")
    print('Charges:')
    for k,v in charges.items():
        print(f" {k:<8} : {v}")
place_order('Ravi','Biryani','Coke','Gulab Jamun',delivery=40,gst=25,discount=50)
