FROM python:3.10

WORKDIR /app

EXPOSE 5050


RUN pip install pipenv 
COPY Pipfile Pipfile.lock ./

RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "main.py"]