from pydantic import BaseModel as PydanticBaseModel, Field as PydanticField
from typing import Any, Dict, Optional

# Re-export BaseModel and Field from pydantic
BaseModel = PydanticBaseModel
Field = PydanticField


class BaseTool:
    """Base class for all tools."""

    name: str
    description: str

    def __init__(self, name: str = None, description: str = None):
        """Initialize the tool with a name and description."""
        if name:
            self.name = name
        if description:
            self.description = description

    def _run(self, **kwargs: Dict[str, Any]) -> Any:
        """Run the tool."""
        raise NotImplementedError("Subclasses must implement this method.")

    async def _arun(self, **kwargs: Dict[str, Any]) -> Any:
        """Run the tool asynchronously."""
        return self._run(**kwargs)
