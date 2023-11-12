#used small image
FROM python:3.11-slim-buster
#setting up a workdir
WORKDIR /app
#installing requirements.txt 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
#copying all files
COPY . .
#setting up a port
EXPOSE 8501
ENV PORT=8501
#to run streamlit app
CMD streamlit run chatbot.py --server.port $PORT
