const removeFromArray = function(array) {
    let amountToRemove = arguments.length - 1;
    let arrayLength = array.length;
    for (let i=0; i <= arrayLength; i++) {
        for (let j=1; j <= amountToRemove; j++) {
            let a = array[i];
            let b = arguments[j];
            if (array[i] === arguments[j]) {
                array.splice(i,1);
                i = i - 1;
            }
        }
    }
    return array;
};

console.log(removeFromArray([1,2,3,4,5], 3, 2))
// Do not edit below this line
module.exports = removeFromArray;
