import requests

def createCore(p_core_name):
    """
    Create a new Solr core with the given name.
    
    Args:
    - p_core_name (str): The name of the core to be created.
    
    Example Usage:
    createCore("newCore")
    """
    # Base URL for the Solr admin cores API
    solr_url = 'http://localhost:8983/solr/admin/cores'

    # Parameters for creating the core
    params = {
        'action': 'CREATE',
        'name': p_core_name
    }

    try:
        # Send a GET request to create the core
        response = requests.get(solr_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            print(f"Core '{p_core_name}' created successfully!")
        else:
            print(f"Failed to create core. Status Code: {response.status_code}, Reason: {response.text}")

    except Exception as e:
        print(f"An error occurred while creating the core: {e}")

# Example usage
createCore("newCore")
