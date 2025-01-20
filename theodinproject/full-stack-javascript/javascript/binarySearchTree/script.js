class Node {
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


class Tree {
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
}

const prettyPrint = (node, prefix = "", isLeft = true) => {
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

const tree = new Tree([128, 872, 691, 404, 203, 999, 293, 264, 41, 799, 438, 265, 807, 665, 552, 655, 735, 43, 209, 802] )
prettyPrint(tree.getRoot)