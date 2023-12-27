import uuid

from lavoro_matching_api.database import queries


def get_applications_to_job_post(job_post_id: uuid.UUID):
    return queries.get_applications_to_job_post(job_post_id)


def approve_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    return queries.approve_application(job_post_id, applicant_account_id)
