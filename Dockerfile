FROM continuumio/anaconda3:4.4.0
COPY . C:/Users/i340968/Downloads/Docker_Implementation
EXPOSE 5000
WORKDIR C:/Users/i340968/Downloads/Docker_Implementation
RUN pip install -r requirements.txt
CMD python app_flassger.py