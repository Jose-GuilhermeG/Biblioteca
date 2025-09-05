
class SuccessFullCreateMessageMixin:
    message = None
    
    def get_message(self)->str:
        if not self.message:
            raise ValueError("Message é um atributo obrigatorio")
        
        return self.message
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        message = self.get_message()
        response['message'] = message
        return response