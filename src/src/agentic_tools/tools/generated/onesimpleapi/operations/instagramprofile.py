from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnesimpleapiInstagramprofileToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    profileName: Optional[str] = Field(None, description="Profile name to get details of")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiInstagramprofileTool(BaseTool):
    name = "onesimpleapi_instagramprofile"
    description = "Tool for oneSimpleApi instagramProfile operation - instagramProfile operation"
    
    def _run(self, **kwargs):
        """Run the oneSimpleApi instagramProfile operation."""
        # Implement the tool logic here
        return f"Running oneSimpleApi instagramProfile operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the oneSimpleApi instagramProfile operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
