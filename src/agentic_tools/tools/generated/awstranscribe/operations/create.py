from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwstranscribeCreateToolInput(BaseModel):
    languageCode: Optional[str] = Field(None, description="Language used in the input media file")
    resource: Optional[str] = Field(None, description="Resource")
    mediaFileUri: Optional[str] = Field(None, description="The S3 object location of the input media file")
    transcriptionJobName: Optional[str] = Field(None, description="The name of the job")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    detectLanguage: Optional[bool] = Field(None, description="Whether to set this field to true to enable automatic language identification")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeCreateTool(BaseTool):
    name = "awstranscribe_create"
    description = "Tool for awsTranscribe create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the awsTranscribe create operation."""
        # Implement the tool logic here
        return f"Running awsTranscribe create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsTranscribe create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
