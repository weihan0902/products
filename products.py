# 記帳程式
# 二維度清單:清單中還有清單

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	# 第10,11,12行可以寫成 p = [name, price]
	products.append(p)
	# 第10,11,12,14行可以寫成 products.append([name, price])
print(products)

# 練習存取二維清單
products[0][0]