
class MessageMixin:
    message = None

    def get_message(self)->str:
        if not self.message:
            raise ValueError("Message é um atributo obrigatorio")
        
        return self.message
    

class SuccessFullCreateMessageMixin(MessageMixin):
    message = 'Created sucefully'
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        message = self.get_message()
        response['message'] = message
        return response
    
class SuccessFullUpdatedMessageMixin(MessageMixin):
    
    message = 'Updated sucefully'
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response['message'] = self.get_message()
        return response
    
