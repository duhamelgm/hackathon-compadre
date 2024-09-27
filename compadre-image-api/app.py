from fastapi import APIRouter, UploadFile, FastAPI, status, HTTPException
from starlette.responses import JSONResponse
from config.validation_config import OutputFormat
from model.image_recognition import ImageDescriptor
import io
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

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

async def unhandled_exception_handler(request: Request, exc: Exception) -> PlainTextResponse:
    """
    This middleware will log all unhandled exceptions.
    Unhandled exceptions are all exceptions that are not HTTPExceptions or RequestValidationErrors.
    """
    logger.debug("Our custom unhandled_exception_handler was called")
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    exception_type, exception_value, exception_traceback = sys.exc_info()
    exception_name = getattr(exception_type, "__name__", None)
    logger.error(
        f'{host}:{port} - "{request.method} {url}" 500 Internal Server Error <{exception_name}: {exception_value}>'
    )
    logger.error(
        f'{exception_traceback}'
    )
    return PlainTextResponse(str(exc), status_code=500)
app.add_exception_handler(Exception, unhandled_exception_handler)

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