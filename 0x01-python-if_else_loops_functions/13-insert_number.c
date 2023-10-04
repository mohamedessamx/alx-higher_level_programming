#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts node in sorted list
 * @head: address of head pointer
 * @number: number to insert
 * Description: insreting node in a list
 * Retrun: inserted list
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current, *prev;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;
    new_node->n = number;
    new_node->next = NULL;
    if (*head == NULL)
    {
        *head = new_node;
        return new_node;
    }
    current = *head;
    prev = NULL;
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }
    if (prev == NULL)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        new_node->next = current;
        prev->next = new_node;
    }

    return new_node;
}
