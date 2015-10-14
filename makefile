clear:
	touch a.pyc
	touch a.db
	touch a~
	rm *.pyc
	rm *.db
	rm *~
	clear

run:
	python app.py
