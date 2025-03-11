from enum import Enum

class JenisKelamin(Enum):
    Pria = 1
    Wanita = 2

patients = []

def add_patients(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis Kelamin harusnya adalah Pria atau Wanita")
    patients.append({"name":name, "gender":gender.name})

add_patients("Adit", JenisKelamin.Pria)
add_patients("Mamah Adit", JenisKelamin.Wanita)


for patients in patients:
    print (f"{patients['name']} adalah {patients['gender']}")