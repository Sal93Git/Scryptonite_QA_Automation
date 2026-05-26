FROM ubuntu:24.04


RUN groupadd -r lex && useradd -r -g lex -m -d /home/lex lex

# Set working directory
WORKDIR /usr/src/SCRYPTONITE_QA

# Install system packages in one layer
RUN apt-get update && \
    # apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        python3 python3-pip python3-venv \
        ca-certificates \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy project code and resources to the container
COPY . .

# Create Python virtual environment and install dependencies
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pip_system_certs && \
    /opt/venv/bin/pip install -r requirements.txt

# Install Playwright Chrome driver
RUN /opt/venv/bin/python -m playwright install chrome

# Set permissions
RUN chown -R lex:lex /usr/src/SCRYPTONITE_QA /opt/venv && \
    chmod -R 755 /usr/src/SCRYPTONITE_QA && \
    chmod +x entrypoint.sh

USER lex

# Use virtual environment by default
ENV PATH="/opt/venv/bin:$PATH"

# Define the entrypoint
CMD ["./entrypoint.sh"]
