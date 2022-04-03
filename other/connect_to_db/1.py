import pymysql

# connect to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='bn_opencart', password='', db='bitnami_opencart')
cursor = conn.cursor()

# Print all tables
cursor.execute('SHOW TABLES')
myresult = cursor.fetchall()
print(myresult)

# show all in table oc_currency
cursor.execute('select * from oc_currency')
table = cursor.fetchall()
print(table)

# show all in table oc_product
cursor.execute('select * from oc_product')
table = cursor.fetchall()
print(table)
print('============')

# show first row of table oc_product
cursor.execute('select * from oc_product')
fetch_one = cursor.fetchone()
print(fetch_one)

# Describe table oc_product
cursor.execute('describe oc_product')
fetch_one = cursor.fetchall()
print(fetch_one)

# Show 2 most expensive models from oc_product table
cursor.execute(' select model, price from oc_product ORDER BY Price DESC')
fetch_one = cursor.fetchone()
print(fetch_one)
fetch_one = cursor.fetchone()
print(fetch_one)





conn.close()