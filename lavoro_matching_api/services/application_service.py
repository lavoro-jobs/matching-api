import uuid

from fastapi import HTTPException, status
from lavoro_library.model.matching_api.dtos import CreateCommentDTO

from lavoro_matching_api.database import queries


def get_applications_by_job_post(job_post_id: uuid.UUID):
    return queries.get_applications_by_job_post(job_post_id)


def get_created_applications_by_applicant(applicant_account_id: uuid.UUID):
    return queries.get_created_applications_by_applicant(applicant_account_id)


def approve_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    application = queries.get_application(job_post_id, applicant_account_id)
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return queries.approve_application(job_post_id, applicant_account_id)


def reject_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    application = queries.get_application(job_post_id, applicant_account_id)
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return queries.reject_application(job_post_id, applicant_account_id)


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


def comment_application(
    job_post_id: uuid.UUID, applicant_account_id: uuid.UUID, current_recruiter_id: uuid.UUID, payload: CreateCommentDTO
):
    application = queries.get_application(job_post_id, applicant_account_id)
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return queries.create_comment(job_post_id, applicant_account_id, current_recruiter_id, payload)


def get_comments_on_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    application = queries.get_application(job_post_id, applicant_account_id)
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    comments = queries.get_comments_on_application(job_post_id, applicant_account_id)
    return comments


def delete_comment(job_post_id: uuid.UUID, comment_id: uuid.UUID):
    comment = queries.get_comment(comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found",
        )
    if comment.job_post_id != job_post_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment does not belong to this job post",
        )

    return queries.delete_comment(comment_id)
