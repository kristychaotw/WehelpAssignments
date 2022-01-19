# 第一題：用迴圈計算 1+2+3+....+50 的結果。
sum=0
for x in range(1,51):
    sum=sum+x
print(sum)

# 第二題：1. 用迴圈把 [3, 1, 10, 5] 中的每個數字都逐一印出來。2. 把數字的平均數算出來。3. 找出其中最大的那個數字。
sum=0
p=[3,1,10,5]
for n in p:
        # print(n)
        sum=sum+n
# length=len(p)
# print(length)
# avg=sum/length
# print(avg)
print(sum/len(p))

max=0
for n in p:
    if n>max:
        max=n
print(max)


# 第三題：使用迴圈印出以下內容，注意每個文字的細節變化：

# 1 apple
# 2 apples
# 3 apples
# 4 apples
# ...
# ...
# 11 apples
# 1 dozen apples
# 13 apples
# 14 apples
# 15 apples

# ------------

for n in range(1,16):
    print(str(n)+" apples")
    if n%12==0:
        print(str(n//12)+" dozen apples")
