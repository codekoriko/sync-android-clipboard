SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy sync_android_clipboard tests/**/*.py
	poetry run flake8 ./sync_android_clipboard

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint package unit

