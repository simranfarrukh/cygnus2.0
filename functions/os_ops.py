# Offline (OS) Operations
import os  # use the os system to work offline programs
import subprocess as sp  # run commands

# dictionary called paths that contains the software names as keys
# and the path to the software as the value
paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'word': "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'powerpoint': "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    'spreadsheets': "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'youtube downloader': "C:\\Program Files\\4KDownload\\4kvideodownloader\\4kvideodownloader.exe",
    'computer health': "C:\\Program Files\\PCHealthCheck\\PCHealthCheck.exe",
    'photoshop': "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe",
    'skype': "C:\\Program Files\\Microsoft Office\\root\\Office16\\lync.exe",
    'unity': "C:\\Program Files\\Unity Hub\\Unity Hub.exe",
    'settings': f"%windir%\\System32\\Control.exe",
    'itunes': "C:\\Program Files\\iTunes\\iTunes.exe"
}


def open_webcam():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_word():
    os.startfile(paths['word'])


def open_calculator():
    os.Popen(paths['calculator'])


def open_powerpoint():
    os.startfile(paths['powerpoint'])


def open_spreadsheets():
    os.startfile(paths['spreadsheets'])


def open_health():
    os.startfile(paths['computer health'])


def open_downloader():
    os.startfile(paths['youtube downloader'])


def open_photoshop():
    os.startfile(paths['photoshop'])


def open_skype():
    os.startfile(paths['skype'])


def open_unity():
    os.startfile(paths['unity'])


def open_itunes():
    os.startfile(paths['itunes'])


def open_settings():
    os.startfile(paths['settings'])


def open_cmd():
    os.system('start cmd')
