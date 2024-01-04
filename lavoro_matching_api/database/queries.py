import uuid

from lavoro_library.model.matching_api.db_models import Application, Comment, Match
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


def delete_matches(job_post_id: uuid.UUID):
    query_tuple = ("DELETE FROM matches WHERE job_post_id = %s", (job_post_id,))
    result = db.execute_one(query_tuple)
    return result["affected_rows"] > 1


def get_match(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM matches WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    if result["result"]:
        return Match(**result["result"][0])
    else:
        return None


def set_match_approved_by_applicant(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "UPDATE matches SET approved_by_applicant = TRUE WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1


def reject_match(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "UPDATE matches SET approved_by_applicant = FALSE WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1


def get_applications_by_job_post(job_post_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM applications WHERE job_post_id = %s",
        (job_post_id,),
    )
    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Application(**row) for row in result["result"]]
    else:
        return []


def get_created_applications_by_applicant(applicant_account_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM applications WHERE applicant_account_id = %s",
        (applicant_account_id,),
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


def reject_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "UPDATE applications SET approved_by_company = FALSE WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )
    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1


def create_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        """
        INSERT INTO applications (job_post_id, applicant_account_id)
        VALUES (%s, %s)
        """,
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1


def get_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM applications WHERE job_post_id = %s AND applicant_account_id = %s",
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    if result["result"]:
        return Application(**result["result"][0])
    else:
        return None


def create_comment(
    job_post_id: uuid.UUID, applicant_account_id: uuid.UUID, current_recruiter_id: uuid.UUID, comment_body: str
):
    query_tuple = (
        """
        INSERT INTO comments (account_id, job_post_id, applicant_account_id, comment_body)
        VALUES (%s, %s, %s, %s)
        """,
        (current_recruiter_id, job_post_id, applicant_account_id, comment_body),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1


def get_comments_on_application(job_post_id: uuid.UUID, applicant_account_id: uuid.UUID):
    query_tuple = (
        """
        SELECT * FROM comments
        WHERE job_post_id = %s AND applicant_account_id = %s
        ORDER BY created_on_date DESC
        """,
        (job_post_id, applicant_account_id),
    )

    result = db.execute_one(query_tuple)
    if result["result"]:
        return [Comment(**row) for row in result["result"]]
    else:
        return []


def get_comment(comment_id: uuid.UUID):
    query_tuple = (
        "SELECT * FROM comments WHERE id = %s",
        (comment_id,),
    )

    result = db.execute_one(query_tuple)
    if result["result"]:
        return Comment(**result["result"][0])
    else:
        return None


def delete_comment(comment_id: uuid.UUID):
    query_tuple = (
        "DELETE FROM comments WHERE id = %s",
        (comment_id,),
    )

    result = db.execute_one(query_tuple)
    return result["affected_rows"] == 1
