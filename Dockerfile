FROM ubuntu:latest 

USER root

# Install Python and other necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    ca-certificates \
    fonts-noto-color-emoji \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get upgrade -y && \
    apt-get install -y curl vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#Install chromium
RUN apt-get update && \
    apt-get install -y \
    chromium-browser \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/src/SCRYPTONITE_QA

# Copy project code and resources in the to container working directory
COPY . .

# Create python virtual environment and install dependencies
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pip_system_certs && \
    /opt/venv/bin/pip install -r requirements.txt

# Install Playwright chrome driver
RUN /opt/venv/bin/python -m playwright install chrome

RUN chmod -R 755 /usr/src/SCRYPTONITE_QA

RUN chmod +x entrypoint.sh

# Set the environment variable to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Define the command to run the application
CMD ["./entrypoint.sh"]
