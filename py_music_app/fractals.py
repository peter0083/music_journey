# reference: https://www.youtube.com/watch?v=-ULt_LiHftI
# reference2: https://medium.com/analytics-vidhya/how-to-create-a-music-visualizer-7fad401f5a69
# reference3: https://gitlab.com/avirzayev/medium-audio-visualizer-code/-/blob/master/main.py

import pygame
import sys
import math
import colorsys
import librosa
import numpy as np


class LSystem():
    def __init__(self, axiom, rules, angle, start, length, ratio):
        self.sentence = axiom
        self.rules = rules
        self.angle = angle
        self.start = start
        self.x, self.y = start
        self.length = length
        self.ratio = ratio
        self.theta = math.pi / 2
        self.positions = []

    def __str__(self):
        return self.sentence

    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio
        new_sentence = ""
        for char in self.sentence:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            new_sentence += mapped
        self.sentence = new_sentence

    def draw(self, screen):
        hue = 0
        for char in self.sentence:
            if char == 'F':
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(screen, (hsv2rgb(hue, 1, 1)), (self.x, self.y), (x2, y2), 2)
                self.x, self.y = x2, y2
            elif char == '+':
                self.theta += self.angle
            elif char == '-':
                self.theta -= self.angle
            elif char == '[':
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char == ']':
                position = self.positions.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']
            hue += 0.00005


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


### audio visualizer
def clamp(min_value, max_value, value):

    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):

        self.x, self.y, self.freq = x, y, freq

        self.color = color

        self.width, self.min_height, self.max_height = width, min_height, max_height

        self.height = min_height

        self.min_decibel, self.max_decibel = min_decibel, max_decibel

        self.__decibel_height_ratio = (self.max_height - self.min_height)/(self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):

        desired_height = decibel * self.__decibel_height_ratio + self.max_height

        speed = (desired_height - self.height)/0.1

        self.height += speed * dt

        self.height = clamp(self.min_height, self.max_height, self.height)

    def render(self, screen):

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))

filename = "../music_app/src/audio/Flower_Sample.wav"

time_series, sample_rate = librosa.load(filename)  # getting information from the file

# getting a matrix which contains amplitude values according to frequency and time indexes
stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))

spectrogram = librosa.amplitude_to_db(stft, ref=np.max)  # converting the matrix to decibel matrix

frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies

# getting an array of time periodic
times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)

time_index_ratio = len(times)/times[len(times) - 1]

frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]

def get_decibel(target_time, freq):
    return spectrogram[int(freq * frequencies_index_ratio)][int(target_time * time_index_ratio)]



### end of audio visualizer

# mix pygame logic from both scripts
l_system_text = sys.argv[1]
start = int(sys.argv[2]), int(sys.argv[3])
length = int(sys.argv[4])
ratio = float(sys.argv[5])

with open(l_system_text) as f:
    axiom = f.readline()
    num_rules = int(f.readline())
    rules = {}
    for i in range(num_rules):
        rule = f.readline().split(' ')
        rules[rule[0]] = rule[1]
    angle = math.radians(int(f.readline()))


def main():
    pygame.init()

    infoObject = pygame.display.Info()

    screen_w = int(infoObject.current_w/2.5)
    screen_h = int(infoObject.current_w/2.5)


    # Set up the drawing window
    screen = pygame.display.set_mode([screen_w, screen_h])
    pygame.mouse.set_visible(False)

    bars = []
    frequencies = np.arange(100, 8000, 100)
    r = len(frequencies)
    width = screen_w/r
    x = (screen_w - width*r)/2

    for c in frequencies:
        bars.append(AudioBar(x, 300, c, (255, 0, 0), max_height=400, width=width))
        x += width

    t = pygame.time.get_ticks()
    getTicksLastFrame = t


    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)

    fractal = LSystem(axiom, rules, angle, start, length, ratio)

    running = True
    while running:
        
        # Fill the background with white
        screen.fill((255, 255, 255))

        # fractal generation
        # fractal.draw(screen)
        # fractal.generate()

        t = pygame.time.get_ticks()
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t

        # Did the user click the window close button?
        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                pygame.quit()

        for b in bars:
            b.update(deltaTime, get_decibel(pygame.mixer.music.get_pos()/1000.0, b.freq))
            b.render(screen)

        # flip the display
        pygame.display.flip()



