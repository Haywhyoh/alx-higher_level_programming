#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * @number: the number to be inserted
 * @head: the sorted linked list
 *
 * Return: address of the new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp, *current;

	temp = *head;
	current = *head;
	new_node  = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	if (*head == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head =  new_node;
		return (new_node);
	}
	while(current->next)
	{
		current = current->next;
		if (current->n >= number)
		{
			new_node->n = number;
			new_node->next = current;
			temp->next = new_node;
			return (new_node);
		}
		else
		{
			temp = temp->next;
		}
	}
	new_node = add_nodeint_end(head, number);
	return(new_node);
}
