import re

def extract_table_info(sql_dump):
    tables = []
    columns = {}
    primary_keys = {}
    foreign_keys = {}

    # RegExs zum Matchen von Tabellen, statements und constraints
    table_regex = r'CREATE TABLE\s+(\w+)\s*\('
    column_regex = r'(\w+)\s+(\w+)\s*(?:.*?,|\n)'
    primary_key_regex = r'PRIMARY KEY\s*\((.*?)\)'
    foreign_key_regex = r'FOREIGN KEY\s*\((.*?)\)\s*REFERENCES\s+(\w+)\s*\((.*?)\)'

    # Tabelleerstellung, Information extraction
    table_matches = re.findall(table_regex, sql_dump, re.IGNORECASE)
    for table_match in table_matches:
        table_name = table_match.lower()
        tables.append(table_name)

        # was eine Zeile in der Tabelle bedeutet
        column_matches = re.findall(column_regex, sql_dump, re.IGNORECASE)
        table_columns = [(column_name.lower(), column_type) for column_name, column_type in column_matches if column_name.lower() != 'primary']
        columns[table_name] = table_columns

        # Primaerschluessel Definition fuer jede Tabelle
        primary_key_matches = re.findall(primary_key_regex, sql_dump, re.IGNORECASE)
        if primary_key_matches:
            primary_key_columns = primary_key_matches[0].split(',')
            primary_keys[table_name] = [column.strip().lower() for column in primary_key_columns]

        # Fremdschluessel Definition fuer jede Tabelle
        foreign_key_matches = re.findall(foreign_key_regex, sql_dump, re.IGNORECASE)
        for foreign_key_match in foreign_key_matches:
            foreign_key_columns = foreign_key_match[0].split(',')
            referenced_table = foreign_key_match[1].lower()
            referenced_columns = foreign_key_match[2].split(',')
            foreign_keys[(table_name, referenced_table)] = list(zip([column.strip().lower() for column in foreign_key_columns], [column.strip().lower() for column in referenced_columns]))

    return tables, columns, primary_keys, foreign_keys

# zur Pruefung
with open('spotifydbdumpschemashare.sql', 'r') as file:
    sql_dump = file.read()

tables, columns, primary_keys, foreign_keys = extract_table_info(sql_dump)

# Print-Anweisungen
for table in tables:
    print(f"Table: {table}")
    print(f"Columns: {columns[table]}")
    print(f"Primary Key: {primary_keys.get(table, None)}")
    print(f"Foreign Keys: {[(table, ref_table, cols) for (ref_table, cols) in foreign_keys.keys() if table == ref_table]}")
    print()