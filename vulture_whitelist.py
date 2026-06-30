"""Whitelist for vulture false positives.

Add names here when frameworks call them dynamically, for example:
- FastAPI route handlers
- pytest fixtures
- Click commands
- Celery tasks

Example:
    some_route_handler
    db_session
"""
