import unittest
from oprations.write_on_file.file_writer.file_writer import FileWriter
from unittest.mock import patch, mock_open

class TestReadFiles(unittest.TestCase):
    def test_file_writer(self):
        fake_file_path = "fake/file/path"
        content = "Message to write on file to be written"
        with patch('oprations.write_on_file.file_writer.file_writer.open', mock_open()) as mocked_file:
            FileWriter().write(fake_file_path, content)

            mocked_file.assert_called_once_with(fake_file_path, 'w')
            mocked_file().write.assert_called_once_with(content)