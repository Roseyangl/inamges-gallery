FROM python:3.10

WORKDIR /app

EXPOSE 5050

RUN pip install pipenv 
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

RUN pip install pymongo

COPY . ./

CMD ["python", "main.py"]
