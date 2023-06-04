

import unittest
import pytimeops as pto


class TestTimeSeries(unittest.TestCase):

    def test_init(self):
        t = [1, 2, 3]
        v = [10, 100, 105]
        md = {"sensillum": "s1", "sugar": "fruc", "GRN": "GRN1"}
        ts = pto.Timeseries(t, v, md)

        self.assertEqual(t, ts.time_index)
        self.assertEqual(v, ts.values)
        self.assertEqual(md, ts.metadata)


if __name__ == '__main__':
    unittest.main()
