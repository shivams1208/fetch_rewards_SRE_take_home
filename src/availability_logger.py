import logging
from urllib.parse import urlparse


# Class for logging the availability of endpoints
class AvailabilityLogger:

    def __init__(self):
        """
        Initialising the AvailabilityLogger with an empty availability record.
        """
        self.availability = {}

    def update_availability(self, url, is_up):
        """
        Update the availability record for a given URL.

        :param url: The URL of the endpoint.
        :param is_up: Boolean indicating whether the endpoint is up or down.
        """
        base_url = urlparse(url).netloc
        if base_url not in self.availability:
            self.availability[base_url] = {'up': 0, 'total': 0}

        self.availability[base_url]['up'] += int(is_up)
        self.availability[base_url]['total'] += 1

    def log_availability(self):
        """
        Logging the availability statistics for each monitored endpoint.
        """
        for base_url, stats in self.availability.items():
            percentage = (stats['up'] / stats['total']) * 100 if stats['total'] > 0 else 0
            logging.info(f"{base_url} has {percentage:.0f}% availability percentage")
