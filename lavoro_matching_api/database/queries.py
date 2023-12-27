import uuid

from lavoro_library.model.matching_api.db_models import Application, Match
from lavoro_matching_api.database import db


def get_matches_by_applicant(applicant_account_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM matches WHERE applicant_account_id = %s AND approved_by_applicant IS NULL",
        (applicant_account_id,),
    )

    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Match(**row) for row in result["result"]]
    else:
        return []


def get_matches_by_job_post(job_post_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM matches WHERE job_post_id = %s AND approved_by_applicant IS NULL",
        (job_post_id,),
    )
    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Match(**row) for row in result["result"]]
    else:
        return []


def reject_match(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "UPDATE matches SET approved_by_applicant = FALSE WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1


def get_applications_to_job_post(job_post_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM applications WHERE job_post_id = %s",
        (job_post_id,),
    )
    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Application(**row) for row in result["result"]]
    else:
        return []


def approve_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "UPDATE applications SET approved_by_company = TRUE WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1
