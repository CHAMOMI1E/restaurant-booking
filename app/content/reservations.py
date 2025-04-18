from fastapi import status


get_reservations_docs = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Ошибка сервера",
        "content": {
            "application/json": {
                "example": {"message": "Ошибка сервера, попробуйте попытку позже"}
            }
        },
    },
}


delete_reservation_docs = {
    status.HTTP_204_NO_CONTENT: {"description": "Успешное удаление", "content": None},
    status.HTTP_404_NOT_FOUND: {
        "description": "Объект не найден",
        "content": {"application/json": {"example": {"message": "Не найдено"}}},
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Ошибка сервера",
        "content": {
            "application/json": {
                "example": {"message": "Ошибка сервера, попробуйте попытку позже"}
            }
        },
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "description": "Ошибка валидации",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["reservation_id"],
                            "msg": "value is not a valid integer",
                            "type": "type_error.integer",
                        }
                    ]
                }
            }
        },
    },
}


add_reservation_docs = {
    status.HTTP_200_OK: {
        "description": "Успешное добавление данных",
        "content": {
            "application/json": {
                "example": {
                    "customer_name": "Имя",
                    "table_id": 1,
                    "reservation_time": "2025-04-17T13:17:49.282Z",
                    "duration_minutes": 1,
                    "id": 0,
                }
            }
        },
    },
    status.HTTP_404_NOT_FOUND: {
        "description": "Объект не найден",
        "content": {"application/json": {"example": {"message": "Не найдено"}}},
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Ошибка сервера",
        "content": {
            "application/json": {
                "example": {"message": "Ошибка сервера, попробуйте попытку позже"}
            }
        },
    },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "description": "Ошибка валидации",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["table_id"],
                            "msg": "value is not a valid integer",
                            "type": "type_error.integer",
                        }
                    ]
                }
            }
        },
    },
}
