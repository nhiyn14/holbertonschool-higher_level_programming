#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
  * check_cycle - check if cycle exists
  * @list: list to be checked
  * Return: 0 if no cycle, 1 if there is
  */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	if (list->next == NULL)/*only 1 node*/
		return (0);

	slow = list;
	fast = list;

	while (slow->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == NULL || fast == NULL)/*both meet end of list*/
			return (0);
		if (slow == fast)/*both arrive at same node*/
			return (1);
	}

	return (0);
}
