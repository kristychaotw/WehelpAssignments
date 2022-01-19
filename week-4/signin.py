from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
# 建立application物件，可以設定靜態檔案的路徑處理
app=Flask(__name__,static_folder="public",static_url_path="/")  
app.secret_key="mysecretkey" #載入session後設定

# 建立路徑 / 對應的處理函式  
@app.route("/")   # 網站首頁
def index():
    return render_template("index.html")

# 使用post方法，處理路徑 /  登入的對應函式
@app.route("/signin",methods=["POST"])
def handle():
    # 接收POST方法的 Query String
    name=request.form["account"]
    pwd=request.form["pwd"]
    if name!="test" or pwd!="test":
        if name=="" or pwd=="":
            return redirect("/error?message=請輸入帳號密碼")
        else:
            return redirect("/error?message=帳號、或密碼輸入錯誤")
    else:
        session["username"]=name
        return redirect("/member")
        
        # result="登入成功"
        # name=="test" and pwd=="test":
        # return render_template("result.html",data=result)

        

# 利用要求字串(Query String)提供彈性 : /error?message=自訂訊息
@app.route("/error")  #錯誤頁面，抓取參數?message的資料
def handleError():
    message=request.args.get("message",None) 
    return render_template(
        "result2.html",
        msg=message
    )


@app.route("/member")   #成功頁面
def handleMember():
    if "username" not in session:
        return redirect("/")
    else:
        return render_template("result.html")
    
    

@app.route("/signout")    #登出頁面
def handleSignout():
    session.pop('username',None)
    return redirect("/")



app.run(port=3000)