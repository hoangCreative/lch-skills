---
pack: vietnamese
name: Vietnamese culture-pack
for_engine: what-for-and-how
engine_version: ">=3.1.0"
language: vi
status: reference_implementation
author: Le Cong Hoang
license: Apache-2.0
version: 0.1.0
created: 2026-06-22
provenance: derived from a multi-council linguistic and cultural critique (Vietnamese, Anglophone, general-linguistics panels); see Provenance section for verification status
---

# Vietnamese culture-pack (reference implementation)

> This is ONE culture's pack for the what-for-and-how engine, labeled honestly as such. It is not the canon. It is the first reference pack, written to show contributors what a pack looks like and to ground the engine in a non-Anglophone case. Vietnamese is itself internally diverse (Northern, Central, Southern), and this pack tries not to collapse that diversity into one accent.

This pack supplies four things the engine plugs in: extra TERMINUS types, a SPEECH-ACT repertoire, language-specific PARSER SIGNALS, and CLINICAL display norms. It never changes the mechanism.

A standing caution that shaped every entry below: there is no single homogeneous "Vietnamese culture". Northern face-display, Central (Hue) restraint, and Southern openness are different in kind, not three shades of one. When this pack says "Vietnamese", read it as "load the regional reading that fits the speaker", not "apply a default Northern reading". [C1]

---

## 1. Triggers (added to the engine)

Explicit-invocation phrases in Vietnamese that should show the full cascade:
- "what for va how", "wfh"
- "dao dong co", "tai sao that su", "5 vi sao den day", "what for den tan cung"

Auto-trigger decision phrases (the engine already fires on decision/why shape; these are the Vietnamese surface forms): "co nen...", "toi dang phan van...", "nen lam X hay Y", "tai sao [he / hien tuong / nhom] lai...".

---

## 2. Terminus map additions (Vietnamese floors)

The engine ships the relational/role terminus as a universal PRINCIPLE. This pack names WHICH roles and goods count as floors in Vietnamese contexts, and how they differ by region. Each is a legitimate place to stop; forcing it into individual-need language ("autonomy", "self-actualization") distorts it.

- **Chu hieu (filial duty).** "O lai cham ba me", "khong di xa vi me yeu" can bottom out at the role of child to parent. The floor is the duty itself, not "my need for meaning". [C2]
- **Relational debt ("khong phu long").** "Khong phu long nguoi da hy sinh cho minh." A felt obligation to not waste another's sacrifice. A real floor; do not reduce it to "fear of guilt". [C2]
- **The dien, by region (NOT one thing).** [C1]
  - Northern: face as something shown and maintained in public; losing face before others is the harm.
  - Central (Hue): worth kept quiet, not displayed; the floor is composure and not-burdening-others, so distress is masked behind calm.
  - Southern: openness and generosity (phong khoang); the floor reads more as keeping warmth and not being stingy or cold.
  These are three different relational terminus. Picking the wrong regional reading misnames the floor.
- **Thuoc ve cong dong (collectivist belonging).** Belonging to family/village/group as a floor, where the individual-vs-group frame itself does not apply cleanly. [C2]
- **Collective continuity ("khong tro ve khong").** The clearest contrast case: hoarding gold, hoarding savings, over-preparing, bottoms out at "not letting the family start from zero again", a collective continuity across generations shaped by lived history of loss, not a personal autonomy or security need. [C2]

**Brute social fact terminus (Vietnamese address system).** The pronoun-and-address system (anh/em, chu/bac/co/di, ong/ba, con/chau) encodes relative age, status, and relationship. WHO may propose a shift in address (for example moving to more intimate or more equal terms) is a brute social fact, asymmetric: the senior party may propose it; the junior proposing it is marked and itself carries meaning. When a cascade hits "why did the address change", the floor can be this social rule, not an inner motive. [C5]

---

## 3. Speech-act repertoire (Vietnamese)

Acts that do not map onto a Western verb shape, which the engine's ACTION-shape cascade can misread.

- **Thoi ke / buong (letting-go, releasing).** "Thoi ke", "buong", "thoi vay" is an act of releasing or accepting, not a decision-to-act and not avoidance. Running the ACTION cascade ("you did X to achieve what?") onto a thoi-ke utterance forces a goal onto an act of release. Read it as STATE or as a relational/acceptance move, not as a plan. [C6]
- **Politeness-wrapped imperatives (face-work).** A request or even a command is routinely wrapped as a question, a hint, or an observation to protect the hearer's face (Brown-Levinson politeness). "Em xem lai giup anh cai nay nhe" is a directive, not a neutral question. The engine's literal/illocutionary scan must read the directive under the politeness wrapper, and must NOT treat the softening as the speaker's genuine uncertainty. [C7]
- **Noi giam, noi tranh (understatement / avoidance-of-direct-naming).** Hard things are named obliquely, especially in Central speech. Absence of a blunt statement is not absence of the content. [C1]

---

## 4. Parser signals (Vietnamese)

Language-specific signals the engine's parser should use when this pack is loaded.

- **Topic-comment / De-Thuyet (subject legitimately dropped).** Vietnamese foregrounds a topic and routinely omits the agent: "Cai ao nay giat roi" (this shirt, washed already) names no washer. This is normal grammar, NOT evasion or a hidden actor. Do NOT insert a subject the sentence did not state, and do NOT read motive into the missing agent. This is the Vietnamese instance of the engine's "subject is language-relative" rule. [C3]
- **Sentence-final modal particles (carry commitment and stance).** Particles such as nhe, nha, nhi, day, co, co ma, ma, thoi, di, a, u, chu, vay, sao shift the speaker's commitment, softness, or stance. "Co le vay nhe" is far less certain than "Dung vay". The cascade must carry this hedge into the terminus: a longing stated with a softening particle should NOT be written up as a hard, certain terminus. Dropping the particle over-certifies the floor. [C4]
- **Sarcasm carried by tone/prosody (text blind spot).** Vietnamese marks much sarcasm through intonation and tone-contour, sometimes only on the final-syllable pitch, which vanishes in writing. On written Vietnamese, the illocutionary scan has a systematic blind spot for tonal sarcasm; declare it rather than asserting you caught the real intent. (Partial offset: Vietnamese is a tonal language written with full tone diacritics in Quoc ngu, so written Vietnamese retains MORE lexical-tone information than a non-tone-marking script; but sentence-level prosodic sarcasm is still lost.) [C8][C9]
- **Dialect code-switch as a face/relational signal.** A speaker shifting from a Hue accent to a Northern one mid-conversation is usually NOT changing referent and NOT being sarcastic; the switch carries social meaning (status, distance, face). The engine's parser should read register/dialect code-switch as relational information, not as an illocutionary anomaly. [C10]

---

## 5. Clinical display norms (feeds the Clinical Brake)

The engine's clinical brake warns against using surface emotional intensity as a proxy for risk. This pack makes that concrete for Vietnamese:
- Central (Hue) norm: distress is masked behind composure; a very calm, understated message can carry real risk. Do not under-weight it. [C11]
- Southern norm: expressive, strong-affect speech can be ordinary venting rather than crisis. Do not over-weight surface intensity. [C11]
In both directions, judge risk by content and signal, not by how loud the affect is, and err toward gentle direct asking.

---

## 6. Worked examples

See examples.md in this folder for Vietnamese worked cases (topic-comment subject-drop, regional face terminus, modal-particle hedging, thoi-ke read).

---

## 7. Provenance and verification status (read honestly)

This pack is DERIVED from a multi-council critique of the engine (Vietnamese, Anglophone, and general-linguistics panels), harvested in the project notes. The councils' per-statement verification was only partly completed before a session limit, so this pack distinguishes what is sourced from what still needs checking.

