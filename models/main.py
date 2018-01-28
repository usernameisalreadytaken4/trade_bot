#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Roman B.

from sqlalchemy import create_engine
from config import *

engine = create_engine('postgresql://%s:%s@%s/%s' % (USERNAME, PASSWORD, URI, DATATABLE))
