CREATE EXTENSION "uuid-ossp";

CREATE TYPE application_status AS ENUM ('created', 'rejected', 'approved');

CREATE TABLE IF NOT EXISTS matches (
    id uuid PRIMARY KEY,
    match_probability REAL NOT NULL,
    job_post_id uuid NOT NULL REFERENCES job_posts(id) ON DELETE CASCADE,
    applicant_profile_id uuid NOT NULL REFERENCES applicant_profiles(id) ON DELETE CASCADE,
    approved_by_applicant BOOLEAN
);

CREATE TABLE IF NOT EXISTS applications (
    id uuid PRIMARY KEY,
    match_id uuid NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
    application_status application_status NOT NULL,
    created_on_date TIMESTAMP NOT NULL,
    approved_by_company BOOLEAN,
    PRIMARY KEY (id, match_id)
);

CREATE TABLE IF NOT EXISTS comments (
    recruiter_profile_id uuid NOT NULL REFERENCES recruiter_profiles(id) ON DELETE CASCADE,
    application_id uuid NOT NULL REFERENCES applications(id) ON DELETE CASCADE,
    comment_body TEXT NOT NULL,
    PRIMARY KEY (recruiter_profile_id, application_id)
);
