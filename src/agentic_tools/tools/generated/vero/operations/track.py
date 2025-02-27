from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VeroCredentials

class VeroTrackToolInput(BaseModel):
    event_name: Optional[str] = Field(None, description="The name of the event tracked")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email")
    tags: Optional[str] = Field(None, description="Tags to add separated by \",\"")
    data_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    data_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent any properties you want to track with this event")
    extra_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent reserved, Vero-specific operators. Refer to the note on “deduplication” below.")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier of the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    extra_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent reserved, Vero-specific operators. Refer to the note on “deduplication” below.")


class VeroTrackTool(BaseTool):
    name: str = "vero_track"
    connector_id: str = "nodes-base.vero"
    description: str = "Tool for vero track operation - track operation"
    args_schema: type[BaseModel] | None = VeroTrackToolInput
    credentials: Optional[VeroCredentials] = None
