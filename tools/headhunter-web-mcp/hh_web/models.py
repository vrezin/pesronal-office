from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class ApplicationStatus(str, Enum):
    NOT_APPLIED = "not_applied"
    APPLIED = "applied"
    VIEWED = "viewed"
    NOT_VIEWED = "not_viewed"
    REJECTED = "rejected"
    INVITATION = "invitation"
    INTERVIEW = "interview"
    UNKNOWN = "unknown"


class VacancyCard(BaseModel):
    vacancy_id: str
    url: str
    title: str
    company: str = ""
    salary: str = ""
    location: str = ""
    work_format: str = ""
    schedule: str = ""
    experience: str = ""
    published_at: str = ""
    application_status: ApplicationStatus = ApplicationStatus.UNKNOWN


class ResumeCard(BaseModel):
    resume_id: str
    title: str
    url: str
    employment: str = ""
    salary: str = ""
    work_format: str = ""
    views: str = ""
    new_views: str = ""
    invitations: str = ""
    lift_status: str = ""
    suitable_vacancies_url: str = ""


class ResumeDetails(ResumeCard):
    search_status: str = ""
    contacts: list[str] = Field(default_factory=list)
    experience_total: str = ""
    skills: list[str] = Field(default_factory=list)
    about: str = ""
    completion_text: str = ""
    lift_details: str = ""
    auto_raise: str = ""
    visibility: str = ""
    suitable_vacancies_count: int | None = None
    language: str = ""
    raw_summary: str = ""


class VacancyFull(BaseModel):
    source: str = "hh-web"
    vacancy_id: str
    url: str
    role_title: str
    company: str = ""
    location_format: str = ""
    salary: str = ""
    experience: str = ""
    schedule: str = ""
    work_format: str = ""
    published_at: str = ""
    raw_jd_markdown: str = ""
    screening_questions: list[str] = Field(default_factory=list)
    application_status: ApplicationStatus = ApplicationStatus.UNKNOWN
    extraction_warnings: list[str] = Field(default_factory=list)
    extraction_confidence: float = 1.0


class SearchResult(BaseModel):
    vacancies: list[VacancyCard] = Field(default_factory=list)
    total_visible: int | None = None
    search_url: str = ""
    warnings: list[str] = Field(default_factory=list)
    resume_id: str = ""
    resume_title: str = ""


class ApplicationEntry(BaseModel):
    status: ApplicationStatus
    title: str
    company: str = ""
    vacancy_id: str = ""
    url: str = ""
    date: str = ""
    last_message_snippet: str = ""
    next_action: str = ""


class DigestResult(BaseModel):
    url: str
    success: bool
    vacancy: VacancyFull | None = None
    error: str | None = None
    status: str = "ok"
    vacancy_id: str = ""
    title: str = ""
    company: str = ""
    salary: str = ""
    duplicate: bool = False
    duplicate_matches: list[str] = Field(default_factory=list)


class DigestVacancyLink(BaseModel):
    vacancy_id: str
    url: str
    title: str = ""
    company: str = ""
    salary_hint: str = ""
    duplicate: bool = False
    duplicate_matches: list[str] = Field(default_factory=list)


class EmailClassification(BaseModel):
    email_type: str
    confidence: float
    reasons: list[str] = Field(default_factory=list)
    chat_id: str = ""
    vacancy_id: str = ""
    vacancy_title: str = ""
    company: str = ""


class DigestEmailReport(BaseModel):
    email_type: str
    total_links: int
    unique_links: int
    duplicate_links_in_email: int
    links: list[DigestVacancyLink] = Field(default_factory=list)
    extracted_results: list[DigestResult] = Field(default_factory=list)
    existing_matches: list[DigestVacancyLink] = Field(default_factory=list)
    new_successes: list[DigestResult] = Field(default_factory=list)
    inaccessible: list[DigestResult] = Field(default_factory=list)
    failed: list[DigestResult] = Field(default_factory=list)
    recommended_next_tasks: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class ChatDetails(BaseModel):
    chat_id: str
    status: str = "unknown"
    company: str = ""
    vacancy_title: str = ""
    vacancy_id: str = ""
    vacancy_url: str = ""
    latest_message_text: str = ""
    inferred_status: ApplicationStatus = ApplicationStatus.UNKNOWN
    warnings: list[str] = Field(default_factory=list)


class ToolError(BaseModel):
    code: str
    message: str
    details: dict[str, Any] = Field(default_factory=dict)
