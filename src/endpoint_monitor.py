import logging
import time

from availability_logger import AvailabilityLogger
from config_loader import YamlConfigLoader
from health_checker import EndpointHealthChecker

# Configuring basic logging. Setting the level at INFO and defining the format of log message: timestamp, loglevel and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Main class for monitoring endpoints
class EndpointMonitor:

    def __init__(self, config_loader, health_checker, availability_logger, sleep_interval=15):
        """
        Initialising the EndpointMonitor with specific dependencies.

        :param config_loader: An instance of ConfigLoader to load endpoint configurations.
        :param health_checker: An instance of HealthChecker to check endpoint health.
        :param availability_logger: An instance of AvailabilityLogger to log endpoint availability.
        :param sleep_interval: Time in seconds between each monitoring cycle.
        """
        self.config_loader = config_loader
        self.health_checker = health_checker
        self.availability_logger = availability_logger
        self.sleep_interval = sleep_interval

    def monitor_endpoints(self, file_path):
        """
        Monitor the endpoints as defined in the configuration file.

        :param file_path: Path to the configuration file.
        """
        endpoints = self.config_loader.load_config(file_path)
        try:
            while True:
                for endpoint in endpoints:
                    if 'url' not in endpoint or 'name' not in endpoint:
                        logging.warning(f"Skipping an endpoint due to missing 'url' or 'name': {endpoint}")
                        continue

                    is_up = self.health_checker.check_health(endpoint)
                    self.availability_logger.update_availability(endpoint['url'], is_up)

                self.availability_logger.log_availability()
                time.sleep(self.sleep_interval)
        except KeyboardInterrupt:
            logging.info("Program interrupted by user. Exiting...")

# Main execution block
if __name__ == "__main__":
    file_path = input("Enter the path to the YAML file: ").strip()
    config_loader = YamlConfigLoader()
    health_checker = EndpointHealthChecker()
    availability_logger = AvailabilityLogger()
    monitor = EndpointMonitor(config_loader, health_checker, availability_logger)
    monitor.monitor_endpoints(file_path)
