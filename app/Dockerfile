# Base Image
FROM python:3.9-slim

# Base Rule
RUN adduser --disabled-password myuser
WORKDIR /app
COPY requirements.txt .

# Requirements
#RUN pip install Flask

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# setting
ENV APP_VERSION=1.0

USER myuser
#CMD ["python", "app.py"]
CMD ["python", "app_v2.py"]
