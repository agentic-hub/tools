from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JenkinsQuietdownToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    reason: Optional[str] = Field(None, description="Freeform reason for quiet down mode")
    instanceNotice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsQuietdownTool(BaseTool):
    name = "jenkins_quietdown"
    description = "Tool for jenkins quietDown operation - quietDown operation"
    
    def _run(self, **kwargs):
        """Run the jenkins quietDown operation."""
        # Implement the tool logic here
        return f"Running jenkins quietDown operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jenkins quietDown operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
