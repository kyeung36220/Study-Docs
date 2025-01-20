export class Node {
    constructor(value) {
        this.value = value
        this.leftChild = null
        this.rightChild = null
    }

    get getValue() {
        return this.value
    }

    get getLeftChild() {
        return this.leftChild
    }

    get getRightChild() {
        return this.rightChild
    }

    set setValue(value) {
        this.value = value
    }

    set setLeftChild(node) {
        this.leftChild = node
    }

    set setRightChild(node) {
        this.rightChild = node
    }

    insert(value) {
        if (this.value === value) {
            throw new Error("Data already exists in tree")
        }
        else if(this.value > value) {
            if(this.getLeftChild != null) {
                this.getLeftChild.insert(value)
            }
            else {
                this.setLeftChild = new Node(value)
            }
        }
        else if(this.value < value){
            if(this.getRightChild != null) {
                this.getRightChild.insert(value)
            }
            else {
                this.setRightChild = new Node(value)
            }
        }
    }

    remove(node, value) {
        if (node.getLeftChild && node.getLeftChild.getValue === value) {
            if (node.getLeftChild.getLeftChild === null && node.getLeftChild.getRightChild === null ) { // 0 children
                node.setLeftChild = null
            }

            // if 1 child
            else if (node.getLeftChild.getLeftChild === null && node.getLeftChild.getRightChild != null || node.getLeftChild.getLeftChild != null && node.getLeftChild.getRightChild === null) {

                if (node.getLeftChild.getLeftChild != null){
                    node.setLeftChild = node.getLeftChild.getLeftChild
                }
                else {
                    node.setLeftChild = node.getLeftChild.getRightChild
                }
            }

            //if 2 children
            else {
                let succ = this.getSuccessor(node.getLeftChild)[0]
                let succParent = this.getSuccessor(node.getLeftChild)[1]
                node.getLeftChild.setValue = succ.getValue
                succParent.setLeftChild = null
            }

        }
        else if (node.getRightChild && node.getRightChild.getValue === value) {
            if (node.getRightChild.getLeftChild === null && node.getRightChild.getRightChild === null) { // 0 children
                node.setRightChild = null
            }

            else if (node.getRightChild.getLeftChild === null && node.getRightChild.getRightChild != null || node.getRightChild.getLeftChild != null && node.getRightChild.getRightChild === null) {

                if (node.getLeftChild.getLeftChild != null){
                    node.setRightChild = node.getRightChild.getLeftChild
                }
                else {
                    node.setRightChild = node.getRightChild.getRightChild
                }
            }

            //if 2 children
            else {
                let succ = this.getSuccessor(node.getLeftChild)[0]
                let succParent = this.getSuccessor(node.getLeftChild)[1]
                node.getRightChild.setValue = succ.getValue
                if (succ.getRightChild != null) {
                    succParent.setLeftChild = succ.getRightChild
                }
                else {
                    succParent.setLeftChild = null
                }
            }

        }

        else if (node.value === value) {
            let succ = this.getSuccessor(node)[0]
            let succParent = this.getSuccessor(node)[1]
            node.setValue = succ.getValue
            if (succ.getRightChild != null) {
                succParent.setLeftChild = succ.getRightChild
            }
            else {
                succParent.setLeftChild = null
            }
        }

        else if (node.value > value) {
            if (node.getLeftChild === null) {
                return "This item does not exist in tree"
            }
            else {
                this.remove(node.getLeftChild, value)
            }
        }
        else if (node.value < value) {
            if (node.getRightChild === null) {
                return "node item does not exist in tree"
            }
            else {
                this.remove(node.getRightChild, value)
            }
        }
    }

    getSuccessor(node) {
        let curr = node.getRightChild
        let parent = node
        while (curr !== null && curr.getLeftChild !== null) {
            parent = curr
            curr = curr.getLeftChild;
        }
        return [curr,parent];
    }
}


export class Tree {
    constructor(array) {
        this.root = null
        this.buildTree(array)
    }

    get getRoot() {
        return this.root
    }

    buildTree(array) {
        const adjustedArray = this.removeDupes(this.sort(array))
        this.root = this.createChildren(adjustedArray, 0, adjustedArray.length - 1)
    }

    sort(array) {
        let arrayCopy = array.slice().sort((a, b) => {
            const numberA = Number(a)
            const numberB = Number(b)
            if (numberA < numberB) {
                return -1;
            }
            if (numberA > numberB) {
                return 1;
            }

            return 0;
        });
        return arrayCopy
    }

    removeDupes(array) {
        let noDupeArray = []

        for (let i = 0; i < array.length; i++) {
            if (noDupeArray.includes(array[i]) === false) {
                noDupeArray.push(array[i])
            }
        }
        return noDupeArray
    }

