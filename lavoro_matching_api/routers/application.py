import uuid

from fastapi import APIRouter
from lavoro_library.model.matching_api.dtos import CreateCommentDTO

from lavoro_matching_api.services import application_service


router = APIRouter(prefix="/application", tags=["application"])


@router.get("/get-applications-to-job-post/{job_post_id}")
def get_applications_to_job_post(job_post_id: uuid.UUID):
    return application_service.get_applications_to_job_post(job_post_id)


@router.get("/get-created-applications-by-applicant/{applicant_account_id}")
def get_created_applications_by_applicant(applicant_account_id: uuid.UUID):
    print(applicant_account_id)
    return application_service.get_created_applications_by_applicant(applicant_account_id)


@router.post("/approve-application/{job_post_id}/{applicant_account_id}")
def approve_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return application_service.approve_application(job_post_id, applicant_account_id)


@router.post("/reject-application/{job_post_id}/{applicant_account_id}")
def reject_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return application_service.reject_application(job_post_id, applicant_account_id)


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


@router.get("/get-comments-on-application/{job_post_id}/{applicant_account_id}")
def get_comments_on_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return application_service.get_comments_on_application(job_post_id, applicant_account_id)


@router.delete("/delete-comment/{job_post_id}/{comment_id}")
def delete_comment(
    job_post_id: uuid.UUID,
    comment_id: uuid.UUID,
):
    return application_service.delete_comment(job_post_id, comment_id)
