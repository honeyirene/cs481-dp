import tarfile

emotion_annotations = tarfile.open("../emotion_annotations.tar.gz")
emotion_annotations.extractall('../')
emotion_annotations.close()
print(emotion_annotations.getnames())

"""debate_recordings = tarfile.open("../debate_recordings.tar.gz")
debate_recordings.extractall('../')
debate_recordings.close()
print(debate_recordings.getnames())"""

"""e4_data = tarfile.open("../e4_data.tar.gz")
e4_data.extractall('../')
e4_data.close()
print(e4_data.getnames())"""

"""neurosky_polar_data = tarfile.open("../neurosky_polar_data.tar.gz")
neurosky_polar_data.extractall('../')
neurosky_polar_data.close()
print(neurosky_polar_data.getnames())"""