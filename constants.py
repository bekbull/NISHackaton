import requests as req
import logging

logger = logging.getLogger()

toqen = '659340911:AAFdMGvuQKz6r933tLhne-w8clab8QWifZo'
password = 'qwert13'

def fetch_json(base, route):
    product = req.get(base + route)
    logger.info("a request to the api for {route} was sent")
    return product.json()