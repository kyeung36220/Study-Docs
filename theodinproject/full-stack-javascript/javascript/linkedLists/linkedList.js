class LinkedList {
    constructor() {
        this.head = null
    }

    getSize() {
        let size = 0
        let currentNode = this.head
        if (this.head === null) {
            return 0
        }
        while (currentNode.getNextNode != null) {
            size += 1
            currentNode = currentNode.getNextNode
        }

        return size + 1 // adding last node
    }
    
    getHead() {
        return this.head
    }

    getTail() {
        let currentNode = this.head

        if (this.head === null) {
            return null
        }

        while (currentNode.getNextNode != null) {
            currentNode = currentNode.getNextNode
        }
        return currentNode
    }

    getNodeAtIndex(index) {
        let currentIndex = 0
        let currentNode = this.head

        if (this.head === null) {
            return null
        }

        while (currentIndex < index) {
            if (currentNode.getNextNode === null) {
                return null
            }

            currentNode = currentNode.getNextNode
            currentIndex += 1
        }
        return currentNode
    }

    popElement() {
        let previousNode = null
        let currentNode = this.head

        if (this.head === null) {
            return null
        }

        while (currentNode.getNextNode != null) {
            previousNode = currentNode
            currentNode = currentNode.getNextNode
        }
        previousNode.setNextNode = null
    }

    doesListContain(value) {
        let currentNode = this.head

        if (this.head === null) {
            return null
        }

        while (currentNode.getNextNode != null && currentNode.value != value) {
            currentNode = currentNode.getNextNode
        }

        if (currentNode.value != value) {
            return false
        }

        return true
    }

    findValueIndex(value) {
        let index = 0
        let currentNode = this.head

        if (this.head === null) {
            return null
        }

        while (currentNode.getNextNode != null && currentNode.value != value) {
            currentNode = currentNode.getNextNode
            index += 1
        }

        if (currentNode.value != value) {
            return null
        }

        return index
    }

    toString() {
        let currentNode = this.head
        let string = ""

        if (this.head === null) {
            return "List is empty"
        }

        while (currentNode.getNextNode != null) {
            string = string + `( ${currentNode.value} ) -> `
            currentNode = currentNode.getNextNode
        }

        string = string + `( ${currentNode.value} ) -> null`
        return string
    }

    append(value) {
        let currentNode = this.head
        if (this.head === null) {
            this.head = new Node(value, null)
            return
        }

        while (currentNode.getNextNode != null) {
            currentNode = currentNode.getNextNode
        }

        currentNode.setNextNode = new Node(value, null)
        return
    }

    prepend(value) {
        let newNode = new Node(value, this.head)
        this.head = newNode
    }

    insertAt(value, index) {
        let currentIndex = 0
        let previousNode = null
        let currentNode = this.head
        if (this.head === null) {
            return "Index does not exist"
        }

        while (currentIndex < index) {
            if (currentNode.getNextNode === null && currentIndex < index) {
                return "Index too far ahead"
            }
            previousNode = currentNode
            currentNode = currentNode.getNextNode
            currentIndex += 1
        }

        let nextNode = previousNode.getNextNode
        previousNode.setNextNode = new Node(value, nextNode)
    }

    removeAt(index) {
        let previousNode = null
        let currentIndex = 0
        let currentNode = this.head

        if (this.head === null) {
            return "Index does not exist"
        }

        while (currentIndex < index) {
            if (currentNode.getNextNode === null && currentIndex < index) {
                return "Index too far ahead"
            }
            previousNode = currentNode
            currentNode = currentNode.getNextNode
            currentIndex += 1
        }

        previousNode.setNextNode = currentNode.getNextNode
    }

}

class Node {
    constructor(value = null, nextNode = null) {
        this.value = value
        this.nextNode = nextNode
    }

    get getValue() {
        return this.value
    }

    get getNextNode() {
        return this.nextNode
    }

    set setValue(number) {
        this.value = number
    } 

    set setNextNode(node) {
        this.nextNode = node
    }
}


const list = new LinkedList();

list.append("dog");
list.prepend("cat");
list.append("parrot");
list.append("hamster");
list.append("snake");
list.prepend("turtle");
list.insertAt("dragon", 3)
list.insertAt("pig", 3)

console.log(list.toString());

list.removeAt(2)

console.log(list.toString());
