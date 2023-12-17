import uuid

from lavoro_matching_api.database import queries


def get_matches_by_applicant(applicant_account_id: uuid.UUID):
    matches = queries.get_matches_by_applicant(applicant_account_id)
    return matches


def get_matches_by_job_post(job_post_id: uuid.UUID):
    matches = queries.get_matches_by_job_post(job_post_id)
    return matches


def reject_match(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return queries.reject_match(job_post_id, applicant_account_id)
