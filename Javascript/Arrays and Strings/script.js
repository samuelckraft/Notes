
//Push

let ingredients = ['flour', 'butter', 'eggs'];

ingredients.push('sugar');

console.log(ingredients); // Output: ['flour', 'butter', 'eggs', 'sugar']


//Pop

let fruits = ['apple', 'banana', 'orange'];

let lastFruit = fruits.pop();



console.log(lastFruit); // Output: orange

console.log(fruits); // Output: ['apple', 'banana']

//Map

let numbers = [1, 2, 3];

let doubled = numbers.map(num => num * 2);

console.log(doubled); // Output: [2, 4, 6]


// Filter

let scores = [75, 80, 65, 90, 85];

let passing = scores.filter(score => score >= 70);

console.log(passing); // Output: [75, 80, 90, 85]


// Reduce

let expenses = [100, 50, 75, 120];

let total = expenses.reduce((acc, curr) => acc+curr, 0);

console.log(total); // Output: 345


// Sort

let sorting = ['animal', 'leopard', 'basin', 'monkey', 'grow'];

let sorting_numbers = [5, 12, 32, 25];

sorting_numbers.sort();
sorting.sort();

console.log(sorting); // Output: ['animal', 'basin', 'grow', 'leopard', 'monkey']
console.log(sorting_numbers); // Output: [12, 25, 32, 5] //breaks it down by the first digit, not actual number

sorting_numbers.sort((a, b) => a-b); // runs it as 5-12 then it can see if 5 is greater than, less than or equal to 12 depending on if it returns a negative, positive or 0
console.log(sorting_numbers) // Output: [5, 12, 25, 32]

console.log("Iterating over list");


//for of loop returns value not index
for (let item of sorting) {
    console.log(item)
};
/*Output:
Iterating over list
animal
basin
grow
leopard
monkey */


// Destructuring

// let [first, second, third, fourth, fifth] = sorting;

// console.log('First item:', first);
// console.log('Third item:', third);

/* Output:
First item: animal
Third item: grow */

//let [first, second] = [second, first]  // destructuring can let you swap values in a list


// spread

let original = [1, 2, 3];

let newArray = [...original, 4, 5];

console.log(newArray); // Output: [1, 2, 3, 4, 5]

//can also be used to copy an array
let copyArray = [...original];

console.log(copyArray); // Output: [1, 2, 3]

// rest

let [first, second, ...remaining] = newArray;

console.log('First item:', first); // Output: First item: 1
console.log('Second item:', second); // Output: Second item: 2
console.log('Remaining:', remaining); // Output: Remaining: (3) [3, 4, 5]


// Strings

let greeting = 'Hello, World!'

console.log(greeting.length) // Output: 13

console.log(greeting.toUpperCase()) // Output: HELLO, WORLD!
 
console.log(greeting.substring(2,9)) // Output: llo, Wo

console.log(greeting.split(',')) // Output: ['Hello', ' World!']

console.log(greeting.split('l')) // Output: ['He', '', 'o, Wor', 'd!']

// string search techniques

/*

.includes() - returns true or false if element exists in string
.indexof() - returns index of first instance of element/first letter of element string
.lastindexof() - retuns index of the last instance of element

*/

let sentence = "The quick brown fox jumps over the lazy dog"

console.log(sentence.includes('fox')); // Output: true

console.log(sentence.indexOf('T')); // Output: 0

console.log(sentence.lastIndexOf('a')); // Output: 36


// Regex

let pattern = /hello/;

console.log(pattern.test("hello world!")); // Output: true

console.log("Hey @SamKraft, great game today".match(/@[A-Za-z0-9_]+/g)) // Output: ['@SamKraft']

let pattern2 = /\\d+/; //Matches one or more digits

console.log(pattern2.test("abc123")); 

console.log("abc123".match(pattern2))