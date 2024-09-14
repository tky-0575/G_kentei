#!/usr/bin/env python3

import cgi
import codecs
from jinja2 import Template, Environment, FileSystemLoader

from g_sql import regist
from g_sql import browse

form = cgi.FieldStorage()

if form.list == []:
    #初回アクセスの場合
    html = codecs.open('./g_website.html', 'r', 'utf-8').read()
else:
    if not len(form.getlist("browse")) == 0:
        #検索の場合
        resp = browse(form)
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('./g_temp.jinja')
        html = template.render({'results':resp})
    else:
        #登録の場合
        regist(form)
        html = codecs.open('./g_website.html', 'r', 'utf-8').read()

print("")
print(html)