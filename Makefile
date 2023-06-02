install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


publish:
	 poetry publish --dry-run


package-install:
	 python3 -m pip install --user dist/*.whl



package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
	

package-uninstall:
	python3 -m pip uninstall hexlet-code


lint:
	poetry run flake8 --config=config.cfg brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime