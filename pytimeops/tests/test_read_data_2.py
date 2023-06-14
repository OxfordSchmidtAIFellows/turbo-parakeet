import unittest
import pytimeops as pto


class TestReadData(unittest.TestCase):
    def test_read_file(self):
        '# Test data'
        test_data = 'Data/test_data.csv'
        '# Call the function being tested'
        '#result = pto.read_file(test_data, num_md, num_b)'
        result = pto.read_file(test_data, 10, "", "GRN")
        '# Assert the expected results'
        self.assertIsInstance(result, pto.Dataset)
        '# Check individual Timeseries objects'
        for timeseries in result.dataset:
            self.assertIsInstance(timeseries, pto.Timeseries)
            self.assertEqual(timeseries.time_interval, 10)


if __name__ == '__main__':
    unittest.main()
