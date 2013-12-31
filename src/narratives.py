def yes_value(response):
    '''Returns True if a response is intended to be a Yes
       Returns False if a response is intended to be a No
       Returns None if response is blank or irrelevant'''
    if response.lower() in ['yes','y']:
        return True
    elif response.lower() in ['no','n']:
        return False
    else:
        return None

def gender(response):
    '''Returns dictionary of gender pronouns for student'''
    if response.lower() in ['male','m','boy','b']:
        return {'subject':'he','object':'him'}
    
    #guarantees a response
    else:
        return {'subject':'she','object':'her'}


#functions for generating strings based on response of user
def average(student):
    response = ''
    try:
        response = "{0} currently has an average of {1}.".format\
                            (student['name'],student['current average'])
    except KeyError:
        pass
    return response

def participates(student):
    gender_nouns = gender(student['gender'])
    if yes_value(student['participates?']):
        return ('{0} always manages to push the class forward in mathematical'
                ' discussion by commenting on what other students have to say'
                ' or offering new questions to consider. '
                ).format(gender_nouns['subject'].capitalize())
    else:
        return ('{0} could get more out of this class if he participated. '
                'more actively.').format(gender_nouns['subject'].capitalize())

def strong_ability(student):
    gender_nouns = gender(student['gender'])
    if yes_value(student['strong math ability?']):
        return ('{0} is a student with strong mathematical ability. '
                ).format(student['name'].capitalize())
    else:
        return ''

def does_homework(student):
    gender_nouns = gender(student['gender'])
    if not yes_value(student['does homework?']):
        return('{0} does not finish his homework regularly and on time. '
               'If {1} did, it would help his grade significantly. '
               ).format(student['name'].capitalize(),gender_nouns['subject'])
    else:
        return ''

def on_time(student):
    gender_nouns = gender(student['gender'])
    if not yes_value(student['on time?']):
        return ('{0} is frequently late to class, which is significantly '
                'impacting {1} performance. '
                ).format(student['name'].capitalize(),gender_nouns['object'])
    else:
        return ''

def tutoring(student):
    gender_nouns = gender(student['gender'])
    if yes_value(student['should attend tutoring?']):
        return ('{0} should attend tutoring regularly in order to make sure '
            'that {1} succeeds in my class. '
             ).format(student['name'].capitalize(), gender_nouns['object'])

def additional_comments(student):
    try:
        return student['additional comments?']
    except KeyError:
        return ''

def first_name(student):
    full_name = student['name']
    names = full_name.split()
    if len(names) > 1:
        return names[0]
    else:
        return full_name
    

def narrative(student):
    #make sure only use first name in narrative
    student['name'] = first_name(student)
    
    #generate narrative
    narrative = ''
    narrative += average(student)
    narrative += strong_ability(student)
    narrative += participates(student)
    narrative += does_homework(student)
    narrative += on_time(student)
    narrative += tutoring(student)
    narrative += additional_comments(student)
