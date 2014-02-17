#-*- coding: utf-8 -*-
__author__ = 'amentis'
import sys

sys.path.append("/home/amentis/Dropbox/Rexi")

from beaker.middleware import SessionMiddleware
from UI import Console
from UI import Login


#noinspection PyUnusedLocal
def starter(environ, start_response):
    """
    @param environ: standard environ
    @param start_response: standard start_response
    @return: return html request
    """

    session = environ['beaker.session']

    if 'logged_in' in session:  # check in database if last attempt is a login and successful
        ui = Console.Console()
    else:
        ui = Login.Login()

    response_body = ui.get().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

session_opts = {
    'session_type': 'file',
    'session_cookie_expires': False,
}


application = SessionMiddleware(starter, session_opts)