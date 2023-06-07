import unittest
import pytimeops as pto


class TestReadData(unittest.TestCase):
    def test_read_file(self):
        '# Test data'
        test_data = 'test_data.csv'
        num_md = 4
        num_b = 10
        '# Call the function being tested'
        '#result = pto.read_file(test_data, num_md, num_b)'
        result = pto.read_file(test_data, 4, 10)
        '# Assert the expected results'
        self.assertIsInstance(result, list)
        '# Check individual Timeseries objects'
        for timeseries in result:
            self.assertIsInstance(timeseries, pto.Timeseries)
            self.assertEqual(len(timeseries.values), num_b)
            self.assertEqual(len(timeseries.metadata), num_md)


if __name__ == '__main__':
    unittest.main()
