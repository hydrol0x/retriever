from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume


# Name will be .exe name for the app
def set_volume(name: str):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        print(session.Process.name())
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == name:
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(0.6, None)

# TODO: make cmd line args