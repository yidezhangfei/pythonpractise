# -*- coding: utf-8 -*-

import os, sqlite3

def init_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute("insert into user values ('A-001', 'Adan', 95)")
    cursor.execute("insert into user values ('A-002', 'Bart', 62)")
    cursor.execute("insert into user values ('A-003', 'Lisa', 78)")
    cursor.close()
    conn.commit()
    conn.close()

db_file = ''

def test(db_file):
    assert get_score_in(80, 95) == ['Adan'], get_score_in(80, 95)
    assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adan'], get_score_in(60, 100)

def get_score_in(low, high):
    db = sqlite3.connect(db_file)
    db_cursor = db.cursor()
    try:
        db_cursor.execute('select name from user where score >= ? and score <= ? order by score', (low, high))
        values = db_cursor.fetchall()
        results = [name[0] for name in values]
        print (results)
    finally:
        db_cursor.close()
        db.close()
    return results

if __name__ == '__main__':
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    if os.path.isfile(db_file):
        os.remove(db_file)

    init_db('test.db')
    test(db_file)
