CONTAINER=pva
ENV_NAME=pva_dev

all: reload test

build:
	@echo "[#] Building "$(ENV_NAME)" from "$(CONTAINER)
	docker build -t $(CONTAINER) .

run:
	@echo "[#] Running"$(ENV_NAME)
	docker run -itd --name $(ENV_NAME) -v /opt/pva:/root/daril/projects/ $(CONTAINER)

clean:
	@echo "[#] Cleaning "$(ENV_NAME)
	docker stop $(ENV_NAME)
	docker rm $(ENV_NAME)

start:
	@echo "[#] Starting "$(ENV_NAME)
	docker start $(ENV_NAME)

reload: clean build run start
	@echo "########## ALL OPS ARE DONE ##########"

execute:
	docker exec $(ENV_NAME) python pva/pva.py

test:
	docker exec $(ENV_NAME) nosetests --nocapture --verbosity=3 pva/tests/
