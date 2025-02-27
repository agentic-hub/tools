from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FacebookgraphapiCredentials

class FacebookgraphapiDefaultToolInput(BaseModel):
    send_binary_data: Optional[bool] = Field(None, description="Whether binary data should be sent as body")
    graph_api_version: Optional[str] = Field(None, description="The version of the Graph API to be used in the request")
    binary_property_name: Optional[str] = Field(None, description="For Form-Data Multipart, they can be provided in the format: <code>\"sendKey1:binaryProperty1,sendKey2:binaryProperty2</code>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    http_request_method: Optional[str] = Field(None, description="The HTTP Method to be used for the request")
    edge: Optional[str] = Field(None, description="Edge of the node on which to operate. Edges represent collections of objects which are attached to the node.")
    node: Optional[str] = Field(None, description="The node on which to operate. A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook.")
    host_url: Optional[str] = Field(None, description="The Host URL of the request. Almost all requests are passed to the graph.facebook.com host URL. The single exception is video uploads, which use graph-video.facebook.com.")
    allow_unauthorized_certs: Optional[bool] = Field(None, description="Whether to connect even if SSL certificate validation is not possible")


class FacebookgraphapiDefaultTool(BaseTool):
    name: str = "facebookgraphapi_default"
    description: str = "Tool for facebookGraphApi default operation - default operation"
    args_schema: type[BaseModel] | None = FacebookgraphapiDefaultToolInput
    credentials: Optional[FacebookgraphapiCredentials] = None
