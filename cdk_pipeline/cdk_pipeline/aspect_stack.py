from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam
    )
import aws_cdk as cdk
import jsii

@jsii.implements(cdk.IAspect)
class CfnRoleChecker:
    def visit(self, node):
        # See that its a CfnRole
        if isinstance(node, iam.CfnRole):
            # modifying all role names to be prefixed
            node.add_property_override("RoleName", "DoThisThing"+node.logical_id)