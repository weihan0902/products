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

# for loop搞清楚每個東西是什麼
for p in products:
	print(p[0], '的價格是', p[1], '元')

# 字串可以做 + 跟 *
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 寫到檔案的程式碼 # 改成csv格式
with open('products.csv', 'w') as f: # 此行只有打開 # with功能:自動close
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n' ) # 此行才是真正的寫入(f.write)
		# 通常都會跟\n做合併