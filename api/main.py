from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordBearer
from routers.appll import custom_router, count_router


from db.base import metadata, engine, database

from repositories.admins import *



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost", 
    "http://el-bazaar.kz"
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

metadata.create_all(engine)

app.state.database = database

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/jwt")

   
app.include_router(
    custom_router
    )

app.include_router(
    count_router
    
)
    


app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/api/v1/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/api/v1/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(
        settings.secret, after_forgot_password=on_after_forgot_password
    ),
    prefix="/api/v1/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(
        settings.secret, after_verification_request=after_verification_request
    ),
    prefix="/api/v1/auth",
    tags=["auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/api/v1/users", tags=["users"])