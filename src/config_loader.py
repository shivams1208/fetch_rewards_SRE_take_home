import logging
from abc import ABC, abstractmethod

import yaml


# Abstract base class for configuration loaders
class ConfigLoader(ABC):
    
    @abstractmethod
    def load_config(self, file_path):
        """
        Load configuration from a file.
        
        :param file_path: Path to the configuration file.
        """
        pass

# Concrete implementation of ConfigLoader for YAML files
class YamlConfigLoader(ConfigLoader):

    def load_config(self, file_path):
        """
        Load and parse a YAML file.

        :param file_path: Path to the YAML file.
        :return: Parsed data from the YAML file.
        """
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise
        except yaml.YAMLError as e:
            logging.error(f"Error parsing YAML file: {e}")
            raise
