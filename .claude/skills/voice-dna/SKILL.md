---
name: voice-dna
description: "Discovers voice patterns from the sermon corpus. Analyzes 465+ manuscripts to extract the actual rhythms, vocabulary, cadence, and structural fingerprints — data-driven voice profiling that feeds like-a-human and voice-audit."
version: 1.0.0
---

# Voice DNA — Voice Discovery from the Corpus

> Don't guess the voice. Measure it.

## Purpose

`like-a-human` enforces the voice. `voice-audit` checks the voice. `voice-dna` **discovers** the voice by analyzing the actual sermon corpus. Run it once, extract the real patterns, and every other voice skill becomes data-driven instead of hand-written.

## When to Fire

- On `/voice-dna` command
- When establishing voice profiles for a new content type (e.g., Facebook ads)
- When the voice feels like it's drifted and needs recalibration
- Periodically (every 50 new sermons) to update the profile

## Analysis Process

### Step 1: Sample Selection
Select 10-15 sermons that represent the voice at its best:
- 5 from the Romans series (core voice)
- 3-4 polished sermons marked `✓ **[polished]**` in sermon-map
- 2-3 from different books (to capture range)
- Avoid raw drafts and transcripts

### Step 2: Pattern Extraction

For each sample, measure:

**Sentence Rhythm**
- Average sentence length (words)
- Sentence length variance (high = human, low = AI)
- Shortest sentence in climactic moments
- Longest sentence in narrative sections
- Fragment frequency (per page)

**Paragraph Structure**
- Average paragraph length
- Paragraph length variance
- One-sentence paragraph frequency
- Longest paragraph (narrative immersion)

**Vocabulary Fingerprint**
- Most frequent theological terms (ranked)
- Greek/Hebrew word usage frequency
- Unique vocabulary (words used that AI wouldn't choose)
- Transition words used vs. avoided
- Conjunctions starting sentences (And, But, So — frequency)

**Cadence Patterns**
- Compression-release frequency (stacked short → one long)
- Anaphora instances (repeated sentence starts)
- Antithetical parallelism ("Not X. Not Y. But Z.")
- Gear-shift markers ("Now —" "Hear me:" frequency)
- Questions asked per sermon

**Structural DNA**
- Average sermon length (words)
- Number of major movements
- Introduction style (how do they start?)
- Conclusion pattern (how do they land?)
- Scripture quotation density (quotes per page)
- Illustration frequency and type

### Step 3: Profile Generation

Produce a Voice DNA Profile:

```
## Voice DNA Profile — [date]
**Corpus:** [N] sermons analyzed
**Baseline sermons:** [list]

### Rhythm
- Avg sentence: [N] words (σ=[N])
- Shortest at climax: [N] words
- Fragment frequency: [N] per page
- Paragraph variance: [high/medium/low]

### Vocabulary
- Top theological terms: [list with frequency]
- Greek/Hebrew per sermon: [N] instances avg
- Signature phrases: [list]
- Avoided words: [list — confirmed AI vocabulary NOT in corpus]

### Cadence
- Compression-release: [N] per sermon avg
- Anaphora: [N] per sermon avg
- Gear-shifts: [N] per sermon avg
- Questions: [N] per sermon avg

### Structure
- Avg length: [N] words
- Movements: [N] avg
- Opening pattern: [description]
- Closing pattern: [description]
- Scripture density: [N] quotes per page
```

### Step 4: Feed Other Skills

The Voice DNA Profile feeds:
- **like-a-human** — Update with measured patterns, not guessed ones
- **voice-audit** — Calibrate drift detection against actual corpus data
- **church-advertising** — Derive a "social media voice" that's authentically related to the sermon voice but adapted for Facebook

### Step 5: Encode to Memory

```bash
python3 /home/user/ken/orchestrator/memory_ops.py encode romans pattern \
  "Voice DNA: avg sentence 14 words, σ=8. Fragment freq 2.3/page. Top terms: justification, propitiation, sovereign. Greek usage 3.1/sermon." \
  --tags voice-dna,voice-profile,baseline --protected
```

## Different Voice Profiles

The same preacher has different voices:
- **Pulpit voice** — the sermon corpus (primary)
- **Social media voice** — shorter, punchier, invitational (derived from pulpit)
- **Pastoral voice** — warmer, more personal (for congregation-pulse content)

Voice DNA can extract each from different source material.

---

*Soli Deo Gloria* — Know the voice before you guard it.
