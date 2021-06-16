# Determine this makefile's path.
# Be sure to place this BEFORE `include` directives, if any.
# source: https://stackoverflow.com/a/27132934/7331040
THIS_FILE := $(lastword $(MAKEFILE_LIST))
MANAGE = python manage.py
COMMIT = cz
CHANGELOG = gitchangelog


# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default.";
	@echo "Try 'make help'.";


# target: coverage - Runs tests and creates html report with coverage. You can pass additional arguments with ARGS parameter, eg: 'make coverage ARGS=-k'.
coverage:
	coverage run --rcfile='.coveragerc' manage.py test ${ARGS};
	coverage report;
	coverage html;

build:
	docker-compose -f local.yml build

# target: dev - Builds the project using 'development' settings.
dev:
	docker-compose -f local.yml run --rm django pip install -r requirements/local.txt;
	docker-compose -f local.yml run --rm django $(MANAGE) migrate --settings=config.settings.local;

admin:
	docker-compose -f local.yml run --rm django $(MANAGE) createsuperuser --settings=config.settings.local;

# target: help - Display callable targets.
help:
	@echo "These are common commands used in various situations:\n";
	@grep -E "^# target:" [Mm]akefile;


# target: lint - Checks that python code follows pep8, has docstrings, and imports are sorted properly.
lint:
	@echo "pep8";
	@flake8 apps/* --max-complexity 10;
	@echo "docstrings";
	@pydocstyle apps --count;
	@echo "imports";
	@isort apps --recursive --check-only;


# target: qa - Runs all qa tools.
qa:
	@bandit -ll -r apps;
	@safety check -r requirements/base.txt -r requirements/local.txt -i 37664 -i 38678;
	@$(MAKE) -f $(THIS_FILE) lint;


# target: run - Runs dev server. You can pass additional arguments with ARGS parameter, eg: 'make run ARGS=9000'.
run:
	docker-compose -f local.yml up

# down all service docker
down:
	docker-compose -f local.yml down

init:
	@$(MAKE) -f $(THIS_FILE) build;
	@$(MAKE) -f $(THIS_FILE) dev;

# target: shell - Opens django shell.
shell:
	docker-compose -f local.yml run --rm django $(MANAGE) shell_plus --settings=config.settings.local || $(MANAGE) shell --settings=config.settings.local;

#target: commit - Runs a commitizen commit
commit:
	@$(COMMIT)

#target: changelog - Bump version, generate changelog, commit it with non-conventional log (so it doesnt appear in changelog)
changelog:
	@echo "Bumping version according to commits..."
	@$(COMMIT) bump
	@echo "Generating changelog..."
	@$(CHANGELOG) > CHANGELOG.md
	@echo "Adding and commiting changelog in non-conventional format..."
	@git add CHANGELOG.md
	@git commit -m 'changelog changes'
	@git push --tags
	@echo "Release is ready to be pushed! use git push --follow-tags."

#target: isort found an import in the wrong position
isosrt_run:
	@isort apps --recursive;
