#coding: utf-8

import random

ene = random.randint(1,13)
my = random.randint(1,13)

print("あなたは1から13までの数字どれかが印刷された手札を1枚持っています。")
print("持っている数字を確かめることはできません。")
print("それは対戦相手も同じ条件です")
print("これからあなたはもう1枚カードを引きます。")
print("あと1枚引いて、合計で21に近かった方の勝ち。")
print("21をオーバーしたら、負け。")

r = raw_input("あなたは1から13の数字、どのカードを引く？")

my += int(r)
ene += random.randint(1,13)

print("あなたは"+ str(my))
print("相手は" + str(ene))

if my > ene and my <= 21:
	print("あなたの勝ち。")
elif ene > my or my > 21:
	print("あなたの負け。")
else:
	print("泥沼試合")