const theHobbit = {
    title: `The Hobbit`,
    author: `J.R.R. Tolkien`,
    pages: 295,
    read: `not read yet`,
    info() {
        return`${this.title} by ${this.author}, ${this.pages} pages, ${this.read}`
    }
}

console.log(theHobbit.info());


  
function Food(name) {
    this.name = name
}

Food.prototype.sayName = function() {
    console.log(`I am ${this.name}`)
}

function Condiment(name, condiment) {
    this.name = name;
    this.condiment = condiment;
}

Condiment.prototype.getCondiment = function() {
    console.log(`I am covered with ${this.condiment}`)
}

Object.setPrototypeOf(Condiment.prototype, Food.prototype)

const hotdog = new Condiment(`hotdog`, `ketchup`)
const rice = new Condiment(`rice`, `mustard`)

hotdog.getCondiment()
rice.sayName()


let head = {
    glasses: 100
  };
  
let table = {
    pen: 3
  };
  
let bed = {
    sheet: 1,
    pillow: 2
  };
  
let pockets = {
    money: 2000
  };

Object.setPrototypeOf(pockets, bed)
Object.setPrototypeOf(bed, table)
Object.setPrototypeOf(table, head)

console.log(pockets.glasses)

let hamster = {
    stomach: [],
  
    eat(food) {
      this.stomach =[food];
    }
  };
  
  let speedy = {};
  
  let lazy = {};
  
  Object.setPrototypeOf(speedy, hamster)
  Object.setPrototypeOf(lazy, hamster)
  // This one found the food
  speedy.eat("apple");
  alert( speedy.stomach ); // apple
  
  // This one also has it, why? fix please.
  alert( lazy.stomach ); // apple