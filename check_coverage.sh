coverage erase --rcfile=check_coverage.ini
coverage run  --rcfile=check_coverage.ini test_it.py $@
coverage html --rcfile=check_coverage.ini
coverage report --rcfile=check_coverage.ini
open ./check_coverage/index.html &
