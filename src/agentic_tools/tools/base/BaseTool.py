import asyncio
from pydantic import BaseModel as PydanticBaseModel, Field as PydanticField
from typing import Any, Dict, Optional
from langchain.tools import BaseTool as LangchainBaseTool
from agentic_tools.service.scade import scade_service

# Re-export BaseModel and Field from pydantic
BaseModel = PydanticBaseModel
Field = PydanticField


class BaseTool(LangchainBaseTool):
    """Base class for all tools."""

    def _run(self, **kwargs: Dict[str, Any]) -> Any:
        """Run the tool."""
        result = scade_service.execute_connector(
            connector_id=self.connector_id,
            credentials=self.credentials,
            data=kwargs,
        )
        return result

    async def _arun(self, **kwargs: Dict[str, Any]) -> Any:
        """Run the tool asynchronously."""

        result = await scade_service.execute_connector(
            connector_id=self.connector_id,
            credentials=self.credentials,
            data=kwargs,
        )
        return result
