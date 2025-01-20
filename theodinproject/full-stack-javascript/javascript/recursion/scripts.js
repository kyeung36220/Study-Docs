function sumRange(number) {
    if (number === 1) {
        return 1
    }
    return number + sumRange(number - 1)
}

function power(base, exponent) {
    if (exponent === 0) {
        return 1
    }
    return base * power(base, exponent - 1)
}

function factorial(number) {
    if (number === 1) {
        return 1
    }
    return number * factorial(number - 1)
}

function sumOfAllMultiples3And5(number) {
    let sum = 0
    let max = number - 1
    findOut(max)

    function findOut(max) {
        if (max === 0) {
            return
        }
        else {
            if (max % 3 === 0 || max % 5 === 0) {
                sum += max
            }
            findOut(max - 1)
        }
    }
    return sum
}

function evenFibBelowMax(max) {
    let sum = 0
    let fibArray = [0,1]
    findNumbers(max)
    
    function findNumbers(max) {
        let number = fibArray[fibArray.length - 1] + fibArray[fibArray.length - 2]
        if (number >= max) {
            return
        }
        else {
            if (number % 2 === 0) {
                sum += number
            }
            fibArray.push(number)
            findNumbers(max)
        }
    }
    return sum
}

let divideBy = 2
function largestPrimeFactor(number) {
    let largestPrime = 0
    let listOfFactors = []

    for (let i = 2; i < number; i++) {
        if (isPrime(i) === true && (number % i) === 0) {
            console.log(i)
            listOfFactors.push(i)
        }
    }

    return listOfFactors[listOfFactors.length - 1]

    function isPrime(numberInQuestion) {

        let sqroot = Math.sqrt(numberInQuestion)
        for (let i = 2; i < sqroot; i++) {
            if (numberInQuestion % i === 0) {
                return false
            }
        }
        return true

    }
}

console.log(largestPrimeFactor(600851475143))