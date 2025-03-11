from enum import Enum

# State
class StudentStatusState(Enum):
    TERDAFTAR = "terdaftar"
    CUTI = "cuti"
    AKTIF = "aktif"
    LULUS = "lulus"

# Trigger Input
class TriggerInputState(Enum):
    CETAK_KSM = "cetak ksm"
    MENYELESAIKAIN_CUTI = "menyelesaikan cuti"
    LULUS = "lulus"
    MENGAJUKAN_CUTI = "mengajukan cuti"

# Transtition
state_transtition = {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI: {
        TriggerInputState.MENYELESAIKAIN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF: {
        TriggerInputState.LULUS: StudentStatusState.LULUS;
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    }
}

def change_state(curent_state, trigger_input):
    