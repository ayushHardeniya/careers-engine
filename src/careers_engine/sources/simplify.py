from __future__ import annotations

from careers_engine.employment import infer_employment_type
from careers_engine.models import Job
from careers_engine.parsers import JsonParser
from careers_engine.sources.base import BaseSource


class SimplifySource(BaseSource):
    """Collect internship opportunities from Simplify."""

    BASE_URL = "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/dev/"

    LISTINGS_FILE = ".github/scripts/listings.json"

    @property
    def name(self) -> str:
        return "simplify"

    @property
    def base_url(self) -> str:
        return self.BASE_URL

    async def collect(self) -> list[Job]:
        content = await self.fetcher.fetch(f"{self.base_url}{self.LISTINGS_FILE}")

        listings = JsonParser().parse(content)

        jobs: list[Job] = []

        for listing in listings:
            if not listing.get("active", False):
                continue

            if not listing.get("is_visible", False):
                continue

            company = listing.get("company_name")
            role = listing.get("title")
            apply_url = listing.get("url")

            if not company or not role or not apply_url:
                continue

            locations = listing.get("locations", [])

            for location in locations:
                jobs.append(
                    Job(
                        company=company,
                        role=role,
                        location=location,
                        apply_url=apply_url,
                        employment_type=infer_employment_type(role),
                    )
                )

        return jobs
