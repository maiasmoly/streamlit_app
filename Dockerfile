FROM python:3.8

WORKDIR /app
COPY requirements.txt /app
COPY app.py /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]