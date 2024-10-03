import pysolr

def delEmpById(p_core_name, p_employee_id):
    try:
        solr_url = f'http://localhost:8983/solr/{p_core_name}'
        solr = pysolr.Solr(solr_url, always_commit=True)

        query = f"Employee_ID:{p_employee_id}"

        solr.delete(q=query)

        print(f"Successfully deleted the document with Employee ID '{p_employee_id}' from core '{p_core_name}'")

    except Exception as e:
        print(f"Error deleting employee with ID '{p_employee_id}' from Solr: {e}")
        
#Example Usage
delEmpById("Hash_HubertVeyannie", "E02003")  
