## 3：SQL CRUD
使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![1](https://user-images.githubusercontent.com/95632624/151668387-9fe501b0-8c93-4f24-9cf2-5dc841f1785c.jpg)

使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![2](https://user-images.githubusercontent.com/95632624/151668455-30d86080-3c38-47b3-a3a8-8935c32e1b48.jpg)

使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![3](https://user-images.githubusercontent.com/95632624/151668459-5630985c-e409-45bd-bb71-93bdd67a7130.jpg)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
![4](https://user-images.githubusercontent.com/95632624/151668465-b5ab5c1c-897a-4c35-92d7-70d6779bb2ad.jpg)

使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![5](https://user-images.githubusercontent.com/95632624/151668468-9d455bfb-9618-43f9-af1f-94324529cf77.jpg)

使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![7](https://user-images.githubusercontent.com/95632624/151668472-3f8bc896-a99e-4733-a522-cd3a43eeff89.jpg)
 
使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
![8](https://user-images.githubusercontent.com/95632624/151668475-cfb59a02-acb8-4f86-8abc-3964f2a09c9d.jpg)

## 4：SQL Aggregate Functions
取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![9](https://user-images.githubusercontent.com/95632624/151668482-8f28adb9-0583-4df0-bd88-217c660ffc4a.jpg)
取得 member 資料表中，所有會員 follower_count 欄位的總和。
![10](https://user-images.githubusercontent.com/95632624/151668493-9a9b9372-e841-41ba-9bb5-5d922acf06b9.jpg)
取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![11](https://user-images.githubusercontent.com/95632624/151668497-3bae7cc3-2dca-4e86-965d-1d12bf804043.jpg)

## 5：SQL JOIN (Optional)
在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定
![12](https://user-images.githubusercontent.com/95632624/151668506-4d139b6e-4c08-4044-82c5-2845cd3723dc.jpg)
使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![13](https://user-images.githubusercontent.com/95632624/151668531-d59d5ad4-18e4-4ef6-bd4d-1a5f895bb1a1.jpg)
使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
![14](https://user-images.githubusercontent.com/95632624/151668544-15837849-c7a8-4b99-8f02-5fa077f3ff8b.jpg)

