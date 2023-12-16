import uuid

from fastapi import APIRouter

from lavoro_matching_api.services import matches_service


router = APIRouter(prefix="/matches", tags=["matches"])


@router.get("/get-matches-by-applicant/{applicant_account_id}")
def get_matches_by_applicant(applicant_account_id: uuid.UUID):
    return matches_service.get_matches_by_applicant(applicant_account_id)


@router.get("/get-matches-by-job-post/{job_post_id}")
def get_matches_by_job_post(job_post_id: uuid.UUID):
    return matches_service.get_matches_by_job_post(job_post_id)
