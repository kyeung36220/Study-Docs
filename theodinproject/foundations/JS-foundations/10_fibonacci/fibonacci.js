const fibonacci = function(int) {
    if (int < 0) {
        return "OOPS"
    }
    else if (int == 0) {
        return 0
    }
    else if (int == 1) {
        return 1
    }

    fib = [0, 1]
    for(i = 2; i <= int; i++) {
        currentNumber = fib[i-2] + fib[i-1]
        fib.push(currentNumber)
    }
    return fib[int]
};

// Do not edit below this line
module.exports = fibonacci;
