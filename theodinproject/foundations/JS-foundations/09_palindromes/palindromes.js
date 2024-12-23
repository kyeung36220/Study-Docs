allowed = `abcdefghijklmnopqrstuvwxyz1234567890`

const palindromes = function (str) {
    strCopy = str.toLowerCase().split('').filter(item => allowed.includes(item)).join('')
    reversed = strCopy.split('').reverse().join('')
    if (reversed === strCopy) {
        return true
    }
    else {
        return false
    }
};

// Do not edit below this line
module.exports = palindromes;
