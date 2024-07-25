FROM python:3.12.4-bookworm

# Configure apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
# RUN apt-get -y install git procps lsb-release

# Install any missing dependencies for enhanced language service
# RUN apt-get install -y libicu[0-9][0-9]

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/
COPY ./ /app/
RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/10.15.0/flyway-commandline-10.15.0-linux-x64.tar.gz | tar xvz && \
    mv flyway-10.15.0 /flyway && \
    ln -s /flyway/flyway /usr/local/bin

RUN wget -O /tmp/sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-6.1.0.4477-linux-x64.zip && \
    unzip /tmp/sonar-scanner-cli.zip -d /opt && \
    rm /tmp/sonar-scanner-cli.zip

ENV PATH="/opt/sonar-scanner-6.1.0.4477-linux-x64/bin:${PATH}"

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

ENV SHELL /bin/bash

# CMD ["bash"]
# CMD ["python", "app.py"]

CMD ["sleep", "infinity"]

