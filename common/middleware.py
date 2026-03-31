class UserAgentLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', 'REMOTE_ADDR' 'Unknown')

        print(f"User: {user_agent}")

        response = self.get_response(request)

        return response
