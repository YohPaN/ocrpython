import json

# Sample data for a single object with states
def create_object(object_id):
    states = []
    for i in range(1, 6):
        state = {
            'code': f'State{i}',
            'price': i * 10.0,
            'description': f'State {i} description',
            'name': f'State {i} Name'
        }
        states.append(state)

    object_data = {
        'id': object_id,
        'name': f'Object {object_id}',
        'states': states
    }

    return object_data

# Create a dictionary with 100 objects
objects_dict = {f'object_{i}': create_object(i) for i in range(1, 101)}

# Save the data to a JSON file
file_path = 'objects_data.json'
with open(file_path, 'w') as json_file:
    json.dump(objects_dict, json_file, indent=4)

print(f"Data has been generated and saved to {file_path}.")
