#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - a function checks if a linked list is a palindrome.
 * @head: list to be checked
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *check;
	int i = 1, length = 0, half;
	int *array;

	if (head == NULL || *head == NULL)
		return (1);
	check = *head;

	while (check != NULL)
	{
		length++;
		check = check->next;
	}

	check = *head;
	array = malloc(sizeof(*array) * length);
	array[0] = check->n;
	while (check->next != NULL)
	{
		check = check->next;
		array[i] = check->n;
		i++;
	}
	i = 0;
	half = length / 2;
	while (i <= half)
	{
		if (array[i] != array[length - 1])
		{
			free(array);
			return (0);
		}
		length--;
		i++;
	}
	free(array);
	return (1);
}
