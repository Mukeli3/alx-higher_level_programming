#!/usr/bin/python3
'''
list all states from the database hbtn_0e_0_usa
'''

import sys
import MySQLdb

if __name__ == '__main__':
    '''
    accessing database to get the states
    '''
    db_connection = MySQLdb.connect(
            host='localhost'
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=33306
            )

    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
    selected_rows = db_cursor.fetchall()
    for rw in selected_rows:
        print(rw)

    db_connection.close()
    db_cursor.close()
