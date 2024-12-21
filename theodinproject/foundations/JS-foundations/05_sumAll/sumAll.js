const sumAll = function(int1, int2) {
    let maxInt = 0
    let minInt = 0

    //check if arguments are positive integers
    for (let i=0; i <= arguments.length - 1; i++) {
        if (Number.isInteger(arguments[i]) == false || arguments[i] < 0) {
            return "ERROR"
        }
    }

    if (int1 > int2) {
        maxInt = int1
        minInt = int2
    }

    else {
        maxInt = int2
        minInt = int1
    }

    sum = 0
    for (let i = minInt; i <= maxInt; i++) {
        sum += i
    }
    return sum
};

// Do not edit below this line
module.exports = sumAll;
