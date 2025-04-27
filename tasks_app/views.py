from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

#Import dummy tasks
from .tasks import dummy_background_task


# Create your views here.
'''class TriggerTask(APIView):
    def post(self, request):
        # SImulate a Task
        dummy_background_task.delay()
        # In a real-world scenario, you would call your task here
        return Response({"message": "Task triggered successfully!"})'''
    
@api_view(['POST'])
def trigger_background_task(request):
    name= request.data.get('name')
    email= request.data.get('email')

    if not name or not email:
        return Response({'error': 'Name and email are requires!', 'status': 400})
    dummy_background_task.delay(name, email)
    return Response({'message': f'Task for {name} triggered successfully!', 'status': 200})