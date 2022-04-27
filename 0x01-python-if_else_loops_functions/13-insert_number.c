#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - insert a new node to the sorted list
  * @head: head
  * @number: value for n
  * Return: address of new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *hold;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	while (current->n <= number)
	{
		if (current->n <= number)
		{
			hold = current;
			current = current->next;
		}
		else
			break;
	}
	new->next = current;
	hold->next = new;
	return (new);
}
