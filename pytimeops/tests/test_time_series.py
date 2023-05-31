

import unittest
import pytimeops as pto


class TestTimeSeries(unittest.TestCase):

    def test_init(self):
        t = [1, 2, 3]
        y = [10, 100, 105]
        ts = pto.TimeSeries(t, y)

        self.assertEqual(t, ts.t)
        self.assertEqual(y, ts.x)


if __name__ == '__main__':
    unittest.main()
