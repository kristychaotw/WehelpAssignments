console.log("hello");

fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json',{
    method:'post',
    headers:{
        'content-type':'application/json'
    },
    body: JSON.stringify({
        title:"stitle"
    })
}).then(res => {
    if (res.ok){
    console.log('success');
    }else{
    console.log('not successful');
    }
    res.json()
})
.then(res => res.json())
.then(data=>console.log(data))
.catch(error=>console.log('error'))  // for fetch, not api itself