    insert(value) {
        if (this.root) {
            this.root.insert(value)
        }
        else {
            this.root = new Node(value)
        }
    }

    remove(value) {
        if (this.root) {
            this.root.remove(this.root, value)
        }
        else {
            return "Tree does not exist"
        }
    }
    createChildren(array, start, end) {

        let midPoint = start + Math.floor((end - start) / 2)

        if (start > end) {
            return null
        }

        let root = new Node(array[midPoint])
        
        root.setLeftChild = this.createChildren(array, start, midPoint-1)

        root.setRightChild = this.createChildren(array, midPoint+1, end)

        return root
    }

    find(value) {
        if (this.root.getValue === value) {
            return this.root
        }
        else {
            return findRec(this.root, value)
        }

        function findRec(node, value) {
            if (node.getValue === value) {
                return node
            }
            else if (node.getValue < value) {
                if (node.getRightChild === null) {
                    return "Value does not exist"
                }
                else {
                    return findRec(node.getRightChild, value)
                }
                
            }
            else {
                if (node.getLeftChild === null) {
                    return "Value does not exist"
                }
                else {
                    return findRec(node.getLeftChild, value)
                }
            }
        }
    }

    levelOrder()  {
        const result = []
        const queue = []
        if (this.root === null) {
            return queue
        }

        queue.push(this.root)
        while (queue.length > 0) {
            if (queue[0].getLeftChild != null) {
                queue.push(queue[0].getLeftChild)
            }
            if (queue[0].getRightChild != null) {
                queue.push(queue[0].getRightChild)
            }
            result.push(queue[0].getValue)
            queue.shift()
        }
        return result

    }

    preorder() {
        const result = []  
        preorderRec(this.root)
        return result

        function preorderRec(root) {
            if (root === null) {
                return
            }
            result.push(root.getValue)
            preorderRec(root.getLeftChild)
            preorderRec(root.getRightChild)
        }
    }

    inorder() {
        const result = []  
        inorderRec(this.root)
        return result

        function inorderRec(root) {
            if (root === null) {
                return
            }
            inorderRec(root.getLeftChild)
            result.push(root.getValue)
            inorderRec(root.getRightChild)
        }
    }

    postorder() {
        const result = []  
        postorderRec(this.root)
        return result

        function postorderRec(root) {
            if (root === null) {
                return
            }
            postorderRec(root.getLeftChild)
            postorderRec(root.getRightChild)
            result.push(root.getValue)
        }
    }

    height(node) {
        let maxLeftHeight = 0
        let maxRightHeight = 0
        heightRec(node)
        let maxHeight = Math.max(maxLeftHeight, maxRightHeight)
        return maxHeight
        
        function heightRec(node) {
            if (node === null) {
                return
            }
            if (node.getLeftChild) {
                maxLeftHeight += 1
                heightRec(node.getLeftChild)
            }
            if (node.getRightChild) {
                maxRightHeight += 1
                heightRec(node.getRightChild)
            }

        }
    }

    depth(node) {
        const value = node.getValue
        let depthCounter = 0
        if (this.root.getValue === value) {
            return depthCounter
        }
        else {
            depthRec(this.root, value)
            return depthCounter
        }

        function depthRec(node, value) {
            if (node.getValue === value) {
                return
            }
            else if (node.getValue < value) {
                if (node.getRightChild === null) {
                    throw new Error("Value does not exist") 
                }
                else {
                    depthCounter += 1
                    return depthRec(node.getRightChild, value)
                }
                
            }
            else {
                if (node.getLeftChild === null) {
                    throw new Error("Value does not exist") 
                }
                else {
                    depthCounter += 1
                    return depthRec(node.getLeftChild, value)
                }
            }
        }
    }
}

export function isBalanced(tree) {
    let root = tree.getRoot
    let leftHeight = tree.height(root.getLeftChild)
    let rightHeight = tree.height(root.getRightChild)

    if (Math.abs(leftHeight - rightHeight) > 1) {
        return false
    }
    return true
}

export function rebalance(tree) {
    let sortedArray = tree.inorder()
    return new Tree(sortedArray)
}

export const prettyPrint = (node, prefix = "", isLeft = true) => {
    if (node === null) {
      return;
    }
    if (node.getRightChild !== null) {
      prettyPrint(node.getRightChild, `${prefix}${isLeft ? "│   " : "    "}`, false);
    }
    console.log(`${prefix}${isLeft ? "└── " : "┌── "}${node.getValue}`);
    if (node.getLeftChild !== null) {
      prettyPrint(node.getLeftChild, `${prefix}${isLeft ? "    " : "│   "}`, true);
    }
  };

