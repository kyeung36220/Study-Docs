function addItem() {
    // add item to ul with delete button
    currentItem = inputElement.value
    const item = document.createElement('li')
    item.textContent = `${currentItem}`
    list.appendChild(item)
    inputElement.value = ''

    function deleteItem() {
        list.removeChild(item)
        inputElement.focus()
    }

    const deleteButton = document.createElement('button')

    deleteButton.addEventListener("click", deleteItem)

    const span = document.createElement('span')
    deleteButton.textContent = 'Delete'
    span.appendChild(deleteButton)
    item.appendChild(span)

    inputElement.focus()
}

const addItemButton = document.querySelector(".addItem")
addItemButton.addEventListener("click", addItem)

const list = document.querySelector("ul")

const inputElement = document.querySelector('#item')


