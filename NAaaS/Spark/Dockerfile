# Get the bitnami spark image
FROM bitnami/spark:latest
USER root

# Install Python libraries 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN [ "python", "-c", "import nltk; nltk.download('wordnet')" ]
RUN apt update -y

# Copy all files from the current directory to the working directory in the Docker image
COPY . /opt/bitnami/spark/

# Move the Alldata_refined.csv file to the desired location
RUN mv /opt/bitnami/spark/Alldata_refined.csv /opt/bitnami/spark/alldata_refined.csv
