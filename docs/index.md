# careers-engine

**careers-engine** is an open source job aggregation and publishing platform powering **ZenYukti Jobs**.

It continuously discovers software engineering opportunities from multiple upstream sources, transforms them into a consistent data model, enriches them with additional metadata, stores them in a version-controlled repository, and publishes newly discovered opportunities to Discord through an automated delivery pipeline.

The project is built with modern Python tooling, including [uv](https://docs.astral.sh/uv/) for dependency management, [GitHub Actions](https://docs.github.com/actions) for workflow automation, and [Discord.py](https://discordpy.readthedocs.io/) for publishing opportunities to Discord.

---

## Overview

Instead of manually tracking career pages across dozens of companies, careers-engine automates the complete lifecycle of discovering, processing, and publishing software engineering opportunities.

The platform currently focuses on opportunities from leading technology companies, including FAANG, enterprise software vendors, AI companies, cloud providers, and high-growth startups such as Google, Microsoft, Amazon, Apple, Meta, NVIDIA, OpenAI, Stripe, Databricks, Cloudflare, Flipkart, Razorpay, Zoho, and many others.

Every opportunity passes through a common processing pipeline before it reaches the community, ensuring consistent formatting, branding, metadata enrichment, and duplicate detection.

---

## Core capabilities

The project currently provides:

- Automated collection from upstream job sources.
- Manual opportunity queue for curated postings.
- Company branding with logo support.
- Employment type inference.
- Duplicate detection.
- Version-controlled job storage.
- Automated Discord publishing.
- GitHub Actions based automation.

---

## High-level architecture

At a high level, careers-engine consists of two independent ingestion paths.

- **Automatic ingestion**, which periodically collects opportunities from upstream sources.
- **Manual queue**, which allows maintainers to publish curated opportunities.

Both paths eventually converge into a common publishing pipeline before opportunities are delivered to the ZenYukti Jobs community.

A complete architecture diagram is available in the Architecture section.

---

## Technology stack

careers-engine intentionally keeps its technology stack small and maintainable.

| Component | Technology |
|-----------|------------|
| Language | Python |
| Dependency management | [uv](https://docs.astral.sh/uv/) |
| Workflow automation | [GitHub Actions](https://docs.github.com/actions) |
| Discord integration | [Discord.py](https://discordpy.readthedocs.io/) |
| Documentation | [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) |
| Repository hosting | GitHub |

---

## Project structure

This documentation is organized into the following sections.

### Getting Started

Install, configure, and run careers-engine locally.

### Architecture

Understand the internal design of the ingestion, storage, and publishing pipelines.

### Developer Guide

Learn how to add new sources, extend branding, implement employment inference, and contribute new functionality.

### Reference

Reference documentation for configuration, workflows, environment variables, CLI utilities, and project internals.

---

## Source code

The source code is available on GitHub:

<https://github.com/ZenYukti/careers-engine>

Bug reports, feature requests, and pull requests are welcome.