from collections import namedtuple
import hashlib

def getAllData(personal_details, complexion):
    return { 
        "DateOfBirth": personal_details.date_of_birth,
        "EyeColor": complexion.eye_color,
        "HairColor": complexion.hair_color,
        "Patient": hashlib.sha256((personal_details.date_of_birth + "_" + complexion.eye_color + "_" + complexion.hair_color).encode()).hexdigest()
    }



PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')

print(getAllData(personal_details, complexion))