ENV=./env

all: help

help:
	@echo '-----------------------------------------'
	@echo ' {{cookiecutter.project_name}} make targets'
	@echo '-----------------------------------------'
	@echo 'help: This help'
	@echo 'install: Install dev dependencies'
	@echo 'test: Run tests'
	@echo 'checkstyle: Run flake8'
	@echo 'run: Run CharlesBOT locally'

# Utility target for checking required parameters
guard-%:
	@if [ "$($*)" = '' ]; then \
     echo "Missing required $* variable."; \
     exit 1; \
   fi;

.PHONY: clean
clean:
	py3clean .
	rm -f .coverage
	find . -name "__pycache__" -exec /bin/rm -rf {} \;

.PHONY: clean-all
clean-all: clean
	rm -rf env
	rm -rf *.egg-info

env: clean
	test -d $(ENV) || pyvenv-3.4 $(ENV)

.PHONY: install
install: env
	$(ENV)/bin/pip install -r requirements-dev.txt
	$(ENV)/bin/pip install -e .

.PHONY: checkstyle
checkstyle: install
	$(ENV)/bin/flake8 --max-complexity 10 {{cookiecutter.package_name}}
	$(ENV)/bin/flake8 --max-complexity 10 tests

.PHONY: test
test: install
	$(ENV)/bin/nosetests \
		-v \
		--with-coverage \
		--cover-package={{cookiecutter.package_name}} \
		tests

.PHONY: run
run:
	PYTHONWARNINGS=default PYTHONASYNCIODEBUG=1 $(ENV)/bin/charlesbot

# e.g. PART=major make release
# e.g. PART=minor make release
# e.g. PART=patch make release
.PHONY: release
release: guard-PART
	$(ENV)/bin/bumpversion $(PART)
	@echo "Now manually run: git push && git push --tags"
