# Use the official Jenkins image as a base
FROM jenkins/jenkins:lts-jdk17

# Switch to root user for installation
USER root

# Install wget, Miniconda, and other dependencies
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /usr/local/miniconda3 && \
    rm miniconda.sh && \
    /usr/local/miniconda3/bin/conda init

# Switch back to Jenkins user
USER jenkins

# Copy the Jenkins job scripts and Conda environment YAML file into the image
COPY conda_env.yml /usr/local/jenkins/conda_env.yml
COPY jenkins_job.xml /usr/local/jenkins/jenkins_job.xml

# Install Conda environment and dependencies
RUN /usr/local/miniconda3/bin/conda env create -f /usr/local/jenkins/conda_env.yml

# Start Jenkins
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]
