# common RetrieveUpdateDestroyAPIViewWrapper for models
from rest_framework import response, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class RetrieveUpdateDestroyAPIViewWrapper(RetrieveUpdateDestroyAPIView):
    """
    prevent updating using PUT, redefine delete()
    """

    def put(self, request, **kwargs):
        """
        update object
        """
        return response.Response(
            {"message": "To update %s, use PATCH method" % self.name},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def delete(self, request, **kwargs):
        """
        delete object
        """
        obj = self.get_object()
        obj.delete()
        return response.Response({}, status=status.HTTP_200_OK)
