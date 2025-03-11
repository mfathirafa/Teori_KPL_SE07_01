from enum import Enum

class JenisKelamin(Enum):
    Laki_Laki = 1
    PEREMPUAN = 2

print(JenisKelamin.Laki_Laki) ## JenisKelamin.LAKI_LAKI
print(JenisKelamin.Laki_Laki.value) ## Value dari laki laki ==> 1
print(JenisKelamin.Laki_Laki.name) ## Nama enum ==> Laki_Laki