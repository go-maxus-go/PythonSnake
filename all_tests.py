import unittest
import tests.test_field

# get suites from test modules
suites = [
tests.test_field.suite(),
]

# collect suites in a TestSuite object
suite = unittest.TestSuite()
for s in suites:
    suite.addTest(s)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)
