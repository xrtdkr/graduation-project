from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect("tutorialspoint")


query = "INSERT INTO table_1 (column_1, column_2, column_3, column_4) VALUES (1,2,'3',4);"
for index in xrange(10):
    session.execute(query)

rows = session.execute('SELECT column_1, column_2, column_3, column_4 FROM table_1')

for row in rows:
    print row.column_1


