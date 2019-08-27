# -*- coding: utf-8 -*-
from flask import session
from flask import redirect, url_for
import functools

def auth_wrapper(db_handle, route_url):

    def wrapper(func):
        @functools.wraps(func)
        def my_wrapper(*args, **kwargs):
            # 查询数据库 管理员查出来
            data = db_handle()
            name = session.get('username')
            if not name:
                return redirect(url_for(route_url))
            if not data:
                return redirect(url_for(route_url))

            # if not kwargs.get('administrators'):
            #   return

            administrators = []
            for value in data:
                administrators.append(value[0])

            if name not in administrators:
                return redirect(url_for(route_url)) 
            # print("my_wrapper", args, kwargs)
            return func()

        return my_wrapper
    return wrapper