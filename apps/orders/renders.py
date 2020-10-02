from typing import Any, Dict, List, Optional, Union

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList

message_map = lambda view: lambda status_code: {  # noqa
    "POST": "%s created successfully" % view.name.capitalize(),
    "PUT": "%s updated succesfully" % view.name.capitalize(),
    "DELETE": "%s deleted successfully" % view.name.capitalize(),
}.get(status_code)


class DefaultRenderer(JSONRenderer):
    """
    Custom renderer class for application views
    """

    def render(
        self,
        data: Union[Dict[str, Union[str, List[ErrorDetail]]], ReturnList],
        accepted_media_type: Optional[str] = None,
        renderer_context: Optional[Dict[str, Any]] = None,
    ) -> bytes:
        """
        Format response data for application views
        """
        if renderer_context["response"].status_code == 422:
            renderer_context["response"].status_code = status.HTTP_400_BAD_REQUEST
        status_code = renderer_context["response"].status_code
        if renderer_context["request"].method == "GET":
            if renderer_context["kwargs"] == {}:
                message = (
                    "All %s" % renderer_context["view"].pluralized_name.capitalize()
                )
            else:
                message = "%s info" % renderer_context["view"].name.capitalize()
        else:
            message = message_map(renderer_context["view"])(
                renderer_context["request"].method
            )
        if data is None:
            data = {}
        res_data = (
            ({"status": "success", "message": message, "data": data})
            if status.is_success(status_code)
            else {
                "status": "error",
                "message": "Correct the errors below",
                "data": data,
            }
        )
        return super(DefaultRenderer, self).render(
            res_data, accepted_media_type, renderer_context
        )
