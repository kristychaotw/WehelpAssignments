# 這是註解
# 叫出終端機快捷鍵 也可做快速切換ctrl+~
# cls可以清空終端機
# 可以把終端機換成 git bash (明天再說)
print("hello python")


#資料: 程式的基本單位
    #數字
    1234
    3.5
    #字串
    "測試中文"
    "hello world"
    #布林值
    True
    False

    #有順序、可動的列表 List
    [3,4,5]
    ["helloworld, hello ant"]

    #有順序、不可動的列表 Tuple
    (3,4,5)
    ("hello","world")

    #集合 Set
    {3,4,5}
    {"Hello","World"}

    #字典 Dictionary 鍵與值的配對
    {"apple":"蘋果","data":"資料"}

    #變數: 用來儲存資料的自訂名稱
    #正確變數名稱：英文開頭
    #有彈性：放新的資料進去，就會取代舊的
    #變數名稱 = 資料
    x=3

    #print(資料)
    print(3)
    print(True)
    print([1,2,3])
    print(x)
    #print(變數帶出的資料)
    x=True
    print(x)
    x="Hello"
    print(x)
    x={3,7,8} #集合
    print(x)


#數字運算
    x=3/6
    print(x)
    y=7/6
    print(y)
    z=7//6
    print(z)
    #整數除法//
    #除法/

    x=2**3
    #2的三次方 8
    x=2**0.5
    #2的開根號 0.414
    x=7%3
    #取餘數
    print(x)

    x=2+3
    x+=1 # x=x+1 # 將變數中的數字 +1
    # +=是+符號的變形
    x-=1  #資料減1
    x*=1  #資料乘1

#字串運算 : 表示法 串接重複 索引字元
#字串會對內部字元編號(索引)，從0開始算起
    s="hello"
    s="hell\"o" # 跳脫\
    s="hello"+"world"  # + 或是空白 串接字串
    s="""Hello
    word
    hihi

    hi
    """ 
    print(s)
    s="hello\nworld" # 換行\n 或是"""三個括號內自由換行
    print(s)
    s="hello"*3+"world"
    print(s)
    s="hello\n"*2+"hello" #hello換行

    print(s[0])  #取得字串索引
    print(s[1:4]) #取得內部字串，取頭不取尾
    print(s[1:])  #取得開頭後面全部，取頭
    print(s[:4])  #取得結尾前面全部，不取尾
    print(s[0],s[2],s[4])  #分開取字元