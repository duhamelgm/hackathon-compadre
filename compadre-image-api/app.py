from fastapi import APIRouter, UploadFile, FastAPI, status, HTTPException, Form, Request
from starlette.responses import JSONResponse
from config.validation_config import (
    DescriptionOutputFormat,
    # ComparatorInputFormat,
    ComparatorOutputFormat
)
import json
import logging
from ast import literal_eval
from model.image_description import ImageDescriptor
from model.image_comparison import ImageComparator
import io
import sys
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

# create the app
path = "/compadre-image-recognition"
app = FastAPI(
    title="Image Recognition API",
    description="",
    docs_url=path + "/docs",
    openapi_url=path + "/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    "/generate", status_code=status.HTTP_200_OK, response_model=DescriptionOutputFormat
)
async def predict(file: UploadFile):
    try:
        return _predict(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/compare", status_code=status.HTTP_200_OK, response_model=ComparatorOutputFormat
)
async def compare(file:UploadFile, payload: str = Form(...)):
    print(file)
    print(payload)
    try:
        return _compare(file, payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception) -> PlainTextResponse:
    """
    This middleware will log all unhandled exceptions.
    Unhandled exceptions are all exceptions that are not HTTPExceptions or RequestValidationErrors.
    """
    print("Our custom unhandled_exception_handler was called")
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    exception_type, exception_value, exception_traceback = sys.exc_info()
    exception_name = getattr(exception_type, "__name__", None)
    print(
        f'{host}:{port} - "{request.method} {url}" 500 Internal Server Error <{exception_name}: {exception_value}>'
    )
    print(
        f'{exception_traceback}'
    )
    return PlainTextResponse(str(exc), status_code=500)

app.include_router(router)


def _predict(file: UploadFile):
    image_descriptor = ImageDescriptor()
    image_data = io.BytesIO(file.file.read())
    return {"description": image_descriptor.describe(image_data)}

def _compare(file:UploadFile ,payload):
    logging.info("_compare")
    image_data = io.BytesIO(file.file.read())
    file.file.close()
    image_comparator = ImageComparator()
    payload = literal_eval(payload)
    return {"response": image_comparator.compare(image_data, payload["image_list"])}
    