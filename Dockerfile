FROM python:3.8-slim
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD streamlit run --server.port $PORT app.py