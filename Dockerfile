# Use an official Python image
FROM python:3.13-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app


# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/sbslee/streamlit-openai.git xxxx
RUN git clone --branch 0.1.3-dev https://github.com/sbslee/streamlit-openai.git xxxx
WORKDIR /app/xxxx
RUN mv streamlit_openai ../
#RUN ls -lR
WORKDIR /app

# Copy application files
COPY app.py .
#COPY chat.py streamlit_openai/chat.py

RUN ls -lR

# Run the Streamlit app
#CMD ["streamlit", "run", "app.py", "--server.baseUrlPath=\"/chat/\"", "--server.fileWatcherType", "none" ]
CMD ["streamlit", "run", "app.py", "--server.runOnSave=false"]
