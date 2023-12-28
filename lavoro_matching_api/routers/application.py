import uuid

from fastapi import APIRouter
from lavoro_library.model.matching_api.dtos import CreateCommentDTO

from lavoro_matching_api.services import application_service


router = APIRouter(prefix="/application", tags=["application"])


@router.post("/create-application/{job_post_id}/{applicant_account_id}")
def create_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return application_service.create_application(job_post_id, applicant_account_id)


@router.post("/comment-application/{current_recruiter_id}/{job_post_id}/{applicant_account_id}")
def comment_application(
    job_post_id: uuid.UUID, applicant_account_id: uuid.UUID, current_recruiter_id: uuid.UUID, payload: CreateCommentDTO
):
    return application_service.comment_application(
        job_post_id, applicant_account_id, current_recruiter_id, payload.comment_body
    )
