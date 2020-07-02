test:
			python3 -m unittest tests/*_test.py tests/translate/*_test.py tests/translate/util/*_test.py

build:
			python3 setup.py sdist bdist_wheel

install:
			python3 setup.py install

clean:
			rm -rf build
			rm -rf dist
			rm -rf *.egg-info/

upload:
			twine upload --repository pypi dist/* --verbose

check:
			twine check dist/*
