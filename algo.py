import shots
import scenes
import subshots

class SceneObject:
    def __init__(self, starttime, endttime):
        self.starttime = starttime
        self.endttime = endttime
        self.shots = []

    def addShot(self, shot):
        self.shots.append(shot)

class ShotObject:
    def __init__(self, starttime, endtime):
        self.starttime = starttime
        self.endtime = endtime
        self.subshots = []

class SubShotObject:
    def __init__(self, starttime):
        self.starttime = starttime

video_file = "The_Great_Gatsby_rgb/InputVideo.rgb"
audio_file = "The_Great_Gatsby_rgb/InputAudio.wav"
frame_width = 480
frame_height = 270

shotList = shots.getshots(video_file, frame_width, frame_height)
sceneList = scenes.getscenes(video_file, audio_file)
subshotList = subshots.getsubshots(video_file, frame_width, frame_height)

sortedFormattedData = []

for scene in sceneList:
    sceneObject = SceneObject(scene[0], scene[1])
    sortedFormattedData.append(sceneObject)

for shot in shotList:
    shortStart = shot[0]
    shortEnd = shot[1]
    shotObject = ShotObject(shortStart, shortEnd)

    for scene in sortedFormattedData:
        if scene.starttime <= shotObject.starttime <= scene.endttime:
            scene.addShot(shotObject)

for subshot in subshotList:
    subshotObject = SubShotObject(subshot)

    for scene in sortedFormattedData:
        for shot in scene.shots:
            if shot.starttime <= subshotObject.starttime <= shot.endtime:
                shot.subshots.append(subshotObject)

# code to print scenes, shot and subshots
for scene in sortedFormattedData:
    print("Scene: ", scene.starttime, scene.endttime)

    for shot in scene.shots:
        print("\tShot: ", shot.starttime, shot.endtime)

        for subshot in shot.subshots:
            print("\t\tSubshot: ", subshot.starttime)

    print("\n")

