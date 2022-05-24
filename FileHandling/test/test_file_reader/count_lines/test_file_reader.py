import unittest
from oprations.file_reader.count_lines.file_reader import FileReader
import pdb
from unittest.mock import patch, mock_open

class TestReadFiles(unittest.TestCase):
    def test_count_lines(self):
        file_content_mock = """Name: ng1
                            Post: sdn
                            Salary: 23

                            Name: naren
                            Post: engineer
                            Salary: 4500"""
        fake_file_path = 'file/path/mock'

        with patch('oprations.file_reader.count_lines.file_reader.open'.format(__name__),
            new=mock_open(read_data=file_content_mock)) as _file:
            actual = FileReader().count_lines(fake_file_path)
            _file.assert_called_once_with(fake_file_path, 'r')

        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)
