let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
fetch(src).then(function (response) {
    return response.json();
}).then(function (result) {
    // console.log("json的資料",result);
    let data = result.result.results; //data 是results裡面的陣列
    console.log("只要results:", data);


    // 換圖片標題
    title = []
    for (let i = 0; i < data.length; i++) {
        title[i] = data[i].stitle
    }
    console.log(title, typeof [title]);


    function changeTitle(num) {
        let newbox = document.createElement("newbox" + num);
        let newcontent = document.createTextNode(title[num - 1]);
        newbox.appendChild(newcontent);
        document.getElementById("txt" + num).appendChild(newbox);
    }
    changeTitle(1)
    changeTitle(2)
    changeTitle(3)
    changeTitle(4)
    changeTitle(5)
    changeTitle(6)
    changeTitle(7)
    changeTitle(8)


    // 換圖片
    spotimg = []
    newspotimg=[]
    for (let i = 0; i < data.length; i++) {
        spotimg[i] = data[i].file
        newspotimg[i]=spotimg[i].split("http").map(x => { return "http"+x }).slice(1)
    }
    console.log(newspotimg, typeof [newspotimg]);
    // console.log(newspotimg[0][0])
    // console.log(newspotimg[1][0])
    // console.log(newspotimg[2][0])
    // console.log(newspotimg[3][0])

    link=""
    for (i=0;i<=8;i++){
        link=newspotimg[i][0]
    }
    console.log(link);
    

    function changeImg(num) {
        document.getElementById("pic"+num).style.backgroundImage="url("+newspotimg[(num-1)][0]+")";
    }
    changeImg(1)
    changeImg(2)
    changeImg(3)
    changeImg(4)
    changeImg(5)
    changeImg(6)
    changeImg(7)
    changeImg(8)
})
