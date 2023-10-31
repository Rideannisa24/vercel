from fastapi import FastAPI, HTTPException, Header

app = FastAPI()


# uvicorn (nama.py(w/o.py)):app --reload
# request
# - url
# - header
#   - key
# - body
#   - json 


# key yang perlu dimasukkan ke dalam header
key = 'hactiv8mania2023'

# public
@app.get('/')
def helloFunction():
    return {
        "message": "Hello World"
    }

#secret -> harus memasukkan authentification
@app.get('/secret')
def helloFunction(api_key: str = Header(None)):
    # check api_key dari header
    if api_key is None or api_key != key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {
        "message": "secret message"
    }
