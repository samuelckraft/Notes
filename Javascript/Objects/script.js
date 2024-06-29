let superhero = {
    name: "Iron Man",
    powers: ['Flight', 'Super Strength', 'Genius-level Intellect'],
    suitColor: 'Red and Gold',
    alignment: {'good': 'yes'},
    nameColors: function () {
        return this.name + ': ' + this.suitColor
    }
};

console.log(superhero.name); // Dot notation - Output: Iron Man
console.log(superhero['powers']); // bracket notation - Output: ['Flight', 'Super Strength', 'Genius-level Intellect']

    // can combine them 

console.log(superhero.name[0]); //Output: I
console.log(superhero['powers'][1]); // Output: Super Strength

    //can access internal objects
console.log(superhero['alignment']['good']); // Output: yes
console.log(superhero.alignment['good']); // Output: yes


//Object methods and this keyword

console.log(superhero.nameColors()); //Output: Iron Man: Red and Gold


// Consturctors and prototypes


    //constructor - where we store data that is unique to every "superhero"
function Superhero (name, powers, suitColor) {
    this.name = name;
    this.powers = powers;
    this.suitColor = suitColor;
};

    // prototype - accessible for each "superhero"
Superhero.prototype.introduce = function() {
    console.log("I am " + this.name+ " and I am ready to save the world!")
};

let ironman = new Superhero("Iron Man", ['Flight', 'Super Strength', 'Genius-level Intellect'], 'Red and Gold');
let batman = new Superhero('Batman', null, "Black and Grey");

ironman.introduce(); // Output: I am Iron Man and I am ready to save the world!
batman.introduce(); // Output: I am Batman and I am ready to save the world!


//Math object

    // let x = 10;
    // let y = 5;

    // let sum = Math.add(x,y);
    // let difference = Math.subtract(x,y);
    // let product = Math.multiply(x,y);
    // let quotient = Math.divide(x,y);
    // console.log(Math.PI);
    // console.log(Math.E);


    // console.log(sum + ' - ' + difference+ ' - ' + product + ' - ' + quotient)

let radius = 5;
    // area = pi * r squared
let area = Math.PI * Math.pow(radius, 2); // pow is power to, first number is base second is exponent


    // toFixed(x) gives our answer with x decimal places
console.log("Area of a circle with a radius of " + radius+ " is " + area.toFixed(2)); //Output: Area of a circle with a radius of 5 is 78.53981633974483


//Date object

let currentdate = new Date();

console.log("Current Date:" + currentdate); // Output: Current Date:Sat Jun 29 2024 11:02:24 GMT-0400 (Eastern Daylight Time)

    // format date as yyyy-mm-ddTtime
let specificdate = new Date('2024-02-10T09:00');

console.log("Specific Date/Time:" + specificdate); // Output: Specific Date/Time:Sat Feb 10 2024 09:00:00 GMT-0500 (Eastern Standard Time)

let year = currentdate.getFullYear();
let month = currentdate.getMonth() +1; //adding 1 because months are 0 based like indexes
let day = currentdate.getDate();
let hour = currentdate.getHours();
let minute = currentdate.getMinutes();
let second = currentdate.getSeconds();
let millisecond = currentdate.getMilliseconds();




console.log("Year:", year)
console.log("Month:", month)
console.log("Day:", day)
console.log("Hour:", hour)
console.log("Minute:", minute)
console.log("Second:", second)
console.log("Millisecond:", millisecond)

/* Output: (update as you refresh since it's pulling current times)
Year: 2024
Month: 6
Day: 29
Hour: 11
Minute: 6
Second: 55
Millisecond: 532*/

    //Manipulating dates

currentdate.setDate(currentdate.getDate() + 7)
console.log("Date after adding 7 days:", currentdate) //Output: Date after adding 7 days: Sat Jul 06 2024 11:10:12 GMT-0400 (Eastern Daylight Time)

currentdate.setMonth(currentdate.getMonth() + 2)
console.log("Date after adding 2 months:", currentdate) //Output: Date after adding 2 months: Fri Sep 06 2024 11:11:51 GMT-0400 (Eastern Daylight Time)