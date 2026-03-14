FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Create non-root user
RUN useradd appuser

# Switch to non-root user
USER appuser

# Expose service port
EXPOSE 5000

# Run the service
CMD ["flask", "run", "--host=0.0.0.0"]
