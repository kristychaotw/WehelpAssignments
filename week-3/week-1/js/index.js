let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

fetch(src).then(function (response) {
    return response.json();
}).then(function (result) {
    // console.log("json的資料",result);
    let data = result.result.results; //data 是results裡面的陣列
    console.log("只要results:", data, "data的形式是", typeof data);



// 取得 data 中 標題和第一張圖片
let title=[];
let spotimg=[]
let newspotimg=[]
for (p=0;p<data.length;p++){
        title[p] = data[p].stitle;
        spotimg[p] =data[p].file;
        newspotimg[p]=spotimg[p].split("http").map(x => { return "http"+x }).slice(1)
    }
    console.log("景點名稱:",title, "景點圖片url:",newspotimg);
    
    // 換掉 html 中的標題和圖片
    
    for(num=1;num<=8;num++){  
            let newbox = document.createElement("newbox" + num);
            let newcontent = document.createTextNode(title[num - 1]);
            newbox.appendChild(newcontent);
            document.getElementById("txt" + num).appendChild(newbox);
            document.getElementById("pic"+num).style.backgroundImage="url("+newspotimg[(num-1)][0]+")"; 
        }
        
    })

let c = 0;
let loadmore = function(){
    // 做8個div
    let addgroup = document.getElementById("groupdiv").cloneNode(true);
    document.getElementById("list").appendChild(addgroup);
    
    // 換掉8個div內的內容
    // c++;
    // console.log("按了幾次按鈕:",c);
    // document.getElementById("pic"+c*8).style.backgroundImage="url("+newspotimg[(c*8-1)][0]+")";
    
    
} // loadmore end



let btn=document.getElementById("btnload");
btn.addEventListener("click",loadmore);











//----------------------------------以下是舊的程式碼----------------------------


// 換圖片標題
// title = []
// for (let i = 0; i < data.length; i++) {
    //     title[i] = data[i].stitle
// }
// console.log(title, typeof [title]);

// function changeTitle(num) {
//     let newbox = document.createElement("newbox" + num);
//     let newcontent = document.createTextNode(title[num - 1]);
//     newbox.appendChild(newcontent);
//     document.getElementById("txt" + num).appendChild(newbox);
// }
// changeTitle(1)
// changeTitle(2)
// changeTitle(3)
// changeTitle(4)
// changeTitle(5)
// changeTitle(6)
// changeTitle(7)
// changeTitle(8)


// 換圖片
// spotimg = []
// newspotimg=[]
// for (let i = 0; i < data.length; i++) {
//     spotimg[i] = data[i].file
//     newspotimg[i]=spotimg[i].split("http").map(x => { return "http"+x }).slice(1)
// }
// console.log(newspotimg, typeof [newspotimg]);
// console.log(newspotimg[0][0])
// console.log(newspotimg[1][0])
// console.log(newspotimg[2][0])
// console.log(newspotimg[3][0])

//     link=""
//     for (i=0;i<=8;i++){
//         link=newspotimg[i][0]
//     }
//     console.log(link);
    

//     function changeImg(num) {
//         document.getElementById("pic"+num).style.backgroundImage="url("+newspotimg[(num-1)][0]+")";
//     }
//     changeImg(1)
//     changeImg(2)
//     changeImg(3)
//     changeImg(4)
//     changeImg(5)
//     changeImg(6)
//     changeImg(7)
//     changeImg(8)
// })
