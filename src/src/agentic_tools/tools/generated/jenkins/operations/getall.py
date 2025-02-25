from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JenkinsGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instanceNotice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsGetallTool(BaseTool):
    name = "jenkins_getall"
    description = "Tool for jenkins getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the jenkins getAll operation."""
        # Implement the tool logic here
        return f"Running jenkins getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jenkins getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
