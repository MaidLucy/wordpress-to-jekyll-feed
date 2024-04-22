import os
import sqlalchemy as sa
from email import utils as emailut
import datetime, time
from sqlalchemy.types import DateTime

connstr = os.environ['MARIADB_CONNSTR']
print(connstr)

engine = sa.create_engine(connstr)

with engine.connect() as conn:

    result = conn.execute(sa.text("select ID, post_title, post_name, post_date, post_content, post_excerpt from wp_posts where post_status = \'publish\' and post_type = \'post\'"))

    for row in result:
        with open('output/' + str(row[3].date()) + '-' + row[2] + '.md', 'w+', encoding="utf-8") as f:
            f.write("""---
layout: post
title: {}
date: {}
description: {}
...

{}

""".format(row[1], emailut.formatdate(time.mktime(row[3].timetuple())), row[5], row[4] ))
