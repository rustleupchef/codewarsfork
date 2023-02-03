q = int(input())

for i in range(q):
    tr = (float(input()) / 100)
    price = float(input())
    ptax = price / (1.0 + tr)
    tax_amount = round(ptax * tr, 2)
   
    
    print("On your $" + str(price) + 
          " purchase, the tax amount was $" + tax_amount)
    



        