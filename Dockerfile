FROM python:3
WORKDIR /usr/src/app
COPY random_number_generator/* .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 81