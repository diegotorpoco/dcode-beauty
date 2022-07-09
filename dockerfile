
FROM python:3.8.12-buster

COPY api /api
COPY requirements.txt /requirements.txt
COPY dcodebeauty /dcodebeauty
COPY models /models
COPY data /data
#COPY . / dcodebeauty

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

CMD uvicorn api.app:app --host 0.0.0.0 --port 8000
