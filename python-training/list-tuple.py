# 有序可變動列表 List
grades=[12,60,15,70,90]
print(grades[3])  #[]索引
grades[0]=55 # 把55放到列表中的第一個位置
print(grades[0])
grades[1:4]=[] #連續刪除列表中從編號1到4(不包括)的資料
print(grades)
grades=grades+[12,33] #列表串接
print(grades)

length=len(grades) #取得列表的長度 len(列表資料)
print(length)

data=[[3,4,5],[6,7,8]]
print(data[0][0]) #第一層 第二層
data[0][0:2]=[5,5,5]
print(data)

# 有序不可變動列表 Tuple ()

data=(3,4,5)
print(data[0:2])  #3,4
# data[0]=5 # 錯誤: Tuple的資料不可以變動


data=(4,5,6,7,9)
print(data[2])
print(data[0:3])
# data[3]=9 #7會被9替代     #錯誤
# data[2:4]=[] #刪除        #錯誤
# data2=data+[44,55] #串接  #錯誤

datalength= len(data)
print(datalength)

data3=((1,3,5),(2,4,6))
print(data3[1][0])
# data3[0][0:2]=(7,7,7) #錯誤: Tuple的資烙不可以變動
print(data3)


n=int(input("請輸入: "))
if n%2==0:
    print("n是偶數")
else:
    print("n是奇數")
    
x=int(input("請輸入數字1:"))
y=int(input("請輸入數字2:"))
z=input("請輸入運算符號:")

if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    print(x/y)
else:
    print("無法運算")