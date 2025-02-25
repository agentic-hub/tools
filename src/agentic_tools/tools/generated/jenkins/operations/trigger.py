from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JenkinsTriggerToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instanceNotice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsTriggerTool(BaseTool):
    name = "jenkins_trigger"
    description = "Tool for jenkins trigger operation - trigger operation"
    
    def _run(self, **kwargs):
        """Run the jenkins trigger operation."""
        # Implement the tool logic here
        return f"Running jenkins trigger operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jenkins trigger operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
