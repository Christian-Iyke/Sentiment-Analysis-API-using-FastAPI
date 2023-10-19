
FROM python:3.11

WORKDIR /main

COPY requirements.txt ./

COPY ML_Model.pkl ./

RUN pip install -r requirements.txt 

COPY main.py ./

EXPOSE 8000

CMD ["python", "main:app"]


