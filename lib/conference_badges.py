def badge_maker(name):
# add the f' ' and {name} to the rturn
# Module conference_badges.py contains a function "badge_maker()" that creates and returns a badge. 
# - AssertionError: assert None == 'Hello, my name is Guido van Rossum.'
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
# add the f' ' and {name} fot name in name to the return
#Module conference_badges.py contains a function "batch_badge_creator()" that creates and returns a list of badges. 
# - AssertionError: assert <class 'NoneType'> == list 
     return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
# add rooms range
    rooms = range(1, 9)
# add addigned [] for room in room and append  and for room in rooms 
    assignments = []
    for room in rooms:
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    
    return assignments
#Module conference_badges.py contains a function "assign_rooms" that returns a list of welcome messages and room assignments. 
# - AssertionError: assert <class 'NoneType'> == list 

def printer(names):
# add for badge in batch_badge_creator(names) and add print badge
    for badge in batch_badge_creator(names):
        print(badge)
    
# add for assigned in assing_rooms(names) and print assignemnts 
    for assignment in assign_rooms(names):
        print(assignment)
#Module conference_badges.py contains a function "printer" that outputs the list of badges and room assignments. 
# - AssertionError: assert '' == 'Hello, my na... to room 8!\n' 


