from fastapi import status


delete_table_docs = {
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


get_table_docs = {
    status.HTTP_200_OK: {
        "description": "Успешное получение данных",
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 0,
                        "name": "Название столика",
                        "seats": 1,
                        "location": "Местонахождение",
                    }
                ]
            }
        },
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Ошибка сервера",
        "content": {
            "application/json": {
                "example": {"message": "Ошибка сервера, попробуйте попытку позже"}
            }
        },
    },
}


add_table_docs = {
    status.HTTP_200_OK: {
        "description": "Успешное добавление данных",
        "content": {
            "application/json": {
                "example": {
                    "id": 0,
                    "name": "Название столика",
                    "seats": 1,
                    "location": "Местонахождение",
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
