from uuid import UUID

# from sqlalchemy import update, insert, select, delete, insert
from course.database.db_models.course_orm import Course as CourseDb

from course.models.course_models import CourseCreationProfile
import logging
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, OperationalError

from course.database.db_models.course_orm import database
from course.service.service_exceptions import NotFound, UpdateError

LOGGER = logging.getLogger(__file__)


async def create_course(price, duration, description, title, tutor_uid: int, **kwargs):
    query = CourseDb.insert().values(
        tutor_uid=int(tutor_uid),
        title=title,
        description=description,
        duration=duration,
        price=price,
    )
    try:
        # print(query)
        await database.execute(query)
        
        return CourseCreationProfile(message="successfully created Course")
    except OperationalError as e:
        raise e
  