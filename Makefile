build:
	docker build . -t vigenaire

start:
	docker start vigenaire_app

up:
	docker run -d --name vigenaire_app -p 8000:8000 vigenaire

down:
	docker stop vigenaire_app