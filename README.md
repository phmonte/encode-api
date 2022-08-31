## API - Encode|Decode 

This project is an api with the objective of creating an encode for an integer of up to 8 characters, generating a hash/code with a fixed length of 6 characters.

To create the code/hash, the conversion to decimal hex was used.

## Technologies
- Fast API (https://fastapi.tiangolo.com/)
## How to run?

#### 1 - docker build -t myimage .

#### 2 - docker run -d --name mycontainer -p 80:80 myimage

#### 3 - http://127.0.0.1/docs

## Project Structure
    .
    ├── .gitignore              # Specifies intentionally untracked files to ignore
    ├── Dockerfile              # Dockerfile reference
    ├── hash_script.py          # Script with rules for decode encode
    ├── main.py                 # Main project
    ├── requirements.txt        # Requirements files, are files containing a list of items to be installed using pip install
    ├── test_main.http          # Test of the edpoints
    └── README.md               # Markdown file with project instructions.

why use hex?: https://www.youtube.com/watch?v=cVEj5p9GiBA