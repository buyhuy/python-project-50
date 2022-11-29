build:
		poetry build

install:
		poetry install

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
		poetry run flake8 gendiff


json-gendiff:
		poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

yaml-gendiff:
		poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml

test:
		poetry run pytest
