# Get the bitnami spark image
FROM bitnami/spark:latest
USER root
# Install Python libraries 
COPY ./NAaaS/Spark/requirements.txt requirements.txt
COPY ./NAaaS/Spark/Alldata_refined.csv /opt/bitnami/spark/alldata_refined.csv 
RUN pip install -r requirements.txt
RUN [ "python", "-c", "import spacy; spacy.cli.download('en_core_web_sm')" ]
RUN [ "python", "-c", "import nltk; nltk.download('wordnet')" ]
RUN apt update -y
