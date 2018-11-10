default:
	rm -Rf migrations
	rm -f 500weeks.db
	sqlite3 500weeks.db "VACUUM;"
	python migrate.py db migrate
	python migrate.py db upgrade
	cat data.sql | sqlite3 500weeks.db
