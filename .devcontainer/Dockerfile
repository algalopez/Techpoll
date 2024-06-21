FROM python:3.12.4-bookworm

# Install pylint
RUN pip install pylint

# Configure apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
# RUN apt-get -y install git procps lsb-release

# Install any missing dependencies for enhanced language service
# RUN apt-get install -y libicu[0-9][0-9]

RUN mkdir /app
WORKDIR /app

# Install Python dependencies from requirements.txt if it exists
COPY ./requirements.txt /app/
COPY ./ /app/
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash

# CMD ["bash"]
# CMD ["python", "app.py"]

CMD ["sleep", "infinity"]

