FROM python:3.8-slim
ENV PORT=80
EXPOSE $PORT
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
CMD streamlit run --server.port $PORT app.py