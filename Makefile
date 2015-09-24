ENV=./env

all: help

help:
	@echo '---------------------------------------------'
	@echo ' cookiecutter-charlesbot-plugin make targets'
	@echo '---------------------------------------------'
	@echo 'help: This help'
	@echo 'install: Install dependencies'
	@echo 'test: Run tests'

clean:
	py3clean .
	find . -name "__pycache__" -exec /bin/rm -rf {} \;

clean-all: clean
	rm -rf env
	rm -rf charlesbot_helloworld

env: clean
	test -d $(ENV) || pyvenv-3.4 $(ENV)

install: env
	$(ENV)/bin/pip install cookiecutter

test: install
	$(ENV)/bin/cookiecutter . --no-input
	make -C charlesbot_helloworld checkstyle
	make -C charlesbot_helloworld test
