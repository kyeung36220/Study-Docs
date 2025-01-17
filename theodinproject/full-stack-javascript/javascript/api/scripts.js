const img = document.querySelector('img');
const button = document.querySelector('button')
const input = document.querySelector('input')

button.addEventListener("click", async function getGif() {
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/translate?api_key=v92tE3wdXu2fBC1HKSpPWEJHnVuNtvm9&s=${input.value}`, {mode: 'cors'})
        const gifData = await response.json()
        console.log(gifData)
    
        if (gifData.data.images.original.url === "") {
            alert("No Gif Found")
            return
        }
        img.src = gifData.data.images.original.url;
    } catch(err) {
        console.log(err)
        alert("An error has occured")
    }
})