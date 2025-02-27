# editImage operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all editImage operation tools."""
    tools = []
    from .blur import EditimageBlurTool
    tools.append(EditimageBlurTool())
    from .border import EditimageBorderTool
    tools.append(EditimageBorderTool())
    from .composite import EditimageCompositeTool
    tools.append(EditimageCompositeTool())
    from .create import EditimageCreateTool
    tools.append(EditimageCreateTool())
    from .crop import EditimageCropTool
    tools.append(EditimageCropTool())
    from .draw import EditimageDrawTool
    tools.append(EditimageDrawTool())
    from .information import EditimageInformationTool
    tools.append(EditimageInformationTool())
    from .multistep import EditimageMultistepTool
    tools.append(EditimageMultistepTool())
    from .resize import EditimageResizeTool
    tools.append(EditimageResizeTool())
    from .rotate import EditimageRotateTool
    tools.append(EditimageRotateTool())
    from .shear import EditimageShearTool
    tools.append(EditimageShearTool())
    from .text import EditimageTextTool
    tools.append(EditimageTextTool())
    from .transparent import EditimageTransparentTool
    tools.append(EditimageTransparentTool())
    return tools
