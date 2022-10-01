#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node *next;
} *head;

void initialize(){
    head = NULL;
}

/* Function to insert a new node into the linked list */
void insert(int num) {
    struct node* newNode = (struct node*) malloc(sizeof(struct node));
    newNode->data  = num;
    newNode->next = head;
    head = newNode;
}

/* Function to get the length of the Linked List */
int getLength(struct node *head){
    int length =0;
    while(head != NULL){
        head = head->next;
        length++;
    }
    return length;
}

int main() {
    initialize();

    /* Creating a linked List*/
    insert(1); 
    insert(2);
    insert(3);
    insert(4);
    insert(5);

    /* Printing length of the Linked List */
    printf("\nLinked List Length : %d", getLength(head));

    return 0;
}
