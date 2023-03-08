from flask import request, render_template
import misc.misskey
import misc.note
import traceback

def authRequired():
    def middleware(handler):
        def wrapper(*args, **kw):
            token = request.cookies.get("token")
            if token == None:
                return misc.note.create_note("请先登录！<a href='/' style='color: blue;'>前往主站</a>。")
            try:
                data = misc.misskey.misskey_post("i", {}, token)
                id = data["id"]
                kw["id"] = id
                kw["ud"] = data
                kw["i"] = token
            except:
                return misc.note.create_note("请先登录！<a href='/'>前往主站</a>。")
            return handler(*args, **kw)
        wrapper.__name__ = handler.__name__
        return wrapper
    return middleware