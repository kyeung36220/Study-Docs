const reverseString = function(string) {
    length = string.length - 1;
    stringContainer = "";
    for (let i=0; i <= length; i++) {
        stringContainer = stringContainer.concat(string[length - i]);
    }
    return stringContainer;
};

// Do not edit below this line
module.exports = reverseString;
