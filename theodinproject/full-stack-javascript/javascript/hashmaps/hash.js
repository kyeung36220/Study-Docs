class Hashmap {
    constructor(capacity = 16, loadCapacity = 0.75) {
        this.buckets = []
        this.capacity = capacity
        this.loadCapacity = loadCapacity
        this.usedCapacity = 0

        for (let i = 0; i < capacity; i++) {
            this.buckets.push(null)
        }
    }

    hash(key) {
        let hashCode = 0;
            
        const primeNumber = 31;
        for (let i = 0; i < key.length; i++) {
            hashCode = primeNumber * hashCode + key.charCodeAt(i);
        }
        
        return hashCode;
        }  
    
    set(key, value) {
        if ((this.usedCapacity / this.capacity) >= this.loadCapacity) {
            this.doubleCapacity()
        }

        const hash = this.hash(key)
        const bucket = Math.floor(hash % this.capacity)

        if (bucket < 0 || bucket >= this.buckets.length) {
            throw new Error("Trying to access index out of bounds");
        }

        if (this.buckets[bucket] === null) {
            this.buckets[bucket] = new Node(key, hash, value, null)
            this.usedCapacity += 1
            return
        }

        let currentNode = this.buckets[bucket]
        while (currentNode.getNextNode != null) {
            if (currentNode.getHashedKey === hash) {
                currentNode.setValue = value
                return
            }
            currentNode = currentNode.getNextNode
        }

        if (currentNode.getHashedKey === hash) {
            currentNode.setValue = value
            return
        }
        else {
            currentNode.setNextNode = new Node(key, hash, value, null)
        }
    }

    doubleCapacity() {
        const newBucketsArray = []
        for (let i = 0; i < (this.capacity * 2); i++) {
            newBucketsArray.push(null)
        }
        for (let i = 0; i < this.capacity; i++) {
            if (this.buckets[i] != null) {
                if (i < 0 || i >= this.buckets.length) {
                    throw new Error("Trying to access index out of bounds");
                }
    
                newBucketsArray[Math.floor(this.buckets[i].getHashedKey % (this.capacity * 2))] = this.buckets[i]
            }
        }
        this.capacity = this.capacity * 2
        this.buckets = newBucketsArray
    }

    get(key) {
        const hash = this.hash(key)
        const bucket = Math.floor(hash % this.capacity)

        if (bucket < 0 || bucket >= this.buckets.length) {
            throw new Error("Trying to access index out of bounds");
        }

        if (this.buckets[bucket] === null) {
            return null
        }

        let currentNode = this.buckets[bucket]
        while (currentNode.getNextNode != null) {
            if (currentNode.getHashedKey === hash) {
                return currentNode.getValue
            }
            currentNode = currentNode.getNextNode
        }

        if (currentNode.getHashedKey === hash) {
            return currentNode.getValue
        }
        else {
            return null
        }
    }

    has(key) {
        const hash = this.hash(key)
        const bucket = Math.floor(hash % this.capacity)

        if (bucket < 0 || bucket >= this.buckets.length) {
            throw new Error("Trying to access index out of bounds");
        }

        if (this.buckets[bucket] === null) {
            return false
        }

        let currentNode = this.buckets[bucket]
        while (currentNode.getNextNode != null) {
            if (currentNode.getHashedKey === hash) {
                return true
            }
            currentNode = currentNode.getNextNode
        }

        if (currentNode.getHashedKey === hash) {
            return true
        }
        else {
            return false
        }
    }

    remove(key) {
        const hash = this.hash(key)
        const bucket = Math.floor(hash % this.capacity)

        if (bucket < 0 || bucket >= this.buckets.length) {
            throw new Error("Trying to access index out of bounds");
        }

        if (this.buckets[bucket] === null) { // if bucket empty
            return false
        }

        if (this.buckets[bucket].getNextNode === null) { // if bucket only has one item
            this.buckets[bucket] = null
            return
        } 

        let currentNode = this.buckets[bucket]
        let previousNode = null
        while (currentNode.getNextNode != null) { // if bucket has multiple items
            if (currentNode.getHashedKey === hash) {
                previousNode.setNextNode = currentNode.getNextNode
                return true
            }
            previousNode = currentNode
            currentNode = currentNode.getNextNode
        }

        if (currentNode.getHashedKey === hash) {
            previousNode.setNextNode = currentNode.getNextNode
            return true
        }
        else {
            return false
        }
    }

    length() {
        let total = 0

        for (let i = 0; i < this.buckets.length; i++) {
            if (i < 0 || i >= this.buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }

            if (this.buckets[i] != null) {
                total += getAllNodesInLinkedList(this.buckets[i])
            }
        }

        return total

        function getAllNodesInLinkedList(headNode) {
            let totalInBucket = 1
            let currentNode = headNode

            while (currentNode.getNextNode != null) {
                totalInBucket += 1
                currentNode = currentNode.getNextNode
            }
            return totalInBucket
        }

    }

    clear() {
        for (let i = 0; i < this.buckets.length; i++) {
            if (i < 0 || i >= this.buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }

            if (this.buckets[i] != null) {
                this.buckets[i] = null
            }
        }
    }

    keys() {
        let keys = []

        for (let i = 0; i < this.buckets.length; i++) {
            if (i < 0 || i >= this.buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }

            if (this.buckets[i] != null) {
                getAllKeysInLinkedList(this.buckets[i])
            }
        }

        return keys

        function getAllKeysInLinkedList(headNode) {
            let currentNode = headNode

            while (currentNode.getNextNode != null) {
                keys.push(currentNode.getKey)
                currentNode = currentNode.getNextNode
            }
            keys.push(currentNode.getKey)
        }
    }

    values() {
        let values = []

        for (let i = 0; i < this.buckets.length; i++) {
            if (i < 0 || i >= this.buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }

            if (this.buckets[i] != null) {
                getAllValuesInLinkedList(this.buckets[i])
            }
        }

        return values

        function getAllValuesInLinkedList(headNode) {
            let currentNode = headNode

            while (currentNode.getNextNode != null) {
                values.push(currentNode.getValue)
                currentNode = currentNode.getNextNode
            }
            values.push(currentNode.getValue)
        }
    }

    entries() {
        let entries = []

        for (let i = 0; i < this.buckets.length; i++) {
            if (i < 0 || i >= this.buckets.length) {
                throw new Error("Trying to access index out of bounds");
            }

            if (this.buckets[i] != null) {
                getAllEntriesInLinkedList(this.buckets[i])
            }
        }

        return entries

        function getAllEntriesInLinkedList(headNode) {
            let currentNode = headNode

            while (currentNode.getNextNode != null) {
                entries.push([currentNode.getKey, currentNode.getValue])
                currentNode = currentNode.getNextNode
            }
            entries.push([currentNode.getKey, currentNode.getValue])
        }
    }
}



class Node {
    constructor(key = null, hashedKey = null, value = null, nextNode = null) {
        this.key = key
        this.hashedKey = hashedKey
        this.value = value
        this.nextNode = nextNode
    }

    get getKey() {
        return this.key
    }

    get getHashedKey() {
        return this.hashedKey
    }

    get getValue() {
        return this.value
    }

    get getNextNode() {
        return this.nextNode
    }

    set setKey(newKey) {
        this.key = newKey
    }

    set setHashedKey(hashedKey) {
        this.hashedKey = hashedKey
    }

    set setValue(string) {
        this.value = string
    } 

    set setNextNode(node) {
        this.nextNode = node
    }
}

const test = new Hashmap(16, 0.75)
test.set('apple', 'red')
test.set('banana', 'yellow')
test.set('carrot', 'orange')
test.set('dog', 'brown')
test.set('elephant', 'gray')
test.set('frog', 'green')
test.set('grape', 'purple')
test.set('hat', 'black')
test.set('ice cream', 'white')
test.set('jacket', 'blue')
test.set('kite', 'pink')
test.set('lion', 'golden')
test.set('moon', 'silver')
console.log(test.entries())
