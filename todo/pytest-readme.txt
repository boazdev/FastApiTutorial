pytest -s tests/ # or pytest --capture=no tests/
(runs tests with print function allowed)

pytest -s -p no:warnings ./tests
(runs tests with print and no warnings)