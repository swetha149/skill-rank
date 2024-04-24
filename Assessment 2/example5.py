import json

def add_batter_to_donut(json_file, donut_name, batter_id, batter_type):
    # Open the file in read mode and load the JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Iterate over each item in the JSON data
    for item in data:
        # Check if the item is the specified donut
        if item.get("name") == donut_name and item.get("type") == "donut": 
            # Append a new batter type to the "batters" list
            item["batters"]["batter"].append({"id": batter_id, "type": batter_type})
            break

    # Open the file in write mode and write the modified JSON data
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

# Usage example
add_batter_to_donut('ex5.json', 'Old Fashioned', '1005', 'Tea')
