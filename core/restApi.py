# coding:utf-8
from handler import AsyncClient
from config import appConfig

client = AsyncClient()


def post(url,body=None,headers=None):
    return client.fetch(appConfig.restApiServer+url, headers, body, "POST")


def get(url,headers=None,body=None):
    return client.fetch(appConfig.restApiServer+url, headers, body, "GET")