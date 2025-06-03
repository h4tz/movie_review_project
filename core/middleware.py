



class RequestLoggerMiddleware :
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        
        print(f"--- Request Logged ---")
        print(f"Method: {request.method}")
        print(f"Path: {request.path}")
        print(f"----------------------")
        
        
        response = self.get_response(request)
        return response