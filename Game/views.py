from django.shortcuts import render
import random

# Create your views here.

def guess(request):
    if "number" not in request.session: 
         request.session["number"] = random.randint(1,10)
         request.session["attempts"] = 0

    result = ""
    game_over = False

    if request.method == "POST":

        try: 
            guess = int(request.POST.get("guess", 0))
            number = request.session["number"]
            attempts = request.session.get("attempts", 0) + 1
            request.session["attempts"] = attempts


            if guess == number:
                result = "Correct Guess! Play again."
                game_over = True
                
            elif attempts >= 5:
                result = f"Out of Attempts!, The Number Was {number}"
                game_over = True

            else:
                result = f"Incorrect Guess, Try Again. ({5 - attempts} Attempts Left)."

            if game_over:
                del request.session["number"]
                del request.session["attempts"] 



        except ValueError:
            result = "Invalid Input. Please Enter a Number" 


    return render(request, "Game/index.html", 
                  {"result": result,
                    "guess": guess if request.method == "POST" else None,
                    "number": request.session.get("number")
                   })
        