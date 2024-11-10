import pandas as pd

with open('input_list.txt', 'r') as file:
    items = file.readlines()

unique_items = pd.Series(list(set(item.strip() for item in items)))

unique_items.to_csv('result.txt', index=False, header=False)

print("Unique items have been saved to 'result.txt'.")

