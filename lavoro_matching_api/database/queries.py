import uuid

from lavoro_library.model.matching_api.db_models import Match
from lavoro_matching_api.database import db


def get_matches_by_applicant(applicant_account_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM matches WHERE applicant_account_id = %s",
        (applicant_account_id,),
    )

    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Match(**row) for row in result["result"]]
    else:
        return []


def get_matches_by_job_post(job_post_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM matches WHERE job_post_id = %s",
        (job_post_id,),
    )
    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Match(**row) for row in result["result"]]
    else:
        return []
