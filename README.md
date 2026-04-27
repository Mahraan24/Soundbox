# Soundbox
An audio synthesiser built from scratch in Python, exploring the fundamentals of digital audio synthesis — additive harmonics, ADSR envelopes, and digital filtering.

---

## What it does

Soundbox generates musical notes programmatically by simulating how real instruments produce sound physically. Given a frequency, amplitude, and duration, it builds an audio signal by:

1. **Summing harmonic overtones** — real instruments don't produce a single frequency but a series of overtones. Soundbox replicates this using additive synthesis, stacking harmonics weighted by `1/n`.
2. **Shaping with an ADSR envelope** — attack, decay, sustain, and release control the life cycle of a note, giving each instrument its characteristic feel.
3. **Filtering** — a one-pole low-pass filter that removes harsh high frequencies, adding warmth to the sound.
4. **Vibrato** — a subtle frequency modulation makes sustained notes feel alive rather than static.

---

## Project structure

```
soundbox/
├── wave_generator.py     # Raw oscillators: sine, square, sawtooth, triangle
├── ADSR.py               # ADSR envelope generator
├── filter.py             # Low-pass filter
├── instrument_store.py   # Instrument presets bundling wave type, harmonics, filter, and ADSR
├── note_creator.py       # Orchestrates the full synthesis pipeline
└── main.py               # Entry point — plays notes or sequences
```

---

## How the pipeline works

```
Oscillator → Harmonic summation → Normalize → Vibrato → Filter → ADSR → Audio output
```

Each stage is a separate, independently testable module. No stage knows about the others — they communicate only through numpy arrays.

---

## Instrument presets

| Instrument     | Wave type | Harmonics | Filter (`a`)  |
|----------------|-----------|-----------|---------------|
| Piano          | Triangle  | 8         | 0.80          |
| Acoustic guitar| Sawtooth  | 6         | 0.60          |
| Violin         | Sawtooth  | 15        | 0.50          |
| Flute          | Sine      | 3         | 0.35          |

---


## Installation

```bash
pip install numpy sounddevice
```

Then run:

```bash
python main.py
```

---

## What I learned

- How digital audio works at the sample level
- Additive synthesis and the Fourier basis of timbre
- ADSR envelope design using the idea of a deterministic state machine and sample-accurate phase budgeting
-  Filter design and the Nyquist limit
- How instrument character emerges from the combination of wave shape, harmonics, filtering, and envelope

---

## Planned improvements

- FM synthesis for more realistic timbres
- Reverb and stereo
- A melody generator based on group theory (mapping algebraic structures to musical sequences)
- To turn this to a backend server that sends audio as numpy arrays via API calls to help in building my future webapps based on audios.