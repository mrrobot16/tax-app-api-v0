FROM python:3.11.4

WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Install Doppler CLI
RUN curl -Ls https://cli.doppler.com/install.sh | sh

# # Copy the rest of the application code from the 'app' directory
# COPY app/ .
# COPY app/ /app/
# COPY . /app/

EXPOSE 8000

# Use Doppler to inject environment variables and start the application
ENTRYPOINT ["doppler", "run", "--"]
CMD ["uvicorn", "main:app", "--reload"]

# Use the command below if you want to run with gunicorn
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000", "--timeout", "120"]
