build:
		poetry build

install:
		poetry install

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
		poetry run flake8 project_50

gendiff:
		poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

test:
		poetry run pytest
