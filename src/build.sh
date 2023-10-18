docker build . -t Sepsis_Sentiment_Analysis_API: latest 

docker images

docker run -p 8000:7685 --name Sepsis_Sentiment_Analysis_API image_id

docker ps