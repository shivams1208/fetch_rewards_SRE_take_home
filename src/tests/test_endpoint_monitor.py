import unittest
from unittest.mock import MagicMock, patch

from availability_logger import AvailabilityLogger
from config_loader import YamlConfigLoader
from endpoint_monitor import EndpointMonitor
from health_checker import EndpointHealthChecker


class TestEndpointMonitor(unittest.TestCase):

    # Test for EndpointMonitor
    @patch('time.sleep', return_value=None)
    def test_monitor_endpoints_single_iteration(self, mock_sleep):
        """
        Test a single iteration of the EndpointMonitor's monitoring loop.
        """
        # Mock creation of dependencies
        config_loader = MagicMock(spec=YamlConfigLoader)
        health_checker = MagicMock(spec=EndpointHealthChecker)
        availability_logger = MagicMock(spec=AvailabilityLogger)

        # Configuring the mocks
        config_loader.load_config.return_value = [{'url': 'http://example.com', 'name': 'Example'}]
        health_checker.check_health.return_value = True

        # Instantiate the monitor
        monitor = EndpointMonitor(config_loader, health_checker, availability_logger)

        # Mock the behavior of the availability logger to stop the loop after one iteration
        def side_effect(*args, **kwargs):
            raise Exception("Stop loop")

        availability_logger.log_availability.side_effect = side_effect

        # Execute and expect an exception to stop the loop
        with self.assertRaises(Exception):
            monitor.monitor_endpoints("test.yaml")

        # Assertions
        config_loader.load_config.assert_called_once_with("test.yaml")
        health_checker.check_health.assert_called_once()
        availability_logger.update_availability.assert_called_once()
        availability_logger.log_availability.assert_called_once()

if __name__ == '__main__':
    unittest.main()