- Entries marked with a citation [Cn] below rest on a statement the council verified as supported, with the listed sources. These are the load-bearing claims.
- Entries without a citation are linguistically standard but were not individually re-verified for this pack; treat as reference-grade, not proven, and strengthen before any strong public claim.
- This honesty is not a disclaimer ritual. The companion engine, what-for-and-how, exists to refuse meaningless action; its sibling discipline is to refuse unverified assertion. A culture-pack that overclaimed its grounding would violate the very method it ships.

### Citations

- [C1] Vietnamese regional phonology and dialect difference (Northern/Central/Southern not homogeneous; Hue tone-merging): https://en.wikipedia.org/wiki/Vietnamese_phonology ; https://www.sil.org/resources/archives/3599 ; https://nguyentienhai.blogspot.com/2011/04/cac-ac-iem-ngu-am-cua-tieng-hue.html ; https://vietcetera.com/en/from-north-centre-to-south-exploring-vietnams-linguistic-diversity
- [C2] Filial duty, relational obligation, collectivist belonging as terminus (ethnopragmatics / cultural semantics): https://csdlkhoahoc.hueuni.edu.vn/data/2020/10/Studies_in_Ethnopragmatics,_Cultural_Semantics,_and_Intercultural_Communication_Ethnopragmatics_and_Semantic_Analysis-123-138.pdf
- [C3] Topic-comment structure and subject drop in Vietnamese: https://en.wikipedia.org/wiki/Vietnamese_grammar ; https://en.wikipedia.org/wiki/Topic-prominent_language
- [C4] Sentence-final / modal particles in Vietnamese: https://en.wikipedia.org/wiki/Vietnamese_grammar#Particles
- [C5] Vietnamese pronoun and address system (kinship terms, asymmetric address): https://en.wikipedia.org/wiki/Vietnamese_pronouns
- [C6] Politeness, face, and indirectness (Brown and Levinson, applied): https://en.wikipedia.org/wiki/Politeness_theory
- [C7] Politeness-wrapped directives as face-threatening-act mitigation (Brown and Levinson): https://en.wikipedia.org/wiki/Politeness_theory
- [C8] Sarcasm marked by prosody, lost in text: https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/does-prosody-mark-sarcasm-early-in-an-utterance-a-production-and-perception-study-including-listeners-who-selfidentified-as-being-on-the-autism-spectrum/95396E5672613EED98781EA24C3DAA58 ; https://talkpal.ai/vocabulary/sarcastic-phrases-in-vietnamese-language/
- [C9] Quoc ngu records full lexical tone (partial offset): https://en.wikipedia.org/wiki/Vietnamese_alphabet ; https://en.wikipedia.org/wiki/Tone_(linguistics)
- [C10] Dialect/style code-switch carries social meaning (Markedness Model, style-shifting): https://en.wikipedia.org/wiki/Code-switching ; https://www.academia.edu/102632194/Style_shifting_and_code_switching_are_two_related_but_different_sociolinguistic_phenomena
- [C11] Cultural display rules for emotion (Ekman/Friesen display rules; Matsumoto): https://www.pnas.org/doi/abs/10.1073/pnas.1200155109 ; http://davidmatsumoto.com/content/Matsumoto%202008%20HK%20Conference.pdf

---

## 8. How to read this pack with the engine

1. Run the engine's tier-0 router and parser as usual.
2. When the input is Vietnamese or the subject is in a Vietnamese cultural context, load this pack.
3. In the parser, add the signals in section 4 (topic-comment subject-drop, modal particles, tonal-sarcasm blind spot, dialect code-switch).
4. In the speech-act read, use section 3 (thoi-ke, politeness-wrapped imperatives, understatement).
5. At the terminus, the candidate floors include section 2's Vietnamese terminus on top of the engine defaults. Pick the one the evidence supports, and pick the right REGIONAL reading of face.
6. The clinical brake uses section 5's display norms.
7. Everything else (mode switch, two guards, L6-falsify, the how-bridge) is the engine, unchanged.
