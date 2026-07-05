from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


birth_year_param = openapi.Parameter(
    'birth_year', openapi.IN_PATH, description='Birth year', type=openapi.TYPE_INTEGER
)


@swagger_auto_schema(
    method='get',
    manual_parameters=[birth_year_param],
    responses={
        200: openapi.Response(description='Success'),
        400: openapi.Response(description='Bad Request'),
    },
)
@api_view(['GET'])
def voter_status(request, birth_year):
    print("Request received:", dir(request))
    print("Method:" , request.method)
    print("url path:", request.path)
    print("birth_year:", birth_year)
    try:
        birth_year = int(birth_year)
    except (TypeError, ValueError):
        return Response({'error': 'Invalid birth year provided.'}, status=400)

    current_year = datetime.now().year
    age = current_year - birth_year

    if age < 0 or age > 120:
        return Response({'error': 'Invalid birth year provided.'}, status=400)

    if age >= 18:
        return Response({'message': f'You are {age} years old. You are eligible to vote.'})
    return Response({'message': f'You are {age} years old. You are not eligible to vote.'})


