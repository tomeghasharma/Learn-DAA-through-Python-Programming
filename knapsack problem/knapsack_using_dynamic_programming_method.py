# Program for Knapsack problem using Dynamic Programming
def knapSack(weight, profit, m, n):
    # Initialize a 2D array to store the maximum values
    K = [[0 for x in range(m + 1)] for x in range(n + 1)]
    # Fill in the k table
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i-1] <= j:
                # If the current item can be included, choose the maximum value
                # between including and excluding it
                K[i][j] = max(profit[i-1] + K[i - 1][j - weight[i-1]], K[i - 1][j])
            else:
                # If the current item is too heavy, exclude it
                K[i][j] = K[i - 1][j]
    print("The maximum profit is : ", K[n][m])
    # Find the selected items
    selected = []
    i, j = n, m
    while(i>0 and j>0):
        if(K[i][j] != K[i-1][j]):
            selected.append(i)
            j -= weight[i-1]
        i -= 1
    # Reverse the order of selected items
    selected.reverse()
    print("Items selected : ")
    for i in selected:
            print("item",i, end=" ")


# Input from the user
n = int(input("enter the number of elements  : "))
weight = []
profit = []
print("enter weight for", n, "elements : ")
for i in range(n):
    ele = int(input())
    weight.append(ele)
print("enter profit for", n, "elements : ")
for i in range(n):
    ele = int(input())
    profit.append(ele)
m = int(input("Enter the maximum weight capacity of the knapsack: "))
knapSack(weight, profit, m, n)

""""
output:
enter the number of elements  : 4
enter weight for 4 elements : 
2
1
3
2
enter profit for 4 elements : 
12
10
20
15
Enter the maximum weight capacity of the knapsack: 5
The maximum profit is :  37
Items selected : 
item 1 item 2 item 4 
"""