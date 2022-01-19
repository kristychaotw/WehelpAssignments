#///////////// 第一題 ////////////////////////////////////////////////////////

def calculate(min, max):
# 想法1: 累加連續數字，加上區間宣告迴圈範圍，加上判斷宣告迴圈停止條件
# 用變數n代表min~max之間所有數字，
# 在for迴圈中先判斷後累加，
# 直到判斷n等於max+1時停止迴圈,
# 停止前印出sum
# 後來發現不用判斷式也沒關係，區間本來就有範圍
    sum=0
    for n in range(min,max+1):
        # if n==max+1:
        #     break
        sum=sum+n
    else:
        print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

def calculate(min, max):
# 想法2: 累加從min開始的連續數字，加到max停止迴圈
    sum2=0
    x=min
    while x <= max:
        sum2=sum2+x
        x+=1
    else:
        print(sum2)
    

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#///////////// 第二題 ////////////////////////////////////////////////////////
# avg的參數data是鍵值對{count:3,employees:[]}
# 其中第二個配對的值(employees:[])，是列表，列表中有三個鍵值對，裡面有兩個配對。
# 做法：用迴圈跑employees裡面三個鍵值對，用key調出salary的資料並存放在變數n，並計算變數n的總和/個數=平均值

def avg(data):
    # print(data["count"])
    # print(data["employees"])

    sum=0
    for i in data["employees"]:
        n=i["salary"]
        sum+=n
    # print(sum)

    avgtotal=sum/data["count"]
    print(avgtotal)



avg({"count":3,
    "employees":[
        {"name":"John","salary":30000},
        {"name":"Bob","salary":60000},
        {"name":"Jenny","salary":50000}
    ]
}) # 呼叫 avg 函式



#///////////// 第三題 ////////////////////////////////////////////////////////

def maxProduct(nums):
# 想法1: 0* 1 2 3  1*2 3 2*3，比較六個結果的大小取最大值
    result=None
    for i in range(0,len(nums)-1):
            for n in range(i+1,len(nums)):
                # result= nums[i]*nums[n]
                    if result:
                        if nums[i]*nums[n] > result:
                            result=nums[i]*nums[n]
                    else: 
                        result=nums[i]*nums[n]

    print(result)

# 想法2: 最大正整數兩兩相乘、或兩個最小負整數相乘
# 想法3: bubble sort重新排序，取最大兩數相乘為結果
            

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0


#///////////// 第四題 ////////////////////////////////////////////////////////

def twoSum(nums, target):
    result=None
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)):
            y=nums[i]+nums[j]
            if y==target:
                return([i,j])

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


def maxZeros(nums):
# 做法 (from 彭彭) # 記錄長度的變數sum 看到0 就+1  看到1就歸零
    sum=0
    maxlen=0
    for x in nums:         
        if x==0:
            sum+=1
        else:
            if sum > maxlen:
                maxlen=sum
            sum=0

    if sum > maxlen:
        maxlen=sum
            
    print(maxlen)

            
    
# 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
