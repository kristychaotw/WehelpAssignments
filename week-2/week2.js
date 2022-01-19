/* javascript注意名稱空間 */
/* 同一空間不重複宣告變數 函式外=全域空間 函式內=區域變數 */
/* 外部程式碼不能使用內部變數 */

/* 第一題 */
/* while 迴圈 */
function calculate(min, max) {
    let sum = 0
    let x = min
    while (x <= max) {
        sum = sum + x;
        x++;
    }
    console.log(sum);
}
/* for 迴圈 */
function calculate(min, max) {
    let sum = 0
    for (let x = min; x <= max; x++) {
        sum += x;
    }
    console.log(sum);
}

calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30


/* 第二題 */

function avg(data) {
    // console.log(data);

    let x = data.employees;
    // console.log(x);
    // console.log(x.length);
    // console.log(x.salary); /*不會動 為什麼?*/

    sum = 0
    for (i = 0; i <= x.length - 1; i++) {
        // console.log(x[i])
        // console.log(x[i].salary)
        sum = sum + x[i].salary
        // console.log(sum)
    }
    avgtotal = sum / x.length
    console.log(avgtotal);
}


avg({
    "count": 3,
    "employees": [{
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
}); // 呼叫 avg 函式



/* 第三題 */
/* 注意index和length的回傳的差異，index用編號回傳值，length回傳長度 */
/* 最大值 1/0或Infinity 最小值-1/0*或-Infinity */
function maxProduct(nums) {
    // console.log(nums.length);
    let maxnum = -1 / 0;
    for (i = 0; i < nums.length; i++) {
        for (j = i + 1; j < nums.length; j++) {
            x = nums[i] * nums[j]
            // console.log("這是外圈第"+i+"位的結果"+x);
            if (x > maxnum) {
                maxnum = x;
            }
        }
    }
    console.log("maxnum:" + maxnum)
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0





/* 第四題 */

function twoSum(nums, target) {

    // console.log(nums);
    // console.log(target);


    for (i = 0; i < nums.length; i++) {
        for (j = i + 1; j < nums.length; j++) {
            y = nums[i] + nums[j];
            if (y == target) {
                // console.log("兩數:"+nums[i],nums[j]);
                return ([i, j])
            }
        }
    }



    // your code here
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


function maxZeros(nums){
    let maxlen=0;
    let sum=0;
    for(i=0;i<=nums.length;i++){
        if (nums[i]==0){
            sum+=1;
        }else{
            if (sum>maxlen){
                maxlen=sum;
            }
        sum=0;
    }

    if (sum>maxlen){
        maxlen=sum;
    }

    console.log(maxlen)

    maxZeros([0, 1, 0, 0]); // 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
    maxZeros([1, 1, 1, 1, 1]); // 得到 0
    maxZeros([0, 0, 0, 1, 1]) // 得到 3