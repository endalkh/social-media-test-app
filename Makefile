MANAGE = python manage.py

help:
	@echo "help               -- Print this help showing all commands.         "
	@echo "up                 -- Run the webserver.                            "
	@echo "                      Ex. make manage CMD=\"migrate\"               "
	@echo "dumpdata           -- Run django manage.py dumpdata command         "
	@echo "loaddata           -- Run dango manage.py loaddata comand           "
	@echo "test               -- run all tests                                 "
	@echo "migrate            -- prepare migrations and migrate                "
	@echo "admin              -- Create superuser"


dumpdata:
	$(COMPOSE) run --rm app python3 manage.py dumpdata ${app} --indent 4 > ${fixturepath} 

loaddata:
	$(COMPOSE) run --rm app python3 manage.py loaddata ${fixturepath} --app ${app}

up:
	${MANAGE} runserver 0.0.0.0:8000

test:
	${MANAGE} test ${app}

admin:
	${MANAGE} createsuperuser --email=admin@gmail.com --name=admin

migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate

startapp:
	${MANAGE} startapp ${name}
	${MANAGE} migrate