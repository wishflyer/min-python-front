# -*- coding:utf-8 -*-
from tornado.concurrent import TracebackFuture
from tornado.escape import utf8, native_str
from tornado import httputil, stack_context
from tornado.ioloop import IOLoop
from tornado.util import Configurable

from tornado.httpclient import AsyncHTTPClient,HTTPRequest,_RequestProxy,HTTPResponse,HTTPError
from tornado.simple_httpclient import SimpleAsyncHTTPClient

import time, json


class AsyncClient(SimpleAsyncHTTPClient, AsyncHTTPClient):
    def dict2form(self, obj):
        formStr = ""
        for k,v in obj.items():
            formStr += "%s=%s&"%(k,v)
        return formStr[0:-2]

    def fetch(self, url, headers=None, body=None, method="GET", callback=None, raise_error=True, **kwargs):
        """very simlar with AsyncHTTPClient.fetch
        """
        if self._closed:
            raise RuntimeError("fetch() called on closed AsyncHTTPClient")
        if isinstance(body, dict):
            body = self.dict2form(body)
            print (body)
        request = HTTPRequest(url=url,method=method,headers=headers,body=body, allow_nonstandard_methods=True, **kwargs)
        # We may modify this (to add Host, Accept-Encoding, etc),
        # so make sure we don't modify the caller's object.  This is also
        # where normal dicts get converted to HTTPHeaders objects.
        request.headers = httputil.HTTPHeaders(request.headers)
        request = _RequestProxy(request, self.defaults)
        future = TracebackFuture()
        if callback is not None:
            callback = stack_context.wrap(callback)

            def handle_future(future):
                exc = future.exception()
                if isinstance(exc, HTTPError) and exc.response is not None:
                    response = exc.response
                elif exc is not None:
                    response = HTTPResponse(
                        request, 599, error=exc,
                        request_time=time.time() - request.start_time)
                else:
                    response = future.result()
                self.io_loop.add_callback(callback, response)
            future.add_done_callback(handle_future)

        def handle_response(response):
            if raise_error and response.error:
                future.set_exception(response.error)
            else:
                try:
                    resp = json.loads(str(response.body))
                    future.set_result(resp)
                except Exception,e:
                    print (e)
                    future.set_result({})

        self.fetch_impl(request, handle_response)
        return future