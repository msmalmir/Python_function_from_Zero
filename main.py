# writing a fasapli to show the results of the wiki search in the browser
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from pydantic import BaseModel
from mylib.bot import scrape

app = FastAPI()


class Wiki(BaseModel):
    name: str


@app.post("/wiki")
async def wiki_search(wiki: Wiki):
    """
    Search for a wiki page and return the results.
    """

    result = scrape(wiki.name)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/")
async def root():
    """
    Root endpoint to check if the server is running.
    """
    return {"message": "Welcome to the Wiki Search API!"}


if __name__ == "__main__":
    """
    Run the FastAPI application.
    """
    uvicorn.run(app, port=8000, host="0.0.0.0")
