CONTAINER='pva'
ENV_NAME='pva_dev'
ECHO_NORMAL=$(@echo -e "\e[0m")
ECHO_TITLE=$(@echo -e "\e[33m")
ECHO_INFO=$(@echo -e "\e[33m")

all: reload

build:
	@echo -e "\e[33m[#] Building "$(ENV_NAME)" from "$(CONTAINER)
	@echo -e "\e[0m"
	docker build -t $(CONTAINER) .

run:
	@echo -e "\e[33m[#] Running"$(ENV_NAME)
	@echo -e "\e[0m"
	docker run -d --name $(ENV_NAME) $(CONTAINER)

clean:
	@echo -e "\e[33m[#] Cleaning "$(ENV_NAME)
	@echo -e "\e[0m"
	docker stop $(ENV_NAME)
	docker rm $(ENV_NAME)

start:
	@echo -e "\e[33m[#] Starting "$(ENV_NAME)
	@echo -e "\e[0m"
	docker start $(ENV_NAME)

reload: clean build run start
	@echo -e "\e[1m\e[34m########## ALL OPS ARE DONE ##########"
	@echo -e "\e[0m"

test:
	ccred=$(bash echo -e "\033[0;31mHahaha")
	$(ccred)
	@echo -e "\e[0m"
