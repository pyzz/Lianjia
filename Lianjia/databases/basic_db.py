#!/usr/bin/env python

from Lianjia.settings import MYSQL_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine(MYSQL_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

