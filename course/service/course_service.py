import logging
import course.database.db_handlers.course_db_handler as course_db_handler
from course.models.course_models import CourseCreate, CourseCreationProfile
import random

LOGGER = logging.getLogger(__file__)



async def create_course(course_create: CourseCreate, userID: int, **kwargs):
    try:
        
        return await course_db_handler.create_course(
            duration=course_create.course_duration,
            description=course_create.course_description,
            title=course_create.course_title,
            price=course_create.price,
            tutor_uid=userID
        )
    except:
        ...
