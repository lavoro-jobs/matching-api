import uuid

from fastapi import APIRouter

from lavoro_matching_api.services import application_service


router = APIRouter(prefix="/application", tags=["application"])


@router.post("/get-applications-to-job-post/{job_post_id}")
def get_applications_to_job_post(job_post_id: uuid.UUID):
    return application_service.get_applications_to_job_post(job_post_id)


@router.post("/approve-application/{job_post_id}/{applicant_account_id}")
def approve_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return application_service.approve_application(job_post_id, applicant_account_id)
