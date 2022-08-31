from fastapi import FastAPI, Response, status, HTTPException
from hash_script import encode_number, decode_to_number

tags_metadata = [
    {
        "name": "encode",
        "description": "Endpoint used to encode an integer value with a maximum length of 8 characters.",
    },
    {
        "name": "decode",
        "description": "Endpoint used to decode an integer value previously sent and returned from the endpoint to encode.",
    },
]

app = FastAPI(
    title="Shape",
    description="API used to encode an integer value of up to 8 characters",
    version="1.0.0",
    contact={
        "name": "Pablo Monteiro",
        "email": "pablohenriquem@hotmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


@app.get("/encode/{number}", tags=["encode"])
async def encode(number: int, response: Response):
    try:
        if number > 99999999:
            response.status_code = status.HTTP_400_BAD_REQUEST
            raise HTTPException(status_code=400, detail="The number cannot be greater than 99999999")

        return encode_number(number).rjust(8, '0')
    except Exception:
        raise HTTPException(status_code=500, detail="An error occurred while enncoding")


@app.get("/decode/{code}", tags=["decode"])
async def decode(code: str):
    try:
        return decode_to_number(code)
    except Exception:
        raise HTTPException(status_code=500, detail="An error occurred while decoding")
