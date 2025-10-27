from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class CustomUserRateThrottle(UserRateThrottle):
    scope = 'custom_user'

class CustomAnonRateThrottle(AnonRateThrottle):
    scope = 'custom_anon'
