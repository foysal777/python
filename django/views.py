from django.http import HttpResponse
from datetime import datetime


def voter_status(request, birth_year):
    try:
        birth_year = int(birth_year)
        current_year = datetime.now().year
        age = current_year - birth_year

        if age < 0 or age > 120:
            return HttpResponse("Invalid birth year provided.", status=400
                                    )
        if age >= 18:
            return HttpResponse(f"You are {age} years old. You are eligible to vote.")
        else:
            return HttpResponse(f"You are {age} years old. You are not eligible to vote.")
        

    except ValueError:
        return HttpResponse("Invalid birth year provided.", status=400)     
    

