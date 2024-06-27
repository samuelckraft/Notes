// if

let age = 23;

if (age >= 21) {
    console.log("Welcome to the party")
}

// else if and else

let time = 14;

if (time < 12) {
    console.log("Good Morning")
} else if (time < 18) {
    console.log("Good Afternoon")
} else {
    console.log("Good Evening")
}

// nested if

let isRaining = true;
let umbrella = false;

if (isRaining) {
    if (umbrella) {
        console.log("Grab an umbrella")
    } else {
        console.log("Don't go outside")
    }
} else {
    console.log("What a beautiful day")
}


// increment/decrement

let num = 5;

console.log(num++); //Output: 5
console.log(num); //Output: 6


//for loops

for (let i = 0; i<5; i++) {
    console.log("Iteration:", i)
}
/* Output: 
Iteration:  0
Iteration:  1
Iteration:  2
Iteration:  3
Iteration:  4 */

let my_arr = [1, 2, 3, 4, 5, 6];

for (let i = 0; i > my_arr.length; i++) {
    console.log("Iteration:", i, my_arr[i])
};
/* Output:
Iteration:  0 1
Iteration:  1 2
Iteration:  2 3
Iteration:  3 4
Iteration:  4 5
Iteration:  5 6 */


//while
let count = 0;
while (count < 5) {
    console.log("Count:", count);
    count++
}
/* Output:
Count:  0
Count:  1
Count:  2
Count:  3
Count:  4 */


// do-while

let num1 = 7;

do {
    console.log("Number:", num1)
    num1++
} while (num1 <=5)

// Output: Number: 7


// for in 

const fruits = ['apple', 'banana', 'cherry']

for (const fruit in fruits) {
    console.log("Fruit", fruit)
}
/* Output:
Fruit 0
Fruit 1
Fruit 2 */

for (const fruit in fruits) {
    console.log("Fruit", fruits[fruit])
}
/* Output:
Fruit apple
Fruit banana
Fruit cherry */

const fruits1 = 'apple'

for (const fruit in fruits1) {
    console.log(fruits1[fruit])
}
/* Output:
a
2p  //since there are two p's
l
e */

// nested loops

for (let i = 0; i<3; i++) {
    for (let j=0; j<3; j++){
        console.log(`(${i}, ${j})`);
    }
}
/* Output:
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)*/

// Functions
function greet(name) {
    return "Hello " + name + "!"
}

console.log(greet("Sam")) // Output: Hello Sam!

//closures

// Important for 3 reasons
// 1. encapsulation - data in outer function is only accessible in inner function
// 2. reusability and configuration - if we create more functions we can alter depending on what is passed in
// 3. maintaining state - this allows us to maintain the state of the function over multiple calls; React principle
function outer() {
    let message = "Hello";
    function inner() {
        message += "!"
        console.log(message);
    }
    return inner
}

const myFunc = outer();
myFunc();
myFunc();

/* Output:
Hello!
Hello!! */