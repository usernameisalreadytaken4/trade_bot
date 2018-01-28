#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Roman B.

from datetime import datetime

from sqlalchemy import Column, Integer, String, MetaData, DateTime, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from models.main import engine

model = declarative_base(cls=DeferredReflection)

metadata = MetaData()


class Players(model):

    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    discord_mention = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    rank = Column(Integer, default=1)


class TradeLots(model):

    __tablename__ = 'trade_lots'

    id = Column(Integer, primary_key=True)
    owner_fid = Column(Integer, ForeignKey('players.id'), nullable=False),
    url = Column(String, nullable=False)
    item = Column(String, nullable=False)
    price = Column(BigInteger, nullable=True)
    time_created = Column(DateTime, default=datetime.now())

if __name__ == '__main__':
    model.prepare(engine)