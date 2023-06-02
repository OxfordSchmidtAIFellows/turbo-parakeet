

import unittest
import pytimeops as pto


class TestTimeSeries(unittest.TestCase):

    def test_init(self):
        t = [1, 2, 3]
        v = [10, 100, 105]
        md = ["s1", "fruc", "0mM", "GRN1"]
        ts = pto.TimeSeries(t, v, md)

        self.assertEqual(t, ts.time_index)
        self.assertEqual(v, ts.values)
        self.assertEqual(md, ts.metadata)


if __name__ == '__main__':
    unittest.main()
