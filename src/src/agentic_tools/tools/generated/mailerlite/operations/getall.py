from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailerliteGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    subscriberId: Optional[str] = Field(None, description="Email of subscriber")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteGetallTool(BaseTool):
    name = "mailerlite_getall"
    description = "Tool for mailerLite getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the mailerLite getAll operation."""
        # Implement the tool logic here
        return f"Running mailerLite getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailerLite getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
