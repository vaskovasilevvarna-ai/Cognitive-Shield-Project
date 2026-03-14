# Threat Pattern Library
### Cognitive Shield Manipulation Pattern Framework

The Threat Pattern Library (TPL) is an evolving component of Cognitive Shield.

It provides a structured framework for identifying, classifying, and analyzing manipulation patterns, narrative attack structures, cognitive exploitation mechanisms, and information influence strategies.

This library is intentionally designed as a living system.  
Patterns will continuously expand, refine, split, merge, and mature as new manipulation strategies are identified and better formalized.

---

# Purpose

The purpose of the Threat Pattern Library is to give Cognitive Shield a formal pattern-based foundation for detecting manipulative content.

Instead of treating harmful influence as an unstructured phenomenon, the library models it as a set of recurring, analyzable, and explainable pattern types.

The TPL supports:

- pattern-based detection
- claim-level analysis
- explainable reasoning
- structured risk scoring
- future extension and versioning

---

# Design Philosophy

The Threat Pattern Library follows several core principles.

## 1. Pattern-first detection
Manipulation is treated as a repeatable structural phenomenon, not as an isolated event.

## 2. Explainable classification
Patterns must be understandable by both system developers and end users.

## 3. Localization
Patterns should be attached to specific claims, frames, or message segments whenever possible.

## 4. Evolution over rigidity
The library is not fixed. It is expected to grow as new manipulation techniques emerge.

## 5. Architectural compatibility
The library must remain compatible with the broader Cognitive Shield pipeline, especially message decomposition, risk scoring, and explainable output generation.

---

# Role in Cognitive Shield

Within the Cognitive Shield architecture, the Threat Pattern Library functions as the formal knowledge layer for manipulation pattern recognition.

It supports the following system components:

- Message Decomposition
- Narrative Analysis
- Evidence Analysis
- Cognitive Risk Analysis
- Cross-Lingual Verification
- Shield Decision
- Explainable Interface

The TPL does not replace judgment.  
It provides structured pattern intelligence that contributes to downstream reasoning.

---

# Pattern Categories

The library currently organizes manipulation patterns into several broad classes.

## A. Narrative Manipulation Patterns
Patterns that distort perception through framing, sequencing, selective context, symbolic emphasis, or emotional narrative structure.

Examples include:

- false dilemma framing
- scapegoat framing
- moral panic activation
- hero-victim-villain simplification
- selective causal chaining

## B. Cognitive Exploitation Patterns
Patterns that exploit predictable vulnerabilities in human cognition.

Examples include:

- fear amplification
- outrage triggering
- urgency pressure
- identity fusion pressure
- repetition-based internalization

## C. Evidence Distortion Patterns
Patterns that manipulate the evidentiary layer of a message.

Examples include:

- unsupported certainty
- selective evidence exposure
- false authority invocation
- anecdotal substitution
- misleading comparison structures

## D. Semantic Distortion Patterns
Patterns that alter meaning, interpretation, or conceptual boundaries.

Examples include:

- equivocation
- strategic ambiguity
- label contamination
- concept shifting
- translation distortion

## E. Propagation and Influence Patterns
Patterns optimized for spread, memorability, and social adoption.

Examples include:

- slogan compression
- virality hooks
- emotional replication triggers
- binary alignment pressure
- narrative contagion structures

---

# Canonical Pattern Template

Each pattern in the Threat Pattern Library should be described using a common template.

## Pattern Fields

### Pattern Name
The stable descriptive name of the pattern.

### Pattern ID
A unique identifier for internal reference and future versioning.

### Category
The broader class to which the pattern belongs.

### Definition
A concise explanation of what the pattern is.

### Mechanism
A description of how the pattern operates.

### Cognitive Target
The human cognitive vulnerability or response tendency that the pattern attempts to exploit.

### Typical Signals
Observable indicators that may suggest the presence of the pattern.

### Common Linguistic Markers
Words, phrases, constructions, or rhetorical forms often associated with the pattern.

### Context Dependencies
Conditions under which the pattern becomes more or less likely.

### False Positive Risks
Cases in which the pattern may be incorrectly detected.

### Severity Contribution
How strongly the pattern should affect risk scoring.

### Related Patterns
Other patterns frequently co-occurring with it.

### Example Structure
A schematic example of how the pattern may appear in a message.

---

# Example Pattern Entry

## Pattern Name
False Dilemma Framing

### Pattern ID
TPL-NAR-001

### Category
Narrative Manipulation Pattern

### Definition
A pattern that artificially reduces a complex situation to two mutually exclusive options in order to constrain reasoning and force alignment.

### Mechanism
The message removes intermediate positions, suppresses nuance, and presents a binary choice as inevitable.

### Cognitive Target
Need for clarity, rapid decision pressure, uncertainty reduction.

### Typical Signals
- binary opposition language
- elimination of alternative positions
- forced alignment framing
- reduction of complexity

### Common Linguistic Markers
- "either ... or ..."
- "there are only two choices"
- "if you are not with X, you are with Y"
- "no middle ground"

### Context Dependencies
This pattern is stronger in political, moral, ideological, and crisis communication.

### False Positive Risks
Some situations genuinely do involve binary constraints. Context matters.

### Severity Contribution
Medium to high, depending on supporting pattern cluster.

### Related Patterns
- urgency pressure
- identity fusion pressure
- scapegoat framing

### Example Structure
A message frames a social issue as containing only two legitimate positions and delegitimizes all intermediate views.

---

# Pattern Topology Logic

Patterns should not be viewed as isolated units only.

The TPL assumes that many manipulation mechanisms form clusters, chains, or layered structures.

Examples:

- fear amplification + urgency pressure + false dilemma
- selective evidence + false authority + certainty inflation
- scapegoat framing + identity fusion + moral panic

This means that Cognitive Shield should support both:

- single-pattern detection
- pattern cluster detection

---

# Detection Orientation

The Threat Pattern Library is designed to support explainable detection, not black-box labeling.

Pattern detection should ideally answer:

- what pattern may be present
- what signals support that interpretation
- how confident the system is
- what alternative interpretations remain possible

This preserves transparency and reduces overreach.

---

# Versioning Principle

The Threat Pattern Library is an evolving document.

Future versions may:

- add new patterns
- split broad patterns into more precise subtypes
- merge overlapping patterns
- revise definitions
- improve signal descriptions
- recalibrate severity contribution rules

Because manipulation evolves, the library must evolve as well.

---

# Strategic Importance

The Threat Pattern Library is one of the core foundations of Cognitive Shield.

It transforms the project from a generic AI analysis concept into a structured cognitive defense system with explicit pattern intelligence.

In the long term, the TPL may grow into a broader open taxonomy of manipulation and cognitive attack structures.

---

# Status

Current status: foundational specification.

This document defines the conceptual and structural basis of the library.  
Future iterations may extend it with:

- formal scoring hooks
- machine-readable schemas
- detection rules
- multilingual examples
- topology maps
- pattern relationships
- benchmark datasets

---

# License

This file is part of the Cognitive Shield project and is released under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
