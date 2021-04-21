import psycopg2

# создать соединение
conn = psycopg2.connect(user='', password='', database='', host='')

# создать курсор
cursor = conn.cursor()

# Выполнить запрос
cursor.execute('select attribite from table;')

# получить строку/все строки: fetchone, fetchall
r = cursor.fetchall()
print(r)

# выполнить транзакцию
# conn.commit()

# закрыть курсор
cursor.close()

# закрыть соединение
conn.close()
