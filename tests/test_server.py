import unittest
from app import server
import http.client
import json
import threading


class TestServer(unittest.TestCase):

    def setUp(self):
        a = server.USDConverterServer()
        test_thread = threading.Thread(target=a.start_server)
        test_thread.setDaemon(True)
        test_thread.start()
        self.course = server.get_usd_course()
        conn = http.client.HTTPConnection("", 8000)
        value = 1000
        request = '/{0}/{1}'.format("usd_rub", value)
        conn.request("GET", request)
        self.responce = conn.getresponse()
        self.json_res = json.load(self.responce)

    def test_do_GET(self):
        self.assertEqual(self.responce.status, 200)
        self.assertEqual(self.json_res["currency"], "RUB")
        self.assertEqual(self.json_res["requested_value"], 1000)
        self.assertAlmostEqual(self.json_res["calculated_value"], 1000 * self.course)

    def test_get_usd_course(self):
        self.assertIsInstance(self.course, float)


if __name__ == '__main__':
    unittest.main()
