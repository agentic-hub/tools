from .base import *
from .generated import *

# Tools package
# Import all toolkit classes from generated
# Usage examples:
# 1. With default credentials:
#    from agentic_tools.tools import S3Toolkit
#    tools = S3Toolkit().get_tools()
#
# 2. With custom credentials:
#    from agentic_tools.tools import S3Toolkit
#    credentials = {
#        'aws_access_key_id': 'your-access-key',
#        'aws_secret_access_key': 'your-secret-key',
#        'region_name': 'us-west-2'
#    }
#    tools = S3Toolkit(credentials=credentials).get_tools()
