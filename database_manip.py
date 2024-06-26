import sqlite3

conn = sqlite3.connect('python_programming.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    grade INTEGER
                  )''')

# Insert rows to the table defined by the user
rows_to_insert = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

# Insert the rows into the table
cursor.executemany('INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)', rows_to_insert)

# Save changes
conn.commit()

# Update Carl's grade to 65
update_query = '''
               UPDATE python_programming
               SET grade = 65
               WHERE name = 'Carl Davis'
               '''

cursor.execute(update_query)
conn.commit()  # Save the change

# Delete Dennis's row
delete_query = '''
               DELETE FROM python_programming
               WHERE name = 'Dennis Fredrickson'
               '''

cursor.execute(delete_query)
conn.commit()  # Save the change

# Update grade of all students with id greater than 55 to 80
update_query_all = '''
                    UPDATE python_programming
                    SET grade = 80
                    WHERE id > 55
                    '''

cursor.execute(update_query_all)
conn.commit()  # Save the change

# Select records with grade between 60 and 80
select_query = '''
               SELECT id, name, grade
               FROM python_programming
               WHERE grade BETWEEN 60 AND 80
               '''

# Execute the query
cursor.execute(select_query)

# Select all rows
selected_rows = cursor.fetchall()

# Print the selected rows
print("Records with grade between 60 and 80:")
for row in selected_rows:
    print(row)

conn.close()
