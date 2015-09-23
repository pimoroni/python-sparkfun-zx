all: build install

build:
	python setup.py build
	python3 setup.py build

install:
	sudo python setup.py install
	sudo python3 setup.py install

develop:
	sudo python setup.py develop
	sudo python3 setup.py develop
