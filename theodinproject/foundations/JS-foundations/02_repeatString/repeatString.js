const repeatString = function(string, num) {
    if (num < 0) {
        return "ERROR";
    }
    stringContainer = "";
    for (let i=0; i < num; i++) {
        stringContainer = stringContainer.concat(string);
    }
    return stringContainer;

};

// Do not edit below this line
module.exports = repeatString;
