function sumRange(number) {
    if (number === 1) {
        return 1
    }
    return number + sumRange(number - 1)
}

console.log(sumRange(3))


function power(base, exponent) {
    if (exponent === 0) {
        return 1
    }
    return base * power(base, exponent - 1)
}

console.log(power(2, 3))

function factorial(number) {
    if (number === 1) {
        return 1
    }
    return number * factorial(number - 1)
}

console.log(factorial(5))
