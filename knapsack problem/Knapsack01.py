#  program for 0/1 knapsack problem using greedy method
def knapsack_greedy(n, weights, values, capacity):

    # Calculate value-to-weight ratios for each item
    value_per_weight = [(values[i] / weights[i], i) for i in range(n)]

    # Sort items by value-to-weight ratio in descending order
    value_per_weight.sort(reverse=True)

    max_value = 0  # Maximum value obtained

    for ratio, i in value_per_weight:
        if weights[i] <= capacity:
            # If the entire item can be included, add it
            print(f"item{i+1} is fully added")
            max_value += profit[i]
            capacity -= weights[i]
        else:
            # Add the fraction of the item
            print(f"Fraction of item{i+1} is added")
            max_value += capacity*ratio
            break
    print(f"Maximum profit : {max_value}")


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
capacity = int(input("Enter the maximum weight capacity of the knapsack: "))
knapsack_greedy(n, weight, profit, capacity)
