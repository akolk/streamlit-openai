# Use an official Python image
FROM python:3.13-slim

# Set work directory
WORKDIR /app
COPY .streamlit  .streamlit
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
