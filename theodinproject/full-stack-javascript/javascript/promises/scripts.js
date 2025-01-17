let p = new Promise((resolve, reject) => {
    let a = 1 + 1
    if (a == 2) {
        resolve("Success")
    }
    else {
        reject("Failed")
    }
})

p.then((message) => {
    console.log("This is in the then " + message)
}).catch((message) => {
    console.log("This is in the catch " + message)
}).then((message) => {
    console.log("yo " + message)
})

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  delay(3000).then(() => alert('runs after 3 seconds'));
