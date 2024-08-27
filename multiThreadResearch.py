from concurrent.futures import ThreadPoolExecutor

def search_state(objects_dict, textToFind):
    # Function to search for the state with name "xxx"
    def search_state_in_object(obj_data):
        for state in obj_data['states']:
            if state['name'] in textToFind:
                return state
        return None

    # Use ThreadPoolExecutor for concurrent searching
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(search_state_in_object, obj_data) for obj_data in objects_dict.values()]
        found_state = next((future.result() for future in futures if future.result() is not None), None)

    return found_state
