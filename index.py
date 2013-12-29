#-*- coding: utf-8 -*-
__author__ = 'amentis'
import sys

sys.path.append("/home/amentis/Dropbox/Rexi")

#from UI import Console
from UI import Login

sys.dont_write_bytecode = True


#noinspection PyUnusedLocal
def application(environ, start_response):
    """

    @param environ: standard environ
    @param start_response: standard start_response
    @return: return html request
    """

    #ui = Console.Console()
    ui = Login.Login()
    response_body = ui.get().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]