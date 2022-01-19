# with 會自動關閉檔案，可以不用手動關
# 寫入新檔案      w
# 讀取已在的檔案  r


# 網路連線
# 串接、擷取公開資料
import urllib.request as req
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    data=json.load(response)# 利用 json 模組處理載入 json 資料格式
# print(data)

# 將景點資料列表出來(有註解名稱)
# 景點名稱，區域，經度，緯度，第一張圖檔網址
plist=data["result"]["results"]  #取得一個列表 看尾巴
with open("datawithtitle.txt","w",encoding="utf-8") as file:
    for place in plist:
        z= place["file"]
        newz=z.replace("https","\thttps")
        newzlink1=newz.split()[1]
        file.write("景點名稱:"+place["stitle"]+"\t景點地址:"+place["address"][5:8]+"\t景點經度:"+place["longitude"]+"\t 景點緯度:"+place["latitude"]+"\t景點圖片:"+newzlink1+"\n")  #分隔key-value用+號，不用,號

# 將景點資料列表出來(無註解名稱)
with open("data.txt","w",encoding="utf-8") as file:
    for place in plist:
        z= place["file"]
        newz=z.replace("https","\thttps")
        newzlink1=newz.split()[1]
        file.write(place["stitle"]+","+place["address"][5:8]+","+place["longitude"]+","+place["latitude"]+","+newzlink1+"\n")  #分隔key-value用+號，不用,號


# 測試更改地址欄位
# 結論：key-value，value的值為string，可以用序號[]抓取中間想要的字串
plist=data["result"]["results"]  #取得一個列表 看尾巴
with open("test-address.txt","w",encoding="utf-8") as file:
    for a in plist:
        y= a["address"][5:8]
        file.write("地址:"+y+"\n") 

# 測試只抓到一張圖的網址
# 結論：key-value，value的值為string，可以用序號[]抓取中間想要的字串
plist=data["result"]["results"]  #取得一個列表 看尾巴
with open("test-img.txt","w",encoding="utf-8") as file:
    for i in plist:
        z= i["file"]
        newz=z.replace("https","\thttps")
        newzlink1=newz.split()[1]
        file.write("圖片網址:"+newzlink1+"\n") 

# 要怎麼轉出 csv 檔案 ?
# 測試1：import csv的語法(寫不出來)
        # import csv
        # with open("data.txt","r",encoding="utf-8") as f:
        #     i=f.read()
        #     onelinelist=i.split(",")
        #     for i in onelinelist:
        #         print(i)

        # with open ("output.csv","w",encoding="utf-8",newline="") as csvfile:
        #     writer=csv.writer(csvfile, delimiter=",")

        #     writer.writerows()

# 測試2：直接改txt附檔名為csv，成功了?????
with open("data.csv","w",encoding="utf-8") as file:
    for place in plist:
        z= place["file"]
        newz=z.replace("https","\thttps")
        newzlink1=newz.split()[1]
        file.write(place["stitle"]+","+place["address"][5:8]+","+place["longitude"]+","+place["latitude"]+","+newzlink1+"\n")  #分隔key-value用+號，不用,號
