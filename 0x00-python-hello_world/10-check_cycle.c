#include "lists.h"
/**
 * check_cycle - function checks if a linked list has a cycle in it
 * @list: the linked list to be checked
 *
 * Return: 0 if no cycle found and 1 if found
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
