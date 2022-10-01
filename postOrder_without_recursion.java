/*PostOrder Traversal without Recursion is more complex than InOrder and PreOrder Traversals, 
but PostOrder can be easily done using two stacks. 
Traversing Binary tree involves iterating over all the nodes of Binary Tree in a manner. 
As trees are not a part of linear data structure, 
there can be a possibility of more than 1 possible next node from a given node.*/
  
import java.util.Stack;
class PostOrderNode
{
int val;
PostOrderNode leftNode, rightNode;
public PostOrderNode(int keyVal)
{
val = keyVal;
leftNode = rightNode = null;
}
}
class Main
{
public static void iterativePostOrder (PostOrderNode rootNode)
{
Stack<PostOrderNode> stack = new Stack();
stack.push(rootNode);
Stack<Integer> out = new Stack();
while (!stack.empty())
{
PostOrderNode currentNode = stack.pop();
out.push(currentNode.val);
if (currentNode.leftNode != null) {
stack.push(currentNode.leftNode);
}
if (currentNode.rightNode != null) {
stack.push(currentNode.rightNode);
}
}
while (!out.empty()) {
System.out.print(out.pop() + " ");
}
}
public static void main(String[] args)
{
PostOrderNode rootNode = new PostOrderNode(25);
rootNode.leftNode = new PostOrderNode(35);
rootNode.rightNode = new PostOrderNode(45);
rootNode.leftNode.leftNode = new PostOrderNode(55);
rootNode.leftNode.rightNode = new PostOrderNode(65);
rootNode.rightNode.leftNode = new PostOrderNode(75);
rootNode.rightNode.rightNode = new PostOrderNode(85);
iterativePostOrder(rootNode);
}
}
