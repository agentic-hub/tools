from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class JenkinsTriggerparamsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instanceNotice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    param: Optional[Dict[str, Any]] = Field(None, description="Parameters for Jenkins job")
    triggerParamsNotice: Optional[str] = Field(None, description="Make sure the job is setup to support triggering with parameters. <a href=\"https://wiki.jenkins.io/display/JENKINS/Parameterized+Build\" target=\"_blank\">More info</a>")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsTriggerparamsTool(BaseTool):
    name = "jenkins_triggerparams"
    description = "Tool for jenkins triggerParams operation - triggerParams operation"
    
    def _run(self, **kwargs):
        """Run the jenkins triggerParams operation."""
        # Implement the tool logic here
        return f"Running jenkins triggerParams operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the jenkins triggerParams operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
