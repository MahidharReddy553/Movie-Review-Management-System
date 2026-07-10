import csv

def get_headers(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        return reader.fieldnames
    
def generate_id(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        id = list(reader)[-1].get('id')
        return str(int(id) + 1)
    
def read_csv(filename):
    with open(filename) as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)

def write_row(filename, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = get_headers(filename))
        writer.writerow(data)
        return "Row written successfully."

def write_rows(filename, data):
    headers = get_headers(filename)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = headers)
        writer.writeheader()
        writer.writerows(data)
        return "Rows written successfully."

if __name__ == '__main__':
    path = r"D:\MRS_Project\MRS_no_db\data\users.csv"
    user = {'id' : generate_id(path), 'username' : 'mdr', 'password':'mdr', 'email':'mdr@mailme.com'}
    users = read_csv(path)
    users.append(user)
    print(users)
    write_rows(path, users)