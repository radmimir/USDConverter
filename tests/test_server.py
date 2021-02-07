import unittest
from app import server
import http.client


class TestServer(unittest.TestCase):
    def setUp(self):
        server.start_server()

    def test_do_GET(self):
        conn = http.client.HTTPConnection("", 8000)
        value = 1000
        request = '/{0}/{1}'.format("usd_rub", value)
        print(request)
        conn.request("GET", request)
        responce = conn.getresponse()
        print(responce.status, responce.reason)
        self.assertEqual(responce.status, 200)
        self.assertEqual(responce.status, 200)

    def test_get_usd_course(self):
        course = server.get_usd_course()
        self.assertIsInstance(course, float)


if __name__ == '__main__':
    unittest.main()
