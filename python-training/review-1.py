# 資料：程式的基本單位
資料的種類：數字、字串、布林值、列表、集合Set{}、字典-鍵值對、變數



# 數字
n=int()  #轉數字
可以進行四則運算 (+,-,*,/,//取整數的除,%取餘數,**3次方,**0.5開根號)
可以用sum算總和
可以用判斷式+迴圈，建立在條件內重複執行算式

# 字串字串字串字串
有編號(序號)
可寫判斷式，知道資料內是否有該字元
\* 跳脫
*** *** 中間任意斷行

# 陣列
[1,2,4]
s=[4,5,6]
print[s(1)] # 得5
print[s(1:3)] # 取頭不取尾 得4,5
print[s(1:)] # 取投後面全部 得4,5,6
print[s(:3)] # 尾前面全部不取尾 得4,5
range()

# List & Tuple 列表（有序與無序列）
# List & Tuple 列表（有序可動與有序不可動）

呼叫、刪除、取代、串接，做完用print確認 #[]用順序選取 slicing
len()取得長度
巢狀列表呼叫法
List[]
Tuple()
取資料出來
改變資料順序 ( List , Tuple)
將資料取代 (List )


# 集合{} 沒有順序
# 可以用 in / not in
可以做交集、聯集、差集、反差集
& | - ^
set可以打散字串編碼，變成集合
print ("a" in b) # 會得到布林值


# 字典-鍵值對 key-value pair
可以刪除鍵值對 del
可以知道鍵值對是否存在，查詢"鍵"
可以從列表建立字典
"fruit=n for n in [apple, banana, oragne]"
dic={"fruit":n for n in [apple,banana,orange]}

# 變數
變數運算
n=n+1
n+=1

# condition

if True:
    print("這是True")

if True:
    print("這是True")
else:
    print("這是False")

if True:
    print("這是True")
elif:
    print("判斷條件2")
else:
    print("最後判斷,False")

n=int(input("請輸入: "))
if n%0:
    print("n是偶數")
else:
    print("n是奇數")

# 迴圈 while switch for *python 目前不支援 switch
可用 # break (停止迴圈)  # continue (強制繼續迴圈) # else (結束前執行)

for n in []
    if n

# 轉換資料型別 str() float() chr()
# List 的資料變動 (Tuple不可更動)  是用編號選取操作s[] !=資料本身
# 串接直接加list s=s+[1,2,3] 那可以減嗎? 不能!!!