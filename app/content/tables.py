from fastapi import status


delete_store_docs = {
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
                            "loc": ["path", "table_id"],
                            "msg": "value is not a valid integer",
                            "type": "type_error.integer",
                        }
                    ]
                }
            }
        },
    },
}
