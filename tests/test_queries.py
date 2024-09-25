import unittest
from query_data import query_data

class TestQueries(unittest.TestCase):
    def test_query(self):
        results = query_data()
        self.assertTrue(len(results) > 0)

if __name__ == '__main__':
    unittest.main()
