# The point of this programme is to set an alarm 
# with certain conditions

# the condition for it to be true is if a
# person is an employee and not on vacation.

# else we don't set the alarm

def set_alarm(employed, vacation):
    if (employed == True) and (vacation == False):
        return True
    
    return False

set_alarm(True, True) # expected False
set_alarm(True, False) # expected True
set_alarm(False, True) # expected False
set_alarm(False, False) # expected False
