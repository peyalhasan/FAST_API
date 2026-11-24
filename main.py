from fastapi import FastAPI


app = FastAPI()

notes = [
     {
        "id": 1,
        "term": "variable",
        "definition": "A name that stores a value",
        "js_equivalent": "let x = 5;",
        "tags": ["python", "basics"],
        "learned": True
    },
    {
        "id": 2,
        "term": "list",
        "definition": "A collection of items",
        "js_equivalent": "let myArray = [1, 2, 3];",
        "tags": ["python", "basics"],
        "learned": True,
    },
    {
        "id": 3,
        "term": "dictionary",
        "definition": "A collection of key-value pairs",
        "js_equivalent": "let myObject = {key: 'value'};",
        "tags": ["python", "basics"],
        "learned": False,
    },
    {
        "id": 4,
        "term": "function",
        "definition": "A block of code that performs a task",
        "js_equivalent": "function myFunction() { return 'Hello'; }",
        "tags": ["python", "basics"],
        "learned": False,
    }
]

# "/terms" = the path 
# get = theHTTP operation
# Path + operation = path operation
# @line = a decorator#
@app.get("/")
def root():
    return {"message": "Learning Notebook API is running!"}

@app.get("/terms")
def get_terms():
    return notes