
sum = 0
for d in data:
	sum += len(d)
print('留言平均長度為',sum/len(data))

new = []
for d in data:
	if len(d) < 100 :
		new.append(d)
print("長度小於100有",len(new),"筆")
print(new[0])

good = []
for d in data :
	if 'good' in d:
		good.append(d)
print("有good的句子有",len(good),"筆")



#查找字典功能
data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append (line) 
		count +=1
		if count % 1000 ==0:
			print(len(data))
print("總共有",len(data),"筆資料")
print(data[0])
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key到字典
for word in wc:
	if wc[word] >1000000:
		print(word,wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你要找甚麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過的次數為:',wc[word])
	else:
		print('沒有出現過哦!')
print('感謝使用此功能')

