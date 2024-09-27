from fastapi import APIRouter, UploadFile, FastAPI, status, HTTPException
from starlette.responses import JSONResponse
from config.validation_config import OutputFormat
from model.image_recognition import ImageDescriptor
import io
from PIL import Image

# create the app
path = "/compadre-image-recognition"
app = FastAPI(
    title="Image Recognition API",
    description="",
    docs_url=path + "/docs",
    openapi_url=path + "/openapi.json",
)

router = APIRouter(prefix=path)


@router.get(
    "/health/",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 when model is loaded",
    status_code=status.HTTP_200_OK,
)
async def health():
    return JSONResponse(content={"status": "ok"})


@router.post(
    "/generate", status_code=status.HTTP_200_OK, response_model=OutputFormat
)
async def predict(file: UploadFile):
    try:
        return _predict(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)


def _predict(file: UploadFile):
    agent = ImageDescriptor()
    image_data = io.BytesIO(file.file.read())
    return {"description": agent.describe(image_data)}