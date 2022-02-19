
let fetchData = function(){
    const kName = document.getElementById("kName").value
    const myUrl = new URL('http://127.0.0.1:3000/api/members')
    let params = [['username',kName]]
    myUrl.search = new URLSearchParams(params).toString();
    console.log("使用者輸入:",kName,"網址:",myUrl);
    
    fetch(myUrl).then(function(response){
        return response.json();
    }).then(function(result){
        console.log("最終的資料:",result,typeof(result));
        console.log("name:", result.data.name);
        showHere = document.querySelector(".showHere")
        showHere.innerHTML="他的名字是:"+result.data.name
    });

}

let btn = document.getElementById("btn")
btn.addEventListener("click", fetchData)






// let fetchData = function(){
//     const kName = document.getElementById("kName").value
//     const myUrl = new URL('http://127.0.0.1:3000/api/members')
//     let params = [['username',kName]]
//     myUrl.search = new URLSearchParams(params).toString();
//     console.log("使用者輸入:",kName,"網址:",myUrl);
    
//     fetch(myUrl, {
//         method:'GET',
//         mode:'cors',
//         headers:{
//             'Content-Type':'application/json',
//         },
//         body: JSON.stringify()
//     })
//     .then(res => {
//         return res.json()
//     })
//     .then(data => 
//         console.log("data:",data)
//         )
//     .catch(error => console.log('error'))

// }

// let btn = document.getElementById("btn")
// btn.addEventListener("click", fetchData)

