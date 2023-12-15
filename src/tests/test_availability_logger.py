import unittest

from availability_logger import AvailabilityLogger


class TestAvailabilityLogger(unittest.TestCase):

    # Test for AvailabilityLogger
    def test_availability_logger(self):
        """
        Test the AvailabilityLogger's ability to update and log endpoint availability.
        """
        logger = AvailabilityLogger()
        logger.update_availability("http://test.com", True)
        logger.update_availability("http://test.com", False)

        # Checking if the availability record is updated correctly
        expected = {'test.com': {'up': 1, 'total': 2}}
        self.assertEqual(logger.availability, expected)

        # Checking if the logging output contains the correct availability percentage
        with self.assertLogs(level='INFO') as log:
            logger.log_availability()
            self.assertTrue(any("test.com has 50% availability percentage" in message for message in log.output))

if __name__ == '__main__':
    unittest.main()
