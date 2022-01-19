# 迴圈   重複跑同一個程式碼

# while 迴圈
# n=1
# while True:
#     print(n)
#     n+=1
# 無限迴圈不要寫
n=1
sum=0 # 紀錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)

# for 迴圈
for x in [3,6,1]:
    print(x)
for x in "AHHHH":
    print(x)
for x in range(5):
    print(x)
for x in range(5,10):
    print(x)

for x in range(1,11):
    sum=sum+x
print(sum)   #  上面也有sum會累加!