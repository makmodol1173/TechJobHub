CREATE TABLE recruiter (
    recruiter_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    address TEXT,
    profile_picture VARCHAR(255)
);

CREATE TABLE company (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    recruiter_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    description TEXT,
    trade_license_number VARCHAR(50) UNIQUE NOT NULL,
    website_url VARCHAR(255),
    FOREIGN KEY (recruiter_id) REFERENCES recruiter(recruiter_id)
);

CREATE TABLE job_seeker (
    job_seeker_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    address TEXT,
    profile_picture VARCHAR(255),
    education TEXT,
    resume VARCHAR(255)
);


CREATE TABLE skill (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    job_seeker_id INT NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (job_seeker_id) REFERENCES job_seeker(job_seeker_id)
);

CREATE TABLE bookmark (
    bookmark_id INT AUTO_INCREMENT PRIMARY KEY,
    job_seeker_id INT NOT NULL,
    job_post_id INT NOT NULL,
    FOREIGN KEY (job_seeker_id) REFERENCES job_seeker(job_seeker_id),
    FOREIGN KEY (job_post_id) REFERENCES job_post(job_post_id)
);

CREATE TABLE application (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    job_seeker_id INT NOT NULL,
    job_post_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_seeker_id) REFERENCES job_seeker(job_seeker_id),
    FOREIGN KEY (job_post_id) REFERENCES job_post(job_post_id)
);

CREATE TABLE job_post (
    job_post_id INT AUTO_INCREMENT PRIMARY KEY,
    recruiter_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    key_responsibilities TEXT,
    location VARCHAR(255),
    educational_requirement TEXT,
    deadline DATE NOT NULL,
    year_of_experience INT,
    type VARCHAR(50),
    keywords TEXT,
    FOREIGN KEY (recruiter_id) REFERENCES recruiter(recruiter_id)
);

CREATE TABLE questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL,
    question_1 TEXT,
    question_2 TEXT,
    question_3 TEXT,
    question_4 TEXT,
    question_5 TEXT,
    question_6 TEXT,
    question_7 TEXT,
    question_8 TEXT,
    question_9 TEXT,
    question_10 TEXT,
    FOREIGN KEY (application_id) REFERENCES application(application_id)
);

CREATE TABLE answers (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    answer_1 TEXT,
    answer_2 TEXT,
    answer_3 TEXT,
    answer_4 TEXT,
    answer_5 TEXT,
    answer_6 TEXT,
    answer_7 TEXT,
    answer_8 TEXT,
    answer_9 TEXT,
    answer_10 TEXT,
    FOREIGN KEY (question_id) REFERENCES application_questions(question_id)
);

CREATE TABLE assessment (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    answer_id INT NOT NULL,
    mark_1 INT,
    mark_2 INT,
    mark_3 INT,
    mark_4 INT,
    mark_5 INT,
    mark_6 INT,
    mark_7 INT,
    mark_8 INT,
    mark_9 INT,
    mark_10 INT,
    FOREIGN KEY (answer_id) REFERENCES application_answers(answer_id)
);
