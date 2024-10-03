import pysolr

def searchByColumn(p_core_name, p_column_name, p_column_value):
    try:
        solr_url = f'http://localhost:8983/solr/{p_core_name}'
        solr = pysolr.Solr(solr_url, always_commit=True)

        query = f"{p_column_name}:{p_column_value}"

        results = solr.search(query)

        print(f"Found {len(results)} documents matching '{p_column_name}: {p_column_value}':")
        for document in results:
            print(document)

        return results 

    except Exception as e:
        print(f"Error searching in Solr: {e}")
        return None 

# Example usage
searchByColumn("Hash_5772", "Department", "IT")  
