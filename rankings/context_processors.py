from .playerMatches import playerMatches

def add_variable_to_context(request):
    return {
        'playerData': playerMatches
    }