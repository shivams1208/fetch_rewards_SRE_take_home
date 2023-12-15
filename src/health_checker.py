import logging
import time
from abc import ABC, abstractmethod

import requests


# Abstract base class for health checkers
class HealthChecker(ABC):

    @abstractmethod
    def check_health(self, endpoint):
        """
        Check the health of an endpoint.

        :param endpoint: A dictionary containing endpoint information.
        :return: Boolean indicating the health status of the endpoint.
        """
        pass

# Concrete implementation of HealthChecker
class EndpointHealthChecker(HealthChecker):

    def check_health(self, endpoint):
        """
        Perform a health check on the specified endpoint.

        :param endpoint: A dictionary containing endpoint information.
        :return: Boolean indicating whether the endpoint is healthy.
        """
        try:
            url = endpoint['url']
            method = endpoint.get('method', 'GET').upper()
            headers = endpoint.get('headers', {})
            body = endpoint.get('body', None)

            start_time = time.time()
            response = requests.request(method, url, headers=headers, json=body)
            end_time = time.time()

            latency_ms = (end_time - start_time) * 1000
            return 200 <= response.status_code < 300 and latency_ms < 500
        except Exception as e:
            logging.error(f"Error checking {url} with method {method}: {e}")
            return False
