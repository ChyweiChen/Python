class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            # THEN
            raise Exception("Invalid format")
        # ENDIF;
        self.filename = filename
    # END init()

# END CLASS.

class MP3File(AudioFile):

    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))
    # END play

# END CLASS.

class WAVFile(AudioFile):

    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))
    # END play

# END CLASS.

class OGGFile(AudioFile):

    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))
    # END play

# END CLASS.

file1 = MP3File("myfile.mp3")
file1.play()
file2 = WAVFile("myfile.wav")
file2.play()
file3 = OGGFile("myfile.ogg")
file3.play()
file4 = OGGFile("myfile.frog")
file4.play()
