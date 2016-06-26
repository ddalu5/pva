CONTAINER='pva'
ENV_NAME='pva_dev'

all: reload

build:
	@echo -e "[#] Building "$(ENV_NAME)" from "$(CONTAINER)
	docker build -t $(CONTAINER) .

run:
	@echo -e "[#] Running"$(ENV_NAME)
	docker run -d --name $(ENV_NAME) $(CONTAINER)

clean:
	@echo -e "[#] Cleaning "$(ENV_NAME)
	docker stop $(ENV_NAME)
	docker rm $(ENV_NAME)

start:
	@echo -e "[#] Starting "$(ENV_NAME)
	docker start $(ENV_NAME)

reload: clean build run start
	@echo -e "########## ALL OPS ARE DONE ##########"
