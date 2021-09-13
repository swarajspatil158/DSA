const price = 1200;
const final_price =price +  price*20.6/100
console.log(final_price)

// ---------------------------------------------
const temp_c = 40
const temp_f = (temp_c * 9/5) + 32
console.log(temp_f)

// ---------------------------------------------

let number1 = 5;
let number2 = 3;

number2=number1+number2 // 8
number1=number2 - number1 // 3
number2=number2-number1 // 5

console.log(number1); // Should show 3
console.log(number2); // Should show 5


// ---------------------------------------------

var obj = {
    name:"SwARAJ",
    
    age : 20,
    details() {
        return `name: ${this.name} age: ${this.age} lang: ${this.language}`
    }
}

console.log(obj.details());
console.log(obj.language);
obj.language = "Python";

// ---------------------------------------------------

const aurora = {
    name: "Aurora",
    health: 150,
    strength: 25,
  
    // Return the character description
    describe() {
      return `${this.name} has ${this.health} health points and ${this
        .strength} as strength`;
    }
  };
  
  console.log(aurora.describe());
