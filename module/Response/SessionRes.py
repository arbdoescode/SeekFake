class SessionResponse:
    def __init__(self, success: bool, data=None, message=None):
        self.success = success
        self.data = data
        self.message = message

    def to_json(self):
        if self.success:
            return {
                "success": True,
                "response": self.data  # full session dict
            }
        else:
            return {
                "success": False,
                "response": self.message
            }
