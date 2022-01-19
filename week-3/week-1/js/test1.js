// Ajax 預設是一個非同步的程式
// 用Promise或callback使主程式乾淨,接續回傳後的運作

function getData(){
    return new Promise(function(resolve, reject){
        let req=new XMLHttpRequest()
        req.open("get", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
        req.onload = function(){
            resolve(this.responseText); //呼叫resolve
        }; // onload end
        
        req.onerror = function(){
            reject("Error") // 呼叫reject
        }; // onerror end
        req.send();
    }); //Promise end
}
// 這是主程式
let promise = getData();
promise.then(function(result){
    console.log(result); 


}).catch(function(err){
    console.log(err);
});




function init() {
    let showimg = document.getElementById("picid");
    let loadimg = function () {
        console.log("Test");
    };
    picid.addEventListener("onload", loadimg)
}