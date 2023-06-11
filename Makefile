build:
	docker build -t vigenaire

up:
	docker run -d --name vigenaire_app -p 80:80 vigenaire

down:
	docker stop vigenaire_app