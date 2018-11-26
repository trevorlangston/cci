#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node * next;
} node_t;

void print_list(node_t *head)
{
    node_t *current = head;
    while (current != NULL)
    {
        printf("%d ", current->val);
        current = current->next;
    }
}

int main(int argc, char *argv[])
{
    node_t *head;
    node_t *current;

    head = malloc(sizeof(node_t));
    current = head;

    head->val = 0;

    // insert some elements into list
    for (int i = 1; i < 10; i++)
    {
        current->next = malloc(sizeof(node_t));
        current->next->val = i;
        current = current->next;
        current->next = NULL;
    }

    print_list(head);

    return 0;
}
