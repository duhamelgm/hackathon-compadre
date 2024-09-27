from fastapi import (
    APIRouter,
    UploadFile,
    FastAPI,
    status,
)
from config.validation_config import OutputFormat
from model.image_recognition import ImageDescriptor

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
def health():
    return True


@router.post(
    "/generate", status_code=status.HTTP_200_OK, response_model=OutputFormat
)
def predict(file: UploadFile):
    return _predict(file)



app.include_router(router)

def _predict(file):
    agent = ImageDescriptor()
    return {"description":agent.describe(file)}