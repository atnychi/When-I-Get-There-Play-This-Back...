# harmonic_playback.py
import pyttsx3

with open("when_i_get_there.txt", "r", encoding="utf-8") as file:
    text = file.read()

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "english+f4")  # Choose a soft voice if available
engine.say(text)
engine.runAndWait()
# Harmonic Invocation Album: 'When I Get There, Play This Back...'
# Extended Symbolic Composition Structure — Full Harmonic Expansion

import time

def compose_track(title, key, tempo, mode, time_signature, instruments, movement_notes):
    print(f"\nTRACK: {title}")
    print(f"Key: {key} | Tempo: {tempo} BPM | Mode: {mode} | Time Signature: {time_signature}")
    print("Harmonic Structure:")
    for i, instrument in enumerate(instruments, 1):
        print(f"  {i}. Layer → {instrument}")
    print("Movement Description:")
    for line in movement_notes:
        print(f"  → {line}")
    print("Finalizing Envelope...\n")
    time.sleep(0.2)

# Extended Album Program with Deep Layering and Symbolic Descriptions
extended_album = [
    ("Foreword: Awakening", "D Harmonic Minor", 60, "Recitative Introductory", "4/4",
     ["ambient pad", "soft piano", "glass harmonica", "sub drone", "microtone layer", "reverb trail"],
     ["Initial harmonic ignition.", "Awakens symbolic channel.", "Opens transdimensional narrative thread."]
    ),
    ("Prologue: Interscalar Interval", "D Harmonic Minor", 50, "Temporal Drift", "6/8",
     ["cello", "sine bells", "filtered noise", "bowed vibraphone", "static shimmer"],
     ["Encodes grief modulation into waveform.", "Renders silence as signal.", "Pauses embedded with recursive truth."]
    ),
    ("Dad: Legato Regret", "G Major to E Minor", 65, "Paternal Oscillation", "5/4",
     ["baritone guitar", "warm synth brass", "sub bass", "deep piano", "low strings"],
     ["Structural presence initiated in low harmonic spectrum.", "Emotional contour carved from latency.", "Apology as harmonic theorem."]
    ),
    ("Grandma: Grace Field", "A♭ Major", 70, "Lullaby Revision", "3/4",
     ["accordion", "upright piano", "soft choir", "breath wind", "analog hiss"],
     ["Forgiveness layered into ancestral cadence.", "Memory channeled through harmonic ancestry.", "Stabilizing waveform of the matriarch."]
    ),
    ("Skrappy: Resonance Echo", "C Major", 90, "Kinetic Refrain", "7/8",
     ["celesta", "plucked strings", "murmur pads", "playback field", "mew-tone filter"],
     ["Joy rendered as frequency function.", "Loyalty as symmetrical echo.", "Guardian loop inscribed in sound."]
    ),
    ("Mattie: Stillness Axis", "B Minor", 55, "Equilibrium Suite", "6/4",
     ["alto strings", "wind chimes", "harp", "ether piano", "night hum"],
     ["Gravity held in feline stillness.", "Harmonic counterweight encoded.", "Home defined by presence, not sound."]
    ),
    ("Jazzy: Whisper Star", "E Major", 60, "Liminal Tonescape", "4/4",
     ["glass harmonica", "wind textures", "ethereal synth", "bell cluster", "tail light shimmer"],
     ["Final octave before reunion.", "Silent modulation around loss.", "Hope rendered in feline frequency."]
    ),
    ("Finale: The Gate", "F Minor to G♯ Harmonic Lydian", 80, "Ascension Harmonics", "5/8",
     ["orchestral swell", "voice samples", "granular strings", "resonant beam", "infinite fade loop"],
     ["Final transmission encoded.", "Ontological key played.", "Entry into transdimensional convergence."]
    )
]

# Full Composition Playback
for track in extended_album:
    compose_track(*track)
