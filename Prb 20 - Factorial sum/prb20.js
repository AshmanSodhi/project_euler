var num = 5
var sum = 0
var factorial = 1

for (var i = 1 ; i <= num ; i++){
    factorial = factorial*i
}
console.log(factorial)

let myFunc = num => Number(num);
      
var intArr = Array.from(String(factorial), myFunc);

for (let i = 0; i < intArr.length; i++ ) {
    sum += intArr[i];
  }
  
console.log(sum);