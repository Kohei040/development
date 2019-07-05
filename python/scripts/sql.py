import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='db',
    port='3306',
    user='hoge',
    password='hogehoge',
    database='hogedb'
)

# Connection Check
print(conn.is_connected())

# Create Cursol
cur = conn.cursor()

# DROP TABLE
cur.execute("DROP TABLE IF EXISTS `test_table`")

# Create Table
cur.execute("""CREATE TABLE IF NOT EXISTS `test_table` (
    `id` int(11) NOT NULL,
    `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` int(11) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

# INSERT
cur.execute("INSERT INTO test_table VALUES (1, 'Apple', 1000)")

cur.execute("INSERT INTO test_table VALUES (2, 'Banana', %s)", (1200, ))
cur.execute("INSERT INTO test_table VALUES (%s, %s, %s)", (3, "Grape", 800))
cur.execute("INSERT INTO test_table VALUES (%(id)s, %(name)s, %(price)s)", {'id': 4, 'name': "Strawberry", 'price': 1100})

records = [
    (5, 'Melon', 2000),
    (6, 'Peach', 1800),
]
cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s)", records)

# SELECT
cur.execute("SELECT * FROM test_table ORDER BY id ASC")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT * FROM test_table WHERE name=%s", ('Banana', ))

print(cur.rowcount)
print(cur.fetchone())

# UPDATE
cur.execute('UPDATE test_table SET name=%s WHERE id=1', ('Cherry', ))
cur.execute('UPDATE test_table SET name=%s WHERE id=%s', ('Persimmon', 2))

# DELETE
cur.execute('DELETE FROM test_table WHERE id=3')

cur.execute("SELECT * FROM test_table ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close
cur.close()
conn.commit()
conn.close()
