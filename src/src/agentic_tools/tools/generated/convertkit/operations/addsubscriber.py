from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConvertkitAddsubscriberToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitAddsubscriberTool(BaseTool):
    name = "convertkit_addsubscriber"
    description = "Tool for convertKit addSubscriber operation - addSubscriber operation"
    
    def _run(self, **kwargs):
        """Run the convertKit addSubscriber operation."""
        # Implement the tool logic here
        return f"Running convertKit addSubscriber operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the convertKit addSubscriber operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
