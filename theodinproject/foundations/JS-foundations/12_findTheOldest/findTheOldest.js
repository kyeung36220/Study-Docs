const findTheOldest = function(arr) {
    arrCopy = arr.slice()
    ages = arrCopy.map((person) => person.yearOfDeath !== undefined ? (person.yearOfDeath - person.yearOfBirth) : (new Date().getFullYear() - person.yearOfBirth))

    maxAge = 0
    maxAgeIndex = undefined
    for (i = 0; i <= ages.length; i ++) {
        if (ages[i] > maxAge) {
            maxAge = ages[i]
            maxAgeIndex = i
        }
    }
    return arr[maxAgeIndex]
};
// Do not edit below this line
module.exports = findTheOldest;
