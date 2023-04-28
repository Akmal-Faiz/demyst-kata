from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.routes import loan_application
from starlette.requests import Request
from starlette.responses import Response


app = FastAPI()

app.include_router(loan_application.router)

# Configure CORS middleware

# CORS and custom error handling ref: https://github.com/tiangolo/fastapi/issues/775#issuecomment-592946834


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except ValueError as exc:
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )
    except Exception as exc:
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)},
        )

app.middleware('http')(catch_exceptions_middleware)


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.exception_handler(Exception)
# async def http_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=500,
#         content={"detail": str(exc)},
#     )
