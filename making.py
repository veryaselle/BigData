import sqlparse

# Laden SQL dump file
with open('spotifydbdumpschemashare.sql', 'r') as file:
    sql_statements = file.read()


# SQL statements parsen
parsed_statements = sqlparse.parse(sql_statements)

# Für triples wurden eine leere Liste initializiert
triples = []

# Parsed statements, Vorgang
for statement in parsed_statements:
    # Pruefen, ob CREATE TABLE statement vorhanden ist
    if statement.get_type() == 'CREATE':
        # Ausfueren, falls ja
        tokens = statement.tokens

        # Name der Tabelle finden
        table_name = None
        for token in tokens:
            if isinstance(token, sqlparse.sql.Identifier):
                table_name = token.get_real_name()

        # Zeilennamen:
        columns = []
        for token in tokens:
            if isinstance(token, sqlparse.sql.IdentifierList):
                for identifier in token.get_identifiers():
                    columns.append(identifier.get_real_name())

        # tripples fuer Tabellen- und Zeilennamen
        if table_name:
            triples.append(('table', 'has_name', table_name))
            for column_name in columns:
                triples.append((table_name, 'has_column', column_name))

            # Fremdschluessel ziehen
            for i, token in enumerate(tokens):
                if token.value == 'REFERENCES':
                    referred_table = tokens[i + 1].get_real_name()
                    referred_column = tokens[i + 2].get_real_name()
                    triples.append((table_name, 'has_foreign_key', referred_table))
                    triples.append((table_name, 'has_foreign_key_column', referred_column))

# Triples zu printen
for triple in triples:
    print(triple)