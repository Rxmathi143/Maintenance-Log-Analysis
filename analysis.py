from bisect import bisect_left, bisect_right

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def process_maintenance_logs():
    # User input for maintenance logs
    n = int(input("Enter number of maintenance records: "))
    maintenance_logs = []
    for _ in range(n):
        equipment_id = int(input("Enter equipment ID: "))
        date = input("Enter maintenance date (YYYY-MM-DD): ")
        cost = int(input("Enter maintenance cost: "))
        maintenance_logs.append((equipment_id, date, cost))
    
    # User input for queries
    q = int(input("Enter number of queries: "))
    queries = []
    for _ in range(q):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        queries.append((start_date, end_date))
    
    # Extract unique dates and sort them
    unique_dates = sorted(set(date for _, date, _ in maintenance_logs))
    date_to_index = {date: i + 1 for i, date in enumerate(unique_dates)}
    
    # Initialize Fenwick Tree
    fenwick_tree = FenwickTree(len(unique_dates))
    
    # Add maintenance costs to Fenwick Tree
    for _, date, cost in maintenance_logs:
        fenwick_tree.update(date_to_index[date], cost)
    
    # Process queries
    result = []
    for start_date, end_date in queries:
        left_idx = bisect_left(unique_dates, start_date) + 1
        right_idx = bisect_right(unique_dates, end_date)
        
        if left_idx > right_idx or left_idx > len(unique_dates):
            result.append(0)  # No valid range
        else:
            result.append(fenwick_tree.range_query(left_idx, right_idx))
    
    print("Total maintenance costs for each query:", result)

# Run the function
process_maintenance_logs()
