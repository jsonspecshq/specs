"""The published documents this package carries, by their path under `schemas/`.

The bytes are the published ones. A consumer fetching a document's `$id` receives these,
so the verdict this package reaches is the verdict the published schema states. A tree that
reuses another specification's list carries that specification's document too, because a
validator loads it beside the tree's (type rules § 6).
"""

from __future__ import annotations

__all__ = ["FILES"]

#: Each document's path under `schemas/`, which is the path of its own `$id`.
FILES: tuple[str, ...] = (
    'adcom/schemas/kernel/1/kernel.json',
    'adcom/schemas/modules/lists/1/lists.json',
    'adcom/schemas/modules/objects/1/objects.json',
)
