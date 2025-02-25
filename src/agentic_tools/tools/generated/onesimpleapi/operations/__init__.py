# oneSimpleApi operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all oneSimpleApi operation tools."""
    tools = []
    from .pdf import OnesimpleapiPdfTool
    tools.append(OnesimpleapiPdfTool())
    from .seo import OnesimpleapiSeoTool
    tools.append(OnesimpleapiSeoTool())
    from .screenshot import OnesimpleapiScreenshotTool
    tools.append(OnesimpleapiScreenshotTool())
    from .instagramprofile import OnesimpleapiInstagramprofileTool
    tools.append(OnesimpleapiInstagramprofileTool())
    from .spotifyartistprofile import OnesimpleapiSpotifyartistprofileTool
    tools.append(OnesimpleapiSpotifyartistprofileTool())
    from .exchangerate import OnesimpleapiExchangerateTool
    tools.append(OnesimpleapiExchangerateTool())
    from .imagemetadata import OnesimpleapiImagemetadataTool
    tools.append(OnesimpleapiImagemetadataTool())
    from .expandurl import OnesimpleapiExpandurlTool
    tools.append(OnesimpleapiExpandurlTool())
    from .qrcode import OnesimpleapiQrcodeTool
    tools.append(OnesimpleapiQrcodeTool())
    from .validateemail import OnesimpleapiValidateemailTool
    tools.append(OnesimpleapiValidateemailTool())
    return tools
