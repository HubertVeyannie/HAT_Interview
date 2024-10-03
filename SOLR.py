import datetime
import pandas as pd
import pysolr

df = pd.read_csv("Employee_Sample_Data_1.csv", encoindg='ISO-8859-1')

def convert_date(date_str):
    if pd.isna(date_str):
        return None
    try:
        return datetime.datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%dT00:00:00Z')
    except ValueError:
        print(f"Error converting date: {date_str}")
        return None

solr = pysolr.Solr('http://localhost:8983/solr/employee', always_commit=True)

documents = []

for _, row in df.iterrows():
    document = {
        "id": str(row['Employee ID']),  
        "name": row['Full Name'],
        "position": row['Job Title'],
        "department": row['Department'],
        "business_unit": row['Business Unit'],
        "gender": row['Gender'],
        'ethnicity': row['Ethnicity'],
        "age": row['Age'],
        "hiring_date": row["Hire Date"],
        "salary": row['Annual Salary'],
        "bonus": row['Bonus %'],
        "country": row['Country'],
        "city": row['City'],
        "exit_date": convert_date(row['Exit Date'])  # Convert the exit date
    }
    documents.append(document)

solr.add(documents)

results = solr.search('*:*')
print(f"Number of documents indexed: {results.hits}")
