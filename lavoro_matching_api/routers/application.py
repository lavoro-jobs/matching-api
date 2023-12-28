import uuid

from fastapi import APIRouter

from lavoro_matching_api.services import application_service


router = APIRouter(prefix="/application", tags=["application"])


@router.post("/create-application/{job_post_id}/{applicant_account_id}")
def create_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return application_service.create_application(job_post_id, applicant_account_id)
