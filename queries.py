def sql_insert(tablename, columns, values):
    query = f'INSERT INTO {tablename} {columns} VALUES {values}'
    return query

def sql_select(tablename):
    query = f'SELECT * FROM {tablename}'
    return query

def sql_update(tablename, column, value, idNumber):
    query = f'UPDATE {tablename} SET {column} = {value} WHERE id={idNumber}'
    return query

def sql_delete(tablename, idNumber):
    query = f'DELETE FROM {tablename} WHERE id = {idNumber}'
    return query
