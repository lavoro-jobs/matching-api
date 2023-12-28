import uuid

from fastapi import HTTPException, status

from lavoro_matching_api.database import queries


def get_applications_to_job_post(job_post_id: uuid.UUID):
    return queries.get_applications_to_job_post(job_post_id)


def approve_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return queries.approve_application(job_post_id, applicant_account_id)


def create_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    match = queries.get_match(job_post_id, applicant_account_id)
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Match not found",
        )
    if match.approved_by_applicant is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Application already exists",
        )

    queries.set_match_approved_by_applicant(job_post_id, applicant_account_id)
    return queries.create_application(job_post_id, applicant_account_id)
