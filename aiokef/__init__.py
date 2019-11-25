"""A module for asynchronously interacting with KEF wireless speakers."""

__version__ = "0.1.8"

from aiokef.aiokef import AsyncKefSpeaker, SyncKefSpeaker

__all__ = ["AsyncKefSpeaker", "SyncKefSpeaker"]
