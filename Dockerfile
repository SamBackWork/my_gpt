FROM python:3.12-alpine
LABEL authors="SamBackWork"

COPY . /my_gpt
WORKDIR /my_gpt
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "main.py"]