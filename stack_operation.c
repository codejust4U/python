// WAP for stack operations
// Coder: Pankaj Kori
// Date: 29-08-2022
#include <stdio.h>
#include <stdlib.h>
#define size 4
int top = -1, inp_array[size], choice, x, i;
void push();
void pop();
void display();

void main()
{
    system("cls");
    while (1)
    {
        printf("Operations:");
        printf("\n 1.Push the elements \n 2.Pop the elements \n 3.Display \n 4.Exit");
        printf("\nEnter the choice ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            push();
            break;
        case 2:
            pop();
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
        default:
            printf("\n Invalid choice.\n");
        }
    }
}
void push()
{
    if (top == size - 1)
    {
        printf("\nOverflow..\n");
    }
    else
    {
        printf("\nEnter elements to be inserted in stack:\n");
        scanf("%d", &x);
        top = top + 1;
        inp_array[top] = x;
    }
}
void pop()
{
    if (top == -1)
    {
        printf("\nUnderflow..\n");
    }
    else
    {
        printf("\nElement popped: %d\n", inp_array[top]);
        top = top - 1;
    }
}
void display()
{
    if (top == -1)
    {
        printf("\nUnderflow..\n");
    }
    else
    {
        printf("\nElements in stack: \n");
        for (i = top; i >= 0; --i)
        {
            printf("%d\n", inp_array[i]);
        }
    }
}

