import unittest
import pytimeops as pto


class TestTimeSeries(unittest.TestCase):

    def test_init(self):
        time_indices = [1, 2, 3]
        values = [10, 100, 105]
        metadata = {"sensillum": "s1", "sugar": "fruc", "GRN": "GRN1"}
        ts = pto.Timeseries(time_indices, values, metadata)

        self.assertEqual(time_indices, ts.time_indices)
        self.assertEqual(values, ts.values)
        self.assertEqual(metadata, ts.metadata)


if __name__ == '__main__':
    unittest.main()
