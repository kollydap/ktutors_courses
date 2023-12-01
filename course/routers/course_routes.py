from fastapi import APIRouter, status, Body, Depends
from course.models.course_models import CourseCreate, CourseCreationProfile
from typing import Annotated
from pydantic import EmailStr
import course.service.course_service as course_service
from course.routers.course_utils import get_refresh_token, verify_token_return_userid

AnEmail = Annotated[EmailStr, Body(embed=True)]
AnToken = Annotated[str, Body(embed=True)]
AnRefreshToken = Annotated[str, Depends(get_refresh_token)]


api_router = APIRouter(tags=["Courses"], prefix="/api/v1/course")


@api_router.post("/create", response_model=CourseCreationProfile)
async def create_course(
    course_create: CourseCreate, userID: str = Depends(verify_token_return_userid)
):
    return await course_service.create_course(
        course_create=course_create, userID=userID
    )
