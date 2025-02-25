from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ApitemplateioCreateToolInput(BaseModel):
    imageTemplateId: Optional[str] = Field(None, description="ID of the image template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    download: Optional[bool] = Field(None, description="Name of the binary property to which to write the data of the read file")
    resource: Optional[str] = Field(None, description="Resource")
    propertiesJson: Optional[str] = Field(None, description="Properties (JSON)")
    propertiesUi: Optional[Dict[str, Any]] = Field(None, description="Properties")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    pdfTemplateId: Optional[str] = Field(None, description="ID of the PDF template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    binaryProperty: Optional[str] = Field(None, description="Put Output File in Field")
    overridesJson: Optional[str] = Field(None, description="Overrides (JSON)")
    operation: Optional[str] = Field(None, description="Operation")
    overridesUi: Optional[Dict[str, Any]] = Field(None, description="Overrides")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")


class ApitemplateioCreateTool(BaseTool):
    name = "apitemplateio_create"
    description = "Tool for apiTemplateIo create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the apiTemplateIo create operation."""
        # Implement the tool logic here
        return f"Running apiTemplateIo create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the apiTemplateIo create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
