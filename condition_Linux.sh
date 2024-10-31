if [ -d ".venv" ]; then
	. .venv/bin/activate
else
	sudo apt-get install python3-venv
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt
fi
python3 main.py
