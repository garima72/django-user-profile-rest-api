
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .serializers import UserProfileSerializer
from .filters import UserProfileFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # Removed IsOwner so any authenticated user can create/list all profiles

    filterset_class = UserProfileFilter
    search_fields = ["full_name", "email"]  # Fixed to match actual model fields
    ordering_fields = ["id"]

    def get_queryset(self):
        # Return all profiles (multi-user support) instead of only current user's
        return UserProfile.objects.all().order_by("-id")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)