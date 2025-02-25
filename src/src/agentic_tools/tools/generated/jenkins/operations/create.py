from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JenkinsCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instanceNotice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    xml: Optional[str] = Field(None, description="XML of Jenkins config")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    newJob: Optional[str] = Field(None, description="Name of the new Jenkins job")
    createNotice: Optional[str] = Field(None, description="To get the XML of an existing job, add ‘config.xml’ to the end of the job URL")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsCreateTool(BaseTool):
    name = "jenkins_create"
    description = "Tool for jenkins create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the jenkins create operation."""
        # Implement the tool logic here
        return f"Running jenkins create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jenkins create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
