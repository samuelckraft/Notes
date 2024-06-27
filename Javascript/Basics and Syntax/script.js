
//Output Methods
/* alert('Alert'); //alert

console.log('Console Log') //function that logs the message to the console

document.write('Write') //writing directly to document */

// Variables


//var
/*var name1 = "Sam"

name1 = "Davis" //reassigning the value

console.log(name1) //returns Davis due to hoisting, meaning it will only work if the variable has been assigned before being called

var name1 = "Caden" //redeclaring the value */


//let

/* let name1 = "Sam"

// let name1 = "John" //returns error because it can not be redeclared

name1 = "John" //can be reassigned

function myfunction() {
    let name1 = "Jon Snow" //can be redeclared if it's outside the scope
} 
    
let name1 //can substantiate let variables without giving them a value

name1 = "Sam" */

//const

/* const name1 = "Sam" //cannot be reassigned or redeclared

//name1 = "Davis" //won't throw error here, but will cause error when running code */


//Declaring variables

let string = "Sam";
let num = 30;
let bool = true;
let array = ['apple', 'banana', 'orange'];
let object = {name: 'Sam', age:23};

console.log("String:", string);
console.log("Number:", num);
console.log("Boolean:", bool);
console.log("Array:", array);
console.log("Object:", object);

console.log(typeof string); //Output: string
console.log(typeof num); //Output: number
console.log(typeof bool); //Output: boolean
console.log(typeof array); //Output: objec
console.log(typeof object); //Output: object
console.log(typeof undefined); //Output: undefined

//how to find if it's an array since typeof returns object for lists
console.log(Array.isArray(array)) //Output: true

//arithmetic
let x = 5;
let y = 3;
let sum = x+y;
console.log("Sum:", sum)

//comparison
let isGreaterThan = x>y;
console.log("Is x greater than y?", isGreaterThan) //Output: false

//logical
let isvalid = true && false;
console.log("Is it valid?", isvalid) //Output: false


//Type conversion

console.log(5 + '5') //Output: 55 (as a string)

console.log(10 - '5') //Output: 5 (as an integer)

console.log('true' == true) //Output: false

console.log(+'100') //Output: 100 (as an integer)

console.log(0 == false) //Output: true
console.log("" == false) //Output: true

console.log(0 === false) //Output: false
console.log("" === false) //Output: false