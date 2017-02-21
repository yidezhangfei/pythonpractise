# /bin/env/python3
# coding: utf-8

''' models for user, blog, comment'''

import time, uuid
from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, data_type='varchar(50)')
    email = StringField(data_type='varchar(50)')
    password = StringField(data_type='varchar(50)')
    admin = BooleanField()
    name = StringField(data_type='varchar(50)')
    image = StringField(data_type='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, data_type='varchar(50)')
    user_id = StringField(data_type='varchar(50)')
    user_name = StringField(data_type='varchar(50)')
    user_image = StringField(data_type='varchar(500)')
    name = StringField(data_type='varchar(50)')
    summary = StringField(data_type='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, data_type='varchar(50)')
    blog_id = StringField(data_type='varchar(50)')
    user_id = StringField(data_type='varchar(50)')
    user_name = StringField(data_type='varchar(50)')
    user_image = StringField(data_type='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

if __name__ == '__main__':
    u = User(id='123', email='lijun@sogou-inc.com', password='li')
    print(u)



















