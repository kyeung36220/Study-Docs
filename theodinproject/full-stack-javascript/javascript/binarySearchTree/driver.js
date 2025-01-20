import {Node, Tree, isBalanced, rebalance, prettyPrint } from "./script.js"

function giveArray(size, maxNumber) {
    const max = maxNumber
    const arr = []
    for (let i = 0; i < size; i++) {
        arr.push(Math.floor(Math.random() * max))
    }
    return arr
}

const tree = new Tree(giveArray(10, 100))
prettyPrint(tree.getRoot)
console.log(`Balanced? -> ${isBalanced(tree)}`)
console.log(`Level Order: ${tree.levelOrder()}`)
console.log(`Preorder: ${tree.preorder()}`)
console.log(`Inorder: ${tree.inorder()}`)
console.log(`Postorder: ${tree.postorder()}`)

tree.insert(101)
tree.insert(102)
tree.insert(103)
tree.insert(104)
tree.insert(111)

prettyPrint(tree.getRoot)
console.log(`Balanced? -> ${isBalanced(tree)}`)

const newTree = rebalance(tree)

prettyPrint(newTree.getRoot)
console.log(`Balanced? -> ${isBalanced(newTree)}`)
console.log(`Level Order: ${newTree.levelOrder()}`)
console.log(`Preorder: ${newTree.preorder()}`)
console.log(`Inorder: ${newTree.inorder()}`)
console.log(`Postorder: ${newTree.postorder()}`)

