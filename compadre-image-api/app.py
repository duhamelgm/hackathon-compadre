from fastapi import (
    APIRouter,
    UploadFile,
    FastAPI,
    status,
)
from config.validation_config import OutputFormat

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
)  # TODO depricate once we have migrated to the `1.0/generate` route
def predict(file: UploadFile):
    pass



app.include_router(router)

