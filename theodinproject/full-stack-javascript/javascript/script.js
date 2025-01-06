function makeAdding (firstNumber) {
    // "first" is scoped within the makeAdding function
    const first = firstNumber;
    return function resulting (secondNumber) {
      // "second" is scoped within the resulting function
      const second = secondNumber;
      return first + second;
    }
  }
  // but we've not seen an example of a "function"
  // being returned, thus far - how do we use it?
  
  const add5 = makeAdding(5);
  console.log(makeAdding(5)(2)) // logs 7
  
  const obj = { a: 1, b: 2 };
const { a, b } = obj;
// This creates two variables, a and b,
// which are equivalent to
// const a = obj.a;
// const b = obj.b;

const array = [1, 2, 3, 4, 5];
const [ zerothEle, firstEle ] = array;
console.log(zerothEle)

function createUser (name) {
    const discordName = "@" + name;
  
    let reputation = 0;
    const getReputation = () => reputation;
    const giveReputation = () => reputation++;
  
    return { name, discordName, getReputation, giveReputation };
  }
  
  const josh = createUser("josh");
  josh.giveReputation();
  josh.giveReputation();
  
  console.log({
    discordName: josh.discordName,
    reputation: josh.getReputation()
  });

function createPlayer (name, level) {
const user = createUser(name);

const increaseLevel = () => ++level;
return Object.assign({}, user, { increaseLevel });
}

const player1 = createPlayer(`steve`, 1)
console.log(player1.increaseLevel())
console.log(player1)

function outer() {
    const outerVar = 'Hey I am the outer Var';
  
    function inner() {
      const innerVar = "hey I am an inner var";
      console.log(innerVar); // Output: "hey I am an inner var"
      console.log(outerVar); // Output: "Hey I am the outer Var"
    }
  
    return inner; // Return the inner function
  }
  
  const myInnerFunc = outer(); // Get the inner function
  myInnerFunc(); 