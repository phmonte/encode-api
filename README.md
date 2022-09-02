## API - encode and decode 

This project is an api with the objective of creating an encode for an integer of up to 8 characters, generating a hash/code with a fixed length of 6 characters.

To create the code/hash, the conversion to decimal hex was used.

## Technologies
- Python (https://www.python.org/)
- Fast API (https://fastapi.tiangolo.com/)

## Reasons to use hex:
https://www.youtube.com/watch?v=cVEj5p9GiBA

## How to run the api project:

    docker compose up web

Swagger url: http://127.0.0.1/docs

## How to run the tests:

    docker compose up test


## How to generate a docker image:

    docker build -t myimage .

    docker run -d --name mycontainer -p 80:80 myimage

Swagger url: http://127.0.0.1/docs


## Project structure:

``` text
ROOT
┣ 📂 src
┃ ┣ __init__.py 
┃ ┣ hash_script.py          # Dockerfile reference
┃ ┣ main.py                 # Main project
┣ 📂 test
┃ ┣ __init__.py
┃ ┣ test_main.py            # Test of the edpoints
┣ .coveragerc               # Coverage configuration
┣ Dockerfile                # Dockerfile reference
┣ README.md                 # Markdown file with project instructions.
┣ .gitignore                # Specifies intentionally untracked files to ignore
┣ requirements.txt          # Requirements files, are files containing a list of items to be installed using pip install
```
