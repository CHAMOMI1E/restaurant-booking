from typing import List, Any, Dict
from sqlalchemy import select, desc, update, delete
from sqlalchemy.exc import SQLAlchemyError, MultipleResultsFound
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


class BaseDAO:
    model = None
    pydantic_model = None

    @classmethod
    async def add(cls, session: AsyncSession, **values):
        new_instance = cls.model(**values)
        session.add(new_instance)

        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
        return new_instance

    @classmethod
    async def add_many(cls, session: AsyncSession, instances: List[Dict[str, Any]]):
        new_instances = [cls.model(**values) for values in instances]
        session.add_all(new_instances)

        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
        return new_instances

    @classmethod
    async def get_one_or_none(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)

        result = await session.execute(query)

        try:
            record = result.unique().scalar_one_or_none()
        except MultipleResultsFound:
            return None

        if record:
            return record
        return None

    @classmethod
    async def get_all(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by).order_by(desc(cls.model.id))
        result = await session.execute(query)
        records = result.unique().scalars().all()
        return records

    @classmethod
    async def edit(
        cls,
        session: AsyncSession,
        filter_by: Dict[str, Any],
        update_values: Dict[str, Any],
    ):
        query = update(cls.model).filter_by(**filter_by).values(**update_values)
        result = await session.execute(query)
        try:
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
        return result

    @classmethod
    async def delete_base(cls, session: AsyncSession, **filter_by):
        query = delete(cls.model).filter_by(**filter_by).returning(cls.model)
        result = await session.execute(query)
        try:
            await session.commit()
            r = result.scalar_one_or_none()
            if r:
                return r
            else:
                raise HTTPException(status_code=404, detail={"message": "Не найдено"})
        except SQLAlchemyError:
            await session.rollback()
            raise HTTPException(
                status_code=500,
                detail={"message": "Ошибка сервера, попробуйте попытку позже"},
            )
