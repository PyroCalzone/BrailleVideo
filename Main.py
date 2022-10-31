from braildict import brailleDictionary
import os
import skvideo.io
from time import sleep


def convertToBraille(code): #1234 -> ⠏, 125 -> ⠓
    return brailleDictionary[code]
    
def resizeVideo(file, scale):
    textSplit = file.split('.')
    os.system(f'ffmpeg -i {file} -vf scale={scale}:{scale} {textSplit[0]}{scale}.mp4')
    return f'{textSplit[0]}{scale}.mp4'

def audioFromVideo(file):
    textSplit = file.split('.')
    os.system(f'ffmpeg -i {file} {textSplit[0]}.mp3')
    return f'{textSplit[0]}.mp3'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def convertVideo(file, compression=1):
    viddat = skvideo.io.vread(file, as_grey=True)
    videometadata = skvideo.io.ffprobe(file)
    width = int(videometadata['video']['@width'])
    height = int(videometadata['video']['@height'])
    fps = int(videometadata['video']['@avg_frame_rate'].split('/')[0])//1
    compressed = viddat[1::compression]
    frames = []
    if compression != 1:
        print(f"Compressed video to {fps//compression} FPS")
    #Throw errors if height or width is not divisible by 4 or 2
    if height % 4 != 0:
        raise Exception("Video height is not divisible by 4")
    if width % 2 != 0:
        raise Exception("Video Width is not divisible by 2")

    for frame in compressed[3:]:
        blackAndWhite = []

        for currentRow in frame:
            row = []
            for c in currentRow:
                value = c
                row.append( 0 if value < (255/2) else 1 )
            blackAndWhite.append(row)

        brailleFrame = []
        for i in range(0, height//4):
            brailleFrame.append([])
            for j in range(0, width//2):
                brailleFrame[i].append([])

        #Populate brailleFrame
        for rowIndex, row in enumerate(blackAndWhite):
            for colIndex, item in enumerate(row):
                brailleFrame[rowIndex // 4][colIndex // 2].append(item)
        
        #convert each item of brailleFrame to a braille character
        for rowIndex, row in enumerate(brailleFrame):
            for colIndex, item in enumerate(row):
                brailleString = ''
                for xIndex, x in enumerate(item):
                    if x == 1:
                        brailleString += str(xIndex + 1)
                brailleFrame[rowIndex][colIndex] = convertToBraille(brailleString)

        frames.append(brailleFrame)
    return (fps//compression, frames)

def playVideo(fps, frames, audioFile = None):
    height = len(frames[0])
    width = len(frames[0][0])
    import pygame
    pygame.init()
    if audioFile != None:
        pygame.mixer.init()
    screen = pygame.display.set_mode((width*15, height*25))
    pygame.display.set_caption("Braille Video Player")
    clock = pygame.time.Clock()
    font = pygame.font.Font('Fonts/DejaVuSans.ttf', 20)
    if audioFile != None:
        pygame.mixer.music.load(audioFile)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play()
    for frame in frames:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0,0,0))
        for rowIndex, row in enumerate(frame):
            for colIndex, item in enumerate(row):
                text = font.render(item, True, (255,255,255))
                screen.blit(text, (colIndex*15, rowIndex*25))
        pygame.display.flip()
        clock.tick(fps)
    if audioFile != None:
        pygame.mixer.music.stop()
    pygame.quit()

def playVideoTerminal(fps, frames):
    for frame in frames:
        print(frame)
        for row in frame:
            for item in row:
                print(item, end='')
            print()
        sleep(1/fps)
        input()


if __name__ == '__main__':
    videoFile = 'Example/BadApple88.mp4'
    audioFile =  'Example/BadApple.mp3'
    fps, frames = convertVideo(videoFile, compression=2)
    playVideo(fps, frames, audioFile=audioFile)