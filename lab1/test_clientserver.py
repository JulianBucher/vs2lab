"""
Simple client server unit test
"""

import logging
import threading
import unittest

import clientserver
from context import lab_logging

lab_logging.setup(stream_level=logging.INFO)


class TestEchoService(unittest.TestCase):
    """The test"""
    _server = clientserver.Server()
    _server_thread = threading.Thread(target=_server.serve)

    @classmethod
    def setUpClass(cls):
        cls._server_thread.start() 

    def setUp(self):
        super().setUp()
        self.client = clientserver.Client()

    def test_srv_get(self):
        """Test GET command"""
        msg = self.client.call("GET Alice")
        self.assertEqual(msg, '1234567')

    def test_srv_getall(self):
        """Test GETALL command"""
        msg = self.client.call("GETALL")
        self.assertEqual(msg, "{'alice': 1234567, 'bob': 2345678, 'carol': 3456789}")

    def tearDown(self):
        self.client.close()

    @classmethod
    def tearDownClass(cls):
        cls._server._serving = False
        cls._server_thread.join()


if __name__ == '__main__':
    unittest.main()
