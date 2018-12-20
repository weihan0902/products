# 記帳程式
# 二維度清單:清單中還有清單
products = []
# 讀取檔案
# 增加讀取檔案程式碼
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
	# 怎麼跳過商品名稱?
		if '商品,價格' in line:
			continue # continue跟break依樣只能寫在迴圈裡面，continue就是跳到下一迴的意思
		# 用 .spilt(',')來用逗點做分割
		# 用 .strip()來除掉換行符號(\n)
		name, price = line.strip().split(',')
		# name = [0]
		# price = [1]
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	# 第10,11,12行可以寫成 p = [name, price]
	products.append(p)
	# 第10,11,12,14行可以寫成 products.append([name, price])
print(products)

# 練習存取二維清單
products[0][0]

#印出所有的購買紀錄
# for loop搞清楚每個東西是什麼
for p in products:
	print(p[0], '的價格是', p[1], '元')
# 字串可以做 + 跟 *
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

# 寫入檔案
# 寫到檔案的程式碼 # 改成csv格式
with open('products.csv', 'w', encoding='utf-8') as f: # 此行只有打開 # with功能:自動close
	f.write('商品,價格\n') # 加入程式碼來寫欄位 # 寫入跟讀取都牽扯到編碼
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n' ) # 此行才是真正的寫入(f.write)
		# 通常都會跟\n做合併 # str = string 轉換成字串
# excel導入csv資料:
# 資料->取得外部資料->從文字檔
# 編碼: 選utf-8
# 分隔符號:選逗號