# Шифр Виженера

## Описание

Шифр Виженера - это метод полиалфавитного шифрования буквенного текста с использованием ключевого слова.
Это веб приложение позволяет зашифровать и расшифровать текст с помощью шифра Виженера.

## Инструкция

### Для запуска приложения необходимо:
* [Docker](https://docs.docker.com/engine/install/)

### Запуск приложения:
1. Склонировать репозиторий
```bash
git clone https://github.com/MaHryCT3/vigenaire_cipher.git
```
2. Перейти в папку с проектом
```bash
cd vigenaire_cipher
```
3. Если у вас есть Make
```bash
make build
make up
```
4. Если у вас нет Make
```bash
docker build . -t vigenaire
docker run -d --name vigenaire_app -p 8000:8000 vigenaire
```
5. Открываем в браузере http://localhost:8000 и радуемся жизни

