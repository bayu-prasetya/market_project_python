# === Aplikasi Market ===

# Detail produck
# Price
apple_price = 10_000
orange_price = 15_000
grape_price = 20_000
# Stock
apple_stock = 10
orange_stock = 10
grape_stock = 10

# Input user
print("==== Fruits Market ====")

# Apple input with stock validation
while True:
    apple_qty = input("Masukan Jumlah Apel: ")
    apple_qty = int(apple_qty)
    if apple_stock >= apple_qty:
        break
    print("Jumlah yang dimasukan terlalu banyak. Stok tinggal: ", apple_stock)

# Orange input with stock validation
while True:
    orange_qty = input("Masukan Jumlah Jeruk: ")
    orange_qty = int(orange_qty)
    if orange_stock >= orange_qty:
        break
    print("Jumlah yang dimasukan terlalu banyak. Stok tinggal: ", orange_stock)

# Grape input with stock validation
while True:
    grape_qty = input("Masukan Jumlah Anggur: ")
    grape_qty = int(grape_qty)
    if grape_stock >= grape_qty:
        break
    print("Jumlah yang dimasukan terlalu banyak. Stok tinggal: ", grape_stock)

apple_total_price = apple_qty * apple_price
orange_total_price = orange_qty * orange_price
grape_total_price = grape_qty * grape_price

print("Total Belanja")

print(f"Apel    : {apple_qty} x {apple_price} = {apple_total_price}")
print(f"Jeruk   : {orange_qty} x {orange_price} = {orange_total_price}")
print(f"Anggur  : {grape_qty} x {grape_price} = {grape_total_price}")
total_price = apple_total_price + orange_total_price + grape_total_price

print(f"Total belanja: {total_price}")

while True:
    input_money = input("Masukan jumlah uang: ")
    input_money = int(input_money)

    if input_money > total_price:
        print("Uang kembalian: ", input_money-total_price)
        print("Terimakasih")
        break
    elif input_money < total_price:
        print("Uang kurang sebesar: ", total_price-input_money)
    else:
        print("Uang pas tidak ada kembalian")
        print("Terimakasih")
        break