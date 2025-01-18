function mergeSort(array) {

    if (array.length <= 1) {
        return array
    }

    let midPoint = Math.floor(array.length / 2)

    let left = mergeSort(array.slice(0, midPoint))
    let right = mergeSort(array.slice(midPoint, array.length))

    return merge(left, right)
}

function merge(left, right) {
    let sortedArray = []

    while (left.length && right.length) {
        if (left[0] < right[0]) {
            sortedArray.push(left.shift())
        }
        else {
            sortedArray.push(right.shift())
        }
    }
    return [...sortedArray, ...left, ...right]
}

console.log(mergeSort([3, 2, 1, 13, 8, 5, 0, 1]))