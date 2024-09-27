from fastapi import FastAPI
from compadre_products.scrappers import amazon

app = FastAPI()


@app.get("/")
async def root():
    return await amazon.main()