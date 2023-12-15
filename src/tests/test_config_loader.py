import unittest
from unittest.mock import mock_open, patch

from config_loader import YamlConfigLoader


class TestYamlConfigLoader(unittest.TestCase):

    # Test for YamlConfigLoader
    @patch("builtins.open", new_callable=mock_open, read_data="url: http://example.com")
    @patch("yaml.safe_load", return_value=[{'url': 'http://example.com'}])
    def test_yaml_config_loader(self, mock_safe_load, mock_open):
        """
        Test the YamlConfigLoader's ability to load and parse a YAML file.
        """
        file_path = "test.yaml"
        loader = YamlConfigLoader()
        endpoints = loader.load_config(file_path)

        # Assert that the file is opened correctly and YAML data is loaded
        mock_open.assert_called_with(file_path, 'r')
        mock_safe_load.assert_called()
        self.assertEqual(endpoints, [{'url': 'http://example.com'}])

if __name__ == '__main__':
    unittest.main()
