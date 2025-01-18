function fibs(number) {
    if (number <= 0) {
        return "Bruh moment"
    }
    else if (number === 1) {
        return [0]
    }
    else if (number === 2) {
        return [0, 1]
    }

    let fibsArray = [0,1]
    for (let i = 2; i < number; i++) {
        fibsArray.push(fibsArray[i-1] + fibsArray[i-2])
    }
    return fibsArray

}

function fibsRec(number) {
    console.log("This was printed recursively");
    if (number <= 0) {
        const fibsArray = []
        return fibsArray
    }
    else if (number === 1) {
        const fibsArray = []
        fibsArray.push(0)
        return fibsArray
    }
    else if (number === 2) {
        return [0,1]
    }

    const array = fibsRec(number-1)
    array.push(array[number-2] + array[number-3])
    return array



}


// console.log(fibs(8))
console.log(fibsRec(8))