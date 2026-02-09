# US Finance Daily Bot

This repository contains a small, deterministic pipeline that monitors selected US finance news sources, filters for relevant signals, and sends a daily email summary.

It is designed to reduce noise, not to be comprehensive.

---

## What this does

- Pulls daily news from selected RSS feeds
- Filters items using explicit keyword rules
- Identifies potential US finance–related signals
- Sends a plain-text daily email with highlights
- Runs fully on GitHub Actions, no local machine required

The system is intentionally simple and transparent.

---

## What this does not do

- It does not scrape paywalled content
- It does not predict markets
- It does not generate opinions
- It does not guarantee daily emails with content
- It does not run continuously or in real time

Silence means no signal matched the filter that day.

---

## Architecture

```
RSS sources
   ↓
Keyword filtering
   ↓
Daily summary
   ↓
Email delivery
```

---

## Data sources

Configured in `sources.py`. Example sources include:

- Axios AM
- Reuters Finance
- Crunchbase News

Sources can be added or removed without changing the rest of the system.

---

## Filtering logic

Filtering is based on explicit keyword matching defined in `filter.py`.

If no items match, no summary is sent unless explicitly configured.

---

## Email delivery

- Uses Gmail SMTP
- Requires Google App Password
- Normal Gmail passwords will not work if 2FA is enabled

Secrets are injected via GitHub Actions.

---

## Running schedule

- Runs once per day via GitHub Actions cron
- Can also be triggered manually using `workflow_dispatch`

The system does not depend on a local computer.

---

## Configuration

Secrets required:

- `MAIL_USER`  
  Full Gmail address

- `MAIL_PASS`  
  Google App Password (16 characters)

Dependencies are listed in `requirements.txt`.

---

## License

Personal use.  
No warranty.  
No guarantees.
