from fastapi import APIRouter

from app.config.db import database
# from app.api.example.updateExample import update_jurusan, UpdateJurusanResponse


api_router = APIRouter()


@api_router.on_event('startup')
async def startup():
    await database.connect()


@api_router.on_event('shutdown')
async def shutdown():
    await database.disconnect()

# api_router.add_api_route('/v1/jurusan/{id}', update_jurusan,
#                          methods=['PUT'], tags=['Jurusan'], response_model=UpdateJurusanResponse, status_code=201)
