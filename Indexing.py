import csv
import pysolr

def indexData(p_core_name, p_exclude_column):
    solr_url = f'http://localhost:8983/solr/{p_core_name}'
    solr = pysolr.Solr(solr_url, always_commit=True)

    file_path = 'Employee_Sample_Data_1.csv'
    documents = []

    with open(file_path, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            document = {key: value for key, value in row.items() if key not in p_exclude_column}
            documents.append(document)

    solr.add(documents)
    print(f"Successfully indexed {len(documents)} documents to the core '{p_core_name}'")

# Example usage
indexData("Hash_5772", ["Gender"]) 
