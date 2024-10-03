import pysolr

def getEmpCount(p_core_name):
    try:
        solr_url = f'http://localhost:8983/solr/{p_core_name}'
        solr = pysolr.Solr(solr_url, always_commit=True)

        query = "*:*"  

        results = solr.search(query, rows=0)

        print(f"Total number of documents (employees) in '{p_core_name}': {results.hits}")

        return results.hits  

    except Exception as e:
        print(f"Error getting employee count from Solr: {e}")
        return None 

# Example usage
getEmpCount("Hash_HubertVeyannie") 
