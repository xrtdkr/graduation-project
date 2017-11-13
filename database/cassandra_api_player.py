from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()

session = cluster.connect("tutorialspoint")


query_sql = "INSERT INTO table_1 (column_1, column_2, column_3, column_4) VALUES (1,2,'3',4);"


query_deco = SimpleStatement(
    query_string=query_sql,
    consistency_level=ConsistencyLevel.ANY
)

for index in xrange(10):
    session.execute(query_deco)

rows = session.execute('SELECT column_1, column_2, column_3, column_4 FROM table_1')

for row in rows:
    print row.column_1


