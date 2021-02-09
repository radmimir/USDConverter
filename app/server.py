import http.server
import json
from urllib.request import urlopen
import re
import threading
import asyncio
import logging
import concurrent.futures

PORT = 8000


class Error(Exception):
    pass


class IncorrectURLError(Error):
    """Exception raised for errors in URL address

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def get_usd_course():
    with urlopen("https://1000bankov.ru/kurs/usd/") as r:
        if r.status == 200:
            lines = r.read().decode('utf-8')
            usd_curse = re.search(r'<div class="cbcourses__value">(\d*\.\d*)', lines)
            return float(usd_curse.group(1))
        else:
            raise IncorrectURLError


class USDRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        request = self.path.split('/')[1:]
        data = {}
        usd_course = get_usd_course()
        if len(request) == 2:
            value = float(request[1])
            currency = request[0].lower()
            if currency == 'usd_rub':
                self.send_response(200, 'OK')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                data["currency"] = "RUB"
                data["requested_value"] = value
                data["calculated_value"] = round(usd_course * value, 2)
                json_string = json.dumps(data)
                self.wfile.write(json_string.encode(encoding="utf-8"))
            elif currency == "rub_usd":
                self.send_response(200, 'OK')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                data["currency"] = "USD"
                data["requested_value"] = value
                data["calculated_value"] = round(value / usd_course, 2)
                json_string = json.dumps(data)
                self.wfile.write(json_string.encode(encoding="utf-8"))
            else:
                self.send_response(404, 'Not found')
        else:
            self.send_response(404, "Not found")


class USDConverterServer:
    def start_server(self):
        logging.basicConfig(level=logging.DEBUG)
        with http.server.HTTPServer(('', PORT), USDRequestHandler) as server:
            print("Started Server at localhost:", PORT)
            server.serve_forever()
            print("Flushed", PORT)


if __name__ == '__main__':
    server = USDConverterServer()
    server.start_server()
