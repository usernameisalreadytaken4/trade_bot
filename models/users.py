#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Roman B.

from sqlalchemy import Table, Column, Integer, String, MetaData
from models.main import engine

metadata = MetaData()
users_table = Table('lots', metadata,
    Column('id', Integer, primary_key=True),
    Column('discord_mention', String, nullable=False),
    Column('nick', String, nullable=True),
    Column('item', String, nullable=False),
    Column('price', String, nullable=True)
)

if __name__ == '__main__':
    metadata.create_all(engine)