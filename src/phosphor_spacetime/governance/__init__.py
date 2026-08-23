"""Governance primitives for PHOSPHOR Spacetime."""

from .authority import AuthorityGrant, IdempotencyStore

__all__ = ["AuthorityGrant", "IdempotencyStore"]
