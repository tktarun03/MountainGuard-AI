.PHONY: start stop normal sensor-failure gradual-instability seismic-river multi-hazard tests

start:
	docker compose up --build

stop:
	docker compose down

normal:
	python scripts/run_scenario.py normal

sensor-failure:
	python scripts/run_scenario.py sensor-failure

gradual-instability:
	python scripts/run_scenario.py gradual-instability

seismic-river:
	python scripts/run_scenario.py seismic-river

multi-hazard:
	python scripts/run_scenario.py multi-hazard

tests:
	pytest -q
