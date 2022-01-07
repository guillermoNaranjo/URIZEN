FROM python:3.8.10
WORKDIR /api_py
ADD . /api_py
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
