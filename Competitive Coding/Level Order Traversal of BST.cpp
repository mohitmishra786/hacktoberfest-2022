/*
Level Order Binary Tree Traversal Using Queue
At starting no node is visited, so we push the root node in Queue
and and mark the Root node as visited and then push all the child node of 
the root node and then pop first element from the queue, and we keep doing it
until our queue is not empty. 

Time Complexity O(n) 
Space Complexity O(n) 
where n is the number of elements in our BST

*/

#include<bits/stdc++.h>
using namespace std;

// A Binary Tree Node
struct Node {
    int data;
    struct Node *left, *right;
};
 
// Level order traversal of Binary Tree
void printLevelOrder(Node* root)
{
    // Base Case when we don't have any elements in tree
    if (root == NULL)
        return;
 
    // Create an queue for level order traversal
    queue<Node*> q;
 
    // Enqueue Root and initialize height
    q.push(root);
 
 //the while loop will keep running till we have visited all the elements of the BST
 // Or we can say that till the queue is not empty.
    while (q.empty() == false) {
        /* Print the first node which is present in the queue and then pop that element
         Because it is visited. */
        Node* node = q.front();
        cout << node->data << " ";
        q.pop();
 
        //If the left child of the visited element exits, then enqueu that element
        if (node->left != NULL)
            q.push(node->left);
 
        //If the right child of the visited element exits, then enqueu that element
        if (node->right != NULL)
            q.push(node->right);
    }
}
 
// Utility function to create a new tree node
Node* newNode(int data)
{
    Node* temp = new Node;
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}
 
// Driver program to test above functions
int main()
{
    // Let us create binary tree shown in above diagram
    Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
 
    cout << "Level Order traversal of binary tree is \n";
    printLevelOrder(root);
    return 0;
}