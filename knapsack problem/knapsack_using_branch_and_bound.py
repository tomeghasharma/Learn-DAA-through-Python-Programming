# Program for Knapsack problem using branch and bound
class Item:
    def __init__(self, weight, value, index):
        self.weight = weight  # Weight of the item
        self.value = value  # Value of the item
        self.ratio = value / weight  # Value-to-weight ratio for sorting
        self.index = index  # Index of the item


def knapsack_branch_and_bound(items, max_weight):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    # Function to calculate the upper bound of a node
    def bound(node, current_weight, current_value):
        if current_weight > max_weight:
            return 0
        bound_value = current_value
        bound_weight = current_weight
        while node < len(items) and bound_weight + items[node].weight <= max_weight:
            bound_value += items[node].value
            bound_weight += items[node].weight
            node += 1
        if node < len(items):
            bound_value += (max_weight - bound_weight) * items[node].ratio
        return bound_value

    # Recursive branch and bound algorithm with item tracking
    def branch_and_bound(node, current_weight, current_value, selected_items):
        nonlocal max_value, selected_items_final
        if current_weight <= max_weight and current_value > max_value:
            max_value = current_value
            selected_items_final = selected_items[:]
        if node >= len(items) or bound(node, current_weight, current_value) <= max_value:
            return
        # Exclude current item
        branch_and_bound(node + 1, current_weight, current_value, selected_items)
        # Include current item
        selected_items.append(items[node].index)
        branch_and_bound(node + 1, current_weight + items[node].weight, current_value + items[node].value,
                         selected_items)
        selected_items.pop()  # Backtrack to remove the current item

    max_value = 0
    selected_items_final = []
    branch_and_bound(0, 0, 0, [])  # Start the branch and bound search with an empty selected_items list
    return max_value, selected_items_final


if __name__ == "__main__":
    num_items = int(input("Enter the number of items: "))
    items = []
    for i in range(num_items):
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        value = int(input(f"Enter the value of item {i + 1}: "))
        items.append(Item(weight, value, i + 1))  # Include the index of the item

    max_weight = int(input("Enter the maximum weight capacity of the knapsack: "))

    max_value, selected_items = knapsack_branch_and_bound(items, max_weight)

    print(f"Maximum value for knapsack of capacity {max_weight}: {max_value}")
    print("Selected items:", selected_items)
""""
output:
Enter the number of items: 3
Enter the weight of item 1: 10
Enter the value of item 1: 60
Enter the weight of item 2: 20
Enter the value of item 2: 100
Enter the weight of item 3: 30
Enter the value of item 3: 120
Enter the maximum weight capacity of the knapsack: 50
Maximum value for knapsack of capacity 50: 220
Selected items: [2, 3]
"""