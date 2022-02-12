import os

# Part1 : 連結MySQL資料庫
from cmath import log
from distutils.util import execute
from tracemalloc import stop
import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user=os.environ.get('DB_USER'),            
  password=os.environ.get('DB_PWD'), 
  database="week6"
)
print(mydb)



mycursor=mydb.cursor()

# 建立表格、設定表格格式與內容
# mycursor.execute("CREATE DATABASE week6")
# mycursor.execute("CREATE TABLE Member (name VARCHAR(255) NOT NULL, user VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, ID bigint PRIMARY KEY AUTO_INCREMENT, time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")
# mycursor.execute("DESCRIBE Member")
# mycursor.execute("INSERT INTO Member (name, user, password) VALUES (%s,%s,%s)",("imtest1", "test1", 123))
mydb.commit()

# 刪除表格、刪除表格內容指令
# mycursor.execute("DROP TABLE Member")
# mycursor.execute("DELETE FROM Member")
# mycursor.execute("ALTER TABLE Member AUTO_INCREMENT = 1")




# Part2 : 設定後端程式
# 建立app物件 / 設定靜態檔案自訂路徑
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__, static_folder="public",static_url_path="/")
# 設定session的密鑰
app.secret_key=str(os.environ.get('PY_KEY'))

# 使用GET方法連線，建立路徑 "/" 對應的處理函式
@app.route("/")
def index():
    return render_template("index.html")

# 使用POST方法連線，建立路徑 "/signup" 對應的處理函式
@app.route("/signup", methods=["POST"])
def signUp():
    newusername=request.form["name"]
    newuser=request.form["user"]
    newuserpsd=request.form["pwd"]
    print("註冊使用者輸入:",newusername,newuser,newuserpsd)
   
    
    
    if (newuser != "" and newuserpsd != "" and newusername != ""):
        mycursor.execute("SELECT user FROM Member WHERE user='"+newuser+"'")
        checkuser=mycursor.fetchall()
        print("checkuser是:",checkuser,"資料:",type(checkuser),len(checkuser))
        if len(checkuser) != 0: # db裡面有資料
            for i in checkuser:
                print("i是:",i,"資料:",type(i))
                print("i[0]是:",i[0],"資料:",type(i[0]))
                if newuser == i[0]: # 有資料且有符合
                    print("資料庫裡有:newuser")
                    return redirect("/error?message=帳號已經被註冊")

                else: # 有資料但不符合 newuser
                    mycursor.execute("INSERT INTO Member (name, user, password) VALUES (%s,%s,%s)",(newusername, newuser, newuserpsd))
                    mydb.commit()
                    print("已將 user: "+newuser+"資料存入資料庫")
                    return redirect ("/")
        else: # db裡面沒有資料
            mycursor.execute("INSERT INTO Member (name, user, password) VALUES (%s,%s,%s)",(newusername, newuser, newuserpsd))
            mydb.commit()
            print("已將 user: "+newuser+"資料存入資料庫")
            return redirect ("/")

    else:
        return redirect("/error?message=有空白欄位，請重新輸入註冊資料")


    # ================================================================
    # ===========================舊程式碼==============================
    
    # userdblist=""
    # mycursor.execute("SELECT user FROM Member")
    # selectuser=mycursor.fetchall()
    # # print("existuser的結果:",existuser)
    # for userdb in selectuser:
    #     userdb=userdb[0]
    #     userdblist=userdblist+" "+userdb
    #     print("userdb結果:",userdblist,"類型:",type(userdblist))

    # if (newuser != "" and newuserpsd != "" and newusername != ""):
        
    #     if newuser in userdblist:
    #         print("資料庫裡有:newuser")
    #         return redirect("/error?message=帳號已經被註冊")

    #     else:
    #         mycursor.execute("INSERT INTO Member (name, user, password) VALUES (%s,%s,%s)",(newusername, newuser, newuserpsd))
    #         mydb.commit()
    #         print("已將 user: "+newuser+"資料存入資料庫")
    #         return redirect ("/")
    # else:
    #     return redirect("/error?message=有空白欄位，請重新輸入註冊資料")
    
    # ================================================================
    # ===========================舊程式碼end===========================


# 使用POST方法連線，建立路徑 "/signin" 對應的處理函式
@app.route("/signin", methods=["POST"])
def signIn():
    userlogin=request.form["user"]
    psdlogin=request.form["psd"]

#  WHERE user="+"'"+userlogin+"'"
#  WHERE user=+"'"+userlogin+"'"
    target="SELECT user, password FROM Member WHERE user="+"'"+userlogin+"'"
    mycursor.execute(target)
    checklogin=mycursor.fetchall()
    print("登入使用者輸入:",userlogin,psdlogin)
    print("checklogin是:",checklogin,"資料:",type(checklogin),len(checklogin))
     
    if len(checklogin) != 0: # db裡面有資料
        for p in checklogin:
            if p[0] == userlogin and p[1] ==psdlogin:
                print("帳密符合")
                session["user"]=userlogin
                result=redirect("/member?name="+userlogin)
                break
        
            else:
                print("帳密不符合")
                result=redirect("/error?message=帳號或密碼輸入錯誤")
                continue

        return result

    else: # db裡面沒資料
        result=redirect("/error?message=帳號或密碼輸入錯誤")
    return result


    # list=()
    # for n in existuser:
    #     print("n:",n)
    #     list=list+n
    # print("list:",list,'list len:',len(list))

    # for i in range (0,(len(list)//2)):
    #     dbuser=list[2*i]
    #     dbpwd=list[2*i+1]
    #     print("db帳號:",dbuser,"db密碼:",dbpwd)
    #     if (dbuser == userlogin and dbpwd == psdlogin):
    #         print(list[2*i]+"帳密符合")
    #         session["user"]=userlogin
    #         result=redirect("/member?name="+userlogin)
    #         break
    #     else:
    #         print(list[2*i]+"帳密不符合")
    #         result=redirect("/error?message=帳號或密碼輸入錯誤")
    #         continue
    # return result

# ================================================================
# ===========================舊程式碼==============================

#  target="SELECT user, password FROM Member"
#     mycursor.execute(target)
#     existuser=mycursor.fetchall()
#     list=()
#     for n in existuser:
#         print("n:",n)
#         list=list+n
#     print("list:",list,'list len:',len(list))

#     print("登入使用者輸入:",userlogin,psdlogin)
#     for i in range (0,(len(list)//2)):
#         dbuser=list[2*i]
#         dbpwd=list[2*i+1]
#         print("db帳號:",dbuser,"db密碼:",dbpwd)
#         if (dbuser == userlogin and dbpwd == psdlogin):
#             print(list[2*i]+"帳密符合")
#             session["user"]=userlogin
#             result=redirect("/member?name="+userlogin)
#             break
#         else:
#             print(list[2*i]+"帳密不符合")
#             result=redirect("/error?message=帳號或密碼輸入錯誤")
#             continue
#     return result

# ================================================================
# ===========================舊程式碼end===========================

# 建立路徑 "/error" 對應的處理函式
@app.route("/error")
def handleError():
    msg=request.args.get("message","")
    return render_template("error.html",message=msg)

# 建立路徑 "/member" 對應的處理函式
@app.route("/member")
def handleMember():
    if "user" not in session:
        return redirect("/")
    else:
        name=request.args.get("name","")
        return render_template("member.html",name=name)

# 建立路徑 "/signout" 對應的處理函式
@app.route("/signout")
def handleSignOut():
    session.pop("user",None)
    return redirect("/")

# 啟動網站伺服器
app.run(port=3000)