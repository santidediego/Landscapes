install:
	sudo apt-get update && pip3 install -r requirements.txt

test:
	nosetests
