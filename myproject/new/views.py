from datetime import datetime
from django.http import HttpResponse
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






from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def password_checker_view(request):
    if request.method == 'GET':
        html_content = """
        <form method="POST">
            <label for="password">Enter Password:</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Check Password</button>
        </form>
        """

        return HttpResponse(html_content)
    

    elif request.method == 'POST':
    
        password = request.POST.get('password', '')


        if not password:
            return HttpResponse("Password is required.", status=400)
        
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)        


        if has_uppercase and has_lowercase and has_digit:
            return HttpResponse("Password is strong.")
        else:
            return HttpResponse("Password is weak. It must contain at least one uppercase letter, one lowercase letter, and one digit.", status=400)
         