from careers_engine.filters import EligibilityFilter, JobFilter
from careers_engine.models import Job


class DummyFilter(JobFilter):
    def match(self, job: Job) -> bool:
        return True


def test_filter_match() -> None:
    job = Job(
        company="Google",
        role="Software Engineer Intern",
        location="India",
        apply_url="https://google.com",
    )

    assert DummyFilter().match(job)


# EligibilityFilter() tests


def test_eligibility_filter_accepts_india() -> None:
    job = Job(
        company="Google",
        role="SWE Intern",
        location="Bengaluru, India",
        apply_url="https://google.com",
    )

    assert EligibilityFilter().match(job)


def test_eligibility_filter_rejects_remote_in_usa() -> None:
    job = Job(
        company="Example",
        role="Software Engineer Intern",
        location="Remote in USA",
        apply_url="https://example.com",
    )

    assert not EligibilityFilter().match(job)


def test_eligibility_filter_rejects_remote_in_canada() -> None:
    job = Job(
        company="Example",
        role="Software Engineer Intern",
        location="Remote in Canada",
        apply_url="https://example.com",
    )

    assert not EligibilityFilter().match(job)


def test_eligibility_filter_rejects_indianapolis() -> None:
    job = Job(
        company="Example",
        role="Software Engineer Intern",
        location="Indianapolis, IN",
        apply_url="https://example.com",
    )

    assert not EligibilityFilter().match(job)


def test_eligibility_filter_rejects_indiana() -> None:
    job = Job(
        company="Example",
        role="Software Engineer Intern",
        location="Indiana",
        apply_url="https://example.com",
    )

    assert not EligibilityFilter().match(job)


def test_eligibility_filter_rejects_unspecified_remote() -> None:
    job = Job(
        company="GitLab",
        role="Backend Engineer",
        location="Remote",
        apply_url="https://gitlab.com",
    )

    assert not EligibilityFilter().match(job)


def test_eligibility_filter_rejects_foreign() -> None:
    job = Job(
        company="Google",
        role="SWE Intern",
        location="Sydney, Australia",
        apply_url="https://google.com",
    )

    assert not EligibilityFilter().match(job)
