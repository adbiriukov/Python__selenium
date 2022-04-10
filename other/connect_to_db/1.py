import pymysql

# connect to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='bn_opencart', password='', db='bitnami_opencart')
cursor = conn.cursor()

# # Print all tables
# cursor.execute('SHOW TABLES')
# myresult = cursor.fetchall()
# for x in myresult:
#     print(x)

# # delete one customer
# cursor.execute('delete from oc_customer where email="some_mail@mail.com";')
# table = cursor.fetchall()
# print(table)
# print(len(table))

# # show all in table oc_customer
# cursor.execute('select * from oc_customer')
# table = cursor.fetchall()
# print(table)
# print(len(table))


# # show all in table oc_currency
# cursor.execute('select * from oc_currency')
# table = cursor.fetchall()
# print(table)
#
# show all in table oc_product
cursor.execute('select model, price from oc_product order by price DESC')
table = cursor.fetchall()
for x in table:
    print(x)
# print('============')
#
# # show first row of table oc_product
# cursor.execute('select * from oc_product')
# fetch_one = cursor.fetchone()
# print(fetch_one)
#
# # Describe table oc_product
# cursor.execute('describe oc_product')
# fetch_one = cursor.fetchall()
# print(fetch_one)
#
# # Show 2 most expensive models from oc_product table
# cursor.execute(' select model, price from oc_product ORDER BY Price DESC')
# fetch_one = cursor.fetchone()
# print(fetch_one)
# fetch_one = cursor.fetchone()
# print(fetch_one)





conn.close()