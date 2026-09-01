from __future__ import annotations

import re

from careers_engine.filters.base import JobFilter
from careers_engine.models import Job


class EligibilityFilter(JobFilter):
    """Keep opportunities currently relevant to applicants in India."""

    INDIA_PATTERN = re.compile(r"\bindia\b", re.IGNORECASE)

    def match(self, job: Job) -> bool:
        return bool(self.INDIA_PATTERN.search(job.location))
