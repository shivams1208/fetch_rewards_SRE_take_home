import unittest
from unittest.mock import patch

from health_checker import EndpointHealthChecker


class TestEndpointHealthChecker(unittest.TestCase):

    # Test for EndpointHealthChecker
    @patch("requests.request")
    def test_endpoint_health_checker(self, mock_request):
        """
        Test the EndpointHealthChecker's ability to check the health of an endpoint.
        """
        health_checker = EndpointHealthChecker()
        endpoint = {"url": "http://test.com", "method": "GET"}
        
        # Mock different responses and test the health check outcomes
        mock_request.return_value.status_code = 200
        result = health_checker.check_health(endpoint)
        self.assertTrue(result)

        mock_request.return_value.status_code = 500
        result = health_checker.check_health(endpoint)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
