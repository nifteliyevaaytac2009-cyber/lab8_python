def add_vat(price, vat_percent=18):
    return price + (price * vat_percent / 100)
print(add_vat(100))                    
print(add_vat(50, 10))                  
print(add_vat(vat_percent=5, price=80))
