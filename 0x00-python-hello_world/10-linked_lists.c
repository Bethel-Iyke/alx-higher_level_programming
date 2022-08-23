#include "lists.h"

/**
 * check_cycle - checks if cycle exist or not
 * list: linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
listint_t *current = list->next;
listint_t *post_current = current->next;
if (current != NULL && post_current != NULL)
return (1);
else
return (0);
}
