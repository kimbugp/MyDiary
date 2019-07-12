
FROM python:3.7

COPY . .

ENV FLASK_APP app.py
ENV PYTHONUNBUFFERED 1
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install -r requirements.txt
CMD ["gunicorn", "run:app"]