main()


# Adrian-Mariano-Doily             python fractals.py fractals/Adrian_Mariano_Doily.txt 1350 350 110 0.5
# Anthony-Hanmer-ADH231a           python fractals.py fractals/Anthony_Hanmer_ADH231a.txt 960 1000 50 0.52
# Anthony-Hanmer-ADH256a           python fractals.py fractals/Anthony_Hanmer_ADH256a.txt 650 850 50 0.55
# Anthony-Hanmer-ADH258a           python fractals.py fractals/Anthony_Hanmer_ADH258a.txt 700 950 80 0.4
# Board                            python fractals.py fractals/board.txt 500 1000 100 0.52
# Box-fractal                      python fractals.py fractals/box-fractal.txt 1400 1000 100 0.52
# Classic-Sierpinski-curve         python fractals.py fractals/classic-sierpinski-curve.txt 1150 750 30 0.5
# Cross                            python fractals.py fractals/cross.txt 950 250 250 0.5
# Crystal:                         python fractals.py fractals/crystal.txt 580 920 100 0.5
# Dragon-curve:                    python fractals.py fractals/dragon-curve.txt 960 540 200 0.75
# Hilbert-curve                    python fractals.py fractals/hilbert-curve.txt 1920 1080 250 0.67
# Hilbert-curve-II                 python fractals.py fractals/hilbert-curve-II.txt 0 1080 50 0.7
# Koch-snowflake:                  python fractals.py fractals/koch-snowflake.txt 1200 900 100 0.5
# Krishna-anklets                  python fractals.py fractals/krishna-anklets.txt 1400 550 60 0.8
# Levy-curve                       python fractals.py fractals/levy-curve.txt 1100 750 70 0.8
# Moore-curve                      python fractals.py fractals/moore-curve.txt 1000 1080 50 0.8
# no_name                          python fractals.py fractals/no_name.txt 960 1020 120 0.51
# Peano-curve                      python fractals.py fractals/peano-curve.txt 0 1080 70 0.7
# Peano-Gosper-curve:              python fractals.py fractals/peano-gosper-curve.txt 600 280 200 0.5
# Pentaplexity                     python fractals.py fractals/pentaplexity.txt 550 850 150 0.5
# Plant:                           python fractals.py fractals/plant.txt 960 1000 100 0.6
# Quadratic-Gosper                 python fractals.py fractals/quadratic-gosper.txt 1920 1080 70 0.61
# Quadratic-Koch-island            python fractals.py fractals/quadratic-koch-island.txt 950 850 50 0.5
# Quadratic-snowflake              python fractals.py fractals/quadratic-snowflake.txt 500 1000 50 0.52
# Rings:                           python fractals.py fractals/rings.txt 700 250 60 0.5
# Sierpinski-arrowhead             python fractals.py fractals/sierpinski-arrowhead.txt 1300 1000 90 0.7
# Sierpinski-carpet                python fractals.py fractals/sierpinski-carpet.txt 500 1020 50 0.6
# Sierpinski-curve:                python fractals.py fractals/sierpinski-curve.txt 500 550 200 0.52
# Sierpinski-sieve:                python fractals.py fractals/sierpinski-sieve.txt 1200 950 400 0.5
# Terdragon-curve                  python fractals.py fractals/terdragon-curve.txt 400 500 200 0.7
# Three-dragon-curve               python fractals.py fractals/three-dragon-curve.txt 600 550 40 0.88
# Tiles                            python fractals.py fractals/tiles.txt 900 800 30 0.75
# Tree:                            python fractals.py fractals/tree.txt 960 950 250 0.5
# Triangle                         python fractals.py fractals/triangle.txt 1000 250 60 0.8
# Twin-dragon-curve                python fractals.py fractals/twin-dragon-curve.txt 1000 250 90 0.8
# William-McWorter-Maze01          python fractals.py fractals/William_McWorter_Maze01.txt 1100 750 50 0.8
# William-McWorter-Moore           python fractals.py fractals/William_McWorter_Moore.txt 900 350 100 0.5
# William-McWorter-Pentant         python fractals.py fractals/William_McWorter_Pentant.txt 1000 120 90 0.39
# William-McWorter-Pentl           python fractals.py fractals/William_McWorter_Pentl.txt 1400 400 90 0.5