#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用方法 python md2html.py  filename

import os, sys
sys.path.append("..")
import markdown
from model.blog_article import Article

model_article = Article()

head = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<style type="text/css">
code {
  color: inherit;
  background-color: rgba(0, 0, 0, 0.05);
}
</style>
</head>
<body>
"""

foot = """
</body>
</html>
"""
def article2html():
	html = ""
	data = model_article.query(22)
	for x in data:
		id = x[0]
		user_id = x[1]
		class_id = x[2]
		label_id = x[3]
		title = x[4]
		content = x[5]
		read = x[6]
		create_time = x[7]
		html = markdown.markdown(content)
		return head+html+foot
		break
# fp1.close()