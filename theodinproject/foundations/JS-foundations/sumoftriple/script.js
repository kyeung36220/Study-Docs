function sumofTripledEvens(arr) {
    let adjustedArr = arr

    //filtering
    function isEven(num) {
        return num % 2 == 0;
    }
    adjustedArr = adjustedArr.filter(isEven)

    //mapping
    function triple(num) {
        return num * 3
    }
    adjustedArr = adjustedArr.map(triple)

    //reducing
    function reducer(total, currentItem) {
        return total + currentItem;
    }
    adjustedArr = adjustedArr.reduce(reducer, 0)

    return adjustedArr
}


console.log(sumofTripledEvens([1,2,3,4,5]))