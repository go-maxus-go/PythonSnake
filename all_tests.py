import unittest
import tests.test_field
import tests.test_apple
import tests.test_snake

# get suites from test modules
suites = [
tests.test_field.suite(),
tests.test_apple.suite(),
tests.test_snake.suite(),
]

# collect suites in a TestSuite object
suite = unittest.TestSuite()
for s in suites:
    suite.addTest(s)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)
