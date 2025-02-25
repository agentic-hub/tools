from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwstranscribeGetToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    transcriptionJobName: Optional[str] = Field(None, description="The name of the job")
    returnTranscript: Optional[bool] = Field(None, description="By default, the response only contains metadata about the transcript. Enable this option to retrieve the transcript instead.")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeGetTool(BaseTool):
    name = "awstranscribe_get"
    description = "Tool for awsTranscribe get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the awsTranscribe get operation."""
        # Implement the tool logic here
        return f"Running awsTranscribe get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsTranscribe get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
