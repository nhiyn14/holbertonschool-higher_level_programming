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

	if (head == NULL)
		return (NULL);
	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current->n > number)
	{
		*head = new;
		new->next = current;
		return (new);
	}
	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	return (new);
}
