# 函式
# 程式正確後，注意流程
# 參數可以讓我們的程式有彈性
# 函式分成「定義」&「呼叫」
# 回傳值: 「定義」裡面可以放return 資料/(none) #強制結束函式
# 回傳值: return什麼 變數就是什麼 把結果從函式內部帶出來 繼續進行程式碼

# 定義函式
# 函式內部程式碼，若是沒有做函式呼叫，就不會執行
def multiply(n1,n2):
    print(n1*n2)
# 呼叫函式 函式名稱()
multiply(3,4)
multiply(10,8)


def multiply(n1,n2):
    print(n1*n2)
    return n1*n2
# 呼叫函式 函式名稱()
value=multiply(3,4)
print(value)

# 要回傳結果再印出，還是在函式內印出結果，看之後寫程式怎樣比較方便
value=multiply(3,4)+multiply(10,5)
print(value)

# 函式可用來做程式的包裝: 同樣的邏輯可以重複利用 
sum=0
for n in range(1,11):
    sum=sum+n
print(sum)

sum=0
for n in range(1,21):
    sum=sum+n
print(sum)

def cal(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

cal(10)
cal(20)

