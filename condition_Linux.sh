if [ -d ".venv" ]; then
	. .venv/bin/activate
else
	sudo install python3-venv
	python3 -m venv .venv
	. .venv/bin/actevate
	pip install -r requirements.txt
fi
python3 main.py
