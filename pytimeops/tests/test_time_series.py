import unittest
import pytimeops as pto


class TestTimeSeries(unittest.TestCase):

    def test_init(self):
        time_indices = [1, 2, 3]
        values = [[10, 100, 105],[1, 3, 5]]
        channels = ["GRN1","GRN2"]
        metadata = {"sensillum": "s1", "sugar": "fruc"}
        time_interval = 100 #ms
        ts = pto.Timeseries(time_indices, values, metadata, channels, time_interval)

        self.assertEqual(time_indices, ts.time_indices)
        self.assertEqual(values, ts.values)
        self.assertEqual(metadata, ts.metadata)
        self.assertEqual(channels, ts.channels)
        self.assertEqual(time_interval, ts.time_interval)


if __name__ == '__main__':
    unittest.main()
