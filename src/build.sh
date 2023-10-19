docker build . -t Sepsis_Sentiment_Analysis_API: latest 

docker images

docker run -p 8080:8000 --name Sepsis_Sentiment_Analysis_API image_id

docker ps