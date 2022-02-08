let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

function getData() {
    return new Promise(function (resolve, reject) {
        let req = new XMLHttpRequest();
        req.open("get", src);
        req.onload = function () {
            resolve(this.responseText);
            req.onerror = function () {
                reject("error")
            }
        };
        req.send()
    });
}

// 主程式 ，promise連線回來的json資料會變字串，要用JSON.parse改回物件
let dataPromise = getData();
dataPromise.then(function (result) {
    let data = JSON.parse(result).result.results; // 資料型態為object
    // console.log(data);


    // 換掉1-8
    for(a=1;a<=8;a++){  
        let title = data[a].stitle;
        let spotimg = data[a].file.replace(/http/ig, ',http').split(",")[1];
        console.log(title, spotimg);

        let newbox = document.createElement("newbox" + a);
        let newcontent = document.createTextNode(title+a);
        newbox.appendChild(newcontent);
        document.getElementById("txt" + a).appendChild(newbox);
        document.getElementById("pic"+a).style.backgroundImage="url("+spotimg+")"; 
    }
    


    // 在loadmore按鈕上註冊事件監聽 點擊事件
    // 每次點擊按鈕都加八個div
    const btnLoad = document.getElementById("btnload")
    const listDiv = document.getElementById("list")
    btnLoad.addEventListener("click", addGroup)
    let click = 0;
    let num = 0;

    function addGroup() {
        click = click + 1;
        console.log("按了幾次:", click);
        const newGroup = document.createElement("div")
        newGroup.classList.add("newGroup" + click, "boxgroup")
        listDiv.appendChild(newGroup);

        for (n = 1; n <= 8; n++) {
            num = click * 8 + n;
            const newDiv = document.createElement("div")
            const newPic = document.createElement("div")
            const newTxt = document.createElement("div")
            newDiv.classList.add("box" + (num), "box", "col-12", "col-md-6", "col-lg-3")
            newTxt.classList.add("txt" + (num), "txt")
            newPic.classList.add("pic" + (num), "pic")
            document.querySelector(".newGroup" + click).appendChild(newDiv)
            document.querySelector(".box" + (num)).appendChild(newPic)
            document.querySelector(".box" + (num)).appendChild(newTxt)

            let title = data[num].stitle;
            let spotimg = data[num].file.replace(/http/ig, ',http').split(",")[1];
            console.log(title, spotimg);
            
            document.querySelector(".pic"+num).style.backgroundImage="url("+spotimg+")";
            newTxt.innerText = title;
            
        }

    }

}, function (error) {
    console.log(error);
}); // 主程式結束