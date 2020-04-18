import unittest
import covid

#saved as test_covid.py
#naming convention for testrunners in python: start with test_
#popular one: pytest -> will be able to discover those tests

class TestCovid(unittest.TestCase):
    #xunit paradigm from smalltalk: setup, assertions, teardown
    def test_read_csv(self):
        res = covid.read_csv('covid.csv')
        print(len(res))
        self.assertEqual(len(res), 2284)

    def test_get_value(self):
        data = [{'name':'matt'},
                {'name':'suzy'}]
        res = covid.get_value(data, 'name')
        self.assertEqual(res, ['matt', 'suzy'])

if __name__ == '__main__':
    # executing
    unittest.main()
else:
    # loading this filter
    print('loading')
