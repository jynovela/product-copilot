#!/usr/bin/env python3
"""Flag machine-sounding patterns in text written for people.

Usage:
    python3 skills/humanize-check/check.py FILE [FILE ...] [--mode full|light]

Modes:
    full   (default) prose documents: every check.
    light  text another AI or a builder reads (demo specs, tickets): only
           word- and phrase-level checks; rhythm and structure are skipped.

Each finding is printed on its own line:
    <file>:<line>: <check>: "<excerpt>"
The last line is always:
    RESULT: <n> findings
Exit code is 1 if there are findings, else 0.

Findings are candidates, not verdicts. Fix each one with the smallest change
that removes it, or say in your report why it stays (for example, a quote
from a source). Never change a fact to clear a finding.

Skipped: frontmatter, fenced code, inline code, block quotes and table rows
(phrase checks still run on table rows).
Standard library only. Works on Python 3.9+.
"""

import re
import sys

# ---- word and phrase lists -------------------------------------------------

AI_WORDS = [
    "delve", "delves", "delving", "tapestry", "testament", "beacon", "realm",
    "landscape", "foster", "fosters", "fostering", "leverage", "leverages",
    "leveraging", "utilize", "utilizes", "utilizing", "utilization", "unlock",
    "unlocks", "unlocking", "empower", "empowers", "empowering", "elevate",
    "elevates", "elevating", "harness", "harnessing", "robust", "seamless",
    "seamlessly", "holistic", "comprehensive", "pivotal", "crucial", "vital",
    "intricate", "multifaceted", "nuanced", "dynamic", "vibrant", "nestled",
    "boasts", "showcase", "showcases", "showcasing", "underscore",
    "underscores", "underscoring", "resonate", "resonates", "game-changer",
    "game-changing", "cutting-edge", "transformative", "meticulous",
    "meticulously", "invaluable", "quietly", "grounded", "navigate",
    "navigating", "journey",
]

PUFFERY = [
    "stands as a", "plays a vital role", "plays a crucial role",
    "plays a key role", "serves as a reminder", "marks a pivotal moment",
    "leaves a lasting legacy", "in today's fast-paced world",
    "in the ever-evolving landscape", "as the world continues to evolve",
    "it's no secret that", "at the end of the day",
]

CONTRAST_PHRASES = [
    "not just", "not only", "here's why that matters", "here's why it matters",
    "the result?", "and honestly?", "then i realized", "that's the real",
    "let that sink in", "here's the kicker",
]

SETUP_COLONS = [
    "the result:", "here's the thing:", "the catch:", "the kicker:",
    "bottom line:", "the upshot:", "the takeaway:", "the short version:",
    "the truth:", "the twist:", "the problem:", "the answer:",
]

VAGUE_AUTHORITY = [
    "experts say", "experts agree", "studies show", "research shows",
    "many believe", "it is widely regarded", "it's widely regarded",
    "some would argue", "it is often said",
]

GLUE_OPENERS = [
    "moreover", "furthermore", "additionally", "in addition", "that said",
    "ultimately", "overall", "in conclusion", "in summary", "to summarize",
    "notably", "importantly", "interestingly",
]

FILLER = [
    "it's important to note", "it is important to note", "it's worth noting",
    "it is worth noting", "it's worth mentioning", "when it comes to",
    "in order to", "the fact that", "needless to say", "as a matter of fact",
    "at this point in time", "for all intents and purposes",
]

HEDGE_STACKS = [
    "may potentially", "could potentially", "might potentially",
    "could possibly", "might possibly", "may possibly", "perhaps maybe",
    "somewhat arguably",
]

BALANCED = [
    "both sides have merit", "despite its challenges",
    "has its pros and cons", "there are pros and cons",
    "it also offers opportunities",
]

RESIDUE = [
    "i hope this helps", "great question", "certainly!", "let's dive in",
    "let's dive into", "as an ai", "i'd be happy to", "feel free to reach out",
    "let me know if you", "in this article", "in this document, we",
]

DRESSED_METAPHOR = [
    "wearing the costume of", "in disguise", "dressed up as", "dressed as",
    "masquerading as", "in sheep's clothing", "wearing the mask of",
]

STRAW_MAN = [
    "is the obvious reading", "is the obvious answer", "and it is wrong",
    "and it's wrong", "you might think", "you'd be forgiven for thinking",
    "conventional wisdom says",
]

APHORISM = [
    re.compile(r"\bthe kind of \w+ that\b", re.I),
    re.compile(r"\b(looks|sounds|feels|reads) like [^.]{2,60}\band (is not|isn't)\b", re.I),
]

# ---- regexes ---------------------------------------------------------------

EM_DASH = re.compile(r"—|\s--\s|\s–\s")
SEMICOLON = re.compile(r";\s")
NEG_REVEAL = re.compile(
    r"\b(it|this|that)( is|'s|’s) not\b[^.!?]*[.!?]\s+(it|this|that)( is|'s|’s)\b",
    re.I)
ISNT_ABOUT = re.compile(r"\bisn't about\b[^.]*\bit's about\b", re.I)
NO_NO_JUST = re.compile(r"\bNo \w+[^.]*\.\s+No \w+[^.]*\.\s+Just\b")
SIGNIFICANCE = re.compile(
    r"\b(is|was) the (one |only |real |key )?\w+ that (actually |really |truly )?"
    r"(answers|matters|counts|explains|decides|settles)\b", re.I)
ABSTRACT_AGENT = re.compile(
    r"\b(the )?(table|chart|graph|data|median|average|mean|number|numbers|"
    r"metric|metrics|result|results|evidence|spreadsheet|dashboard)\s+"
    r"(shows|hides|tells|reveals|says|knows|wants|argues|insists)\b", re.I)
DEFERRED = re.compile(
    r"(?:^|[.!?]\s+)((?:The|This|That|One|Another)\b[^.!?]{0,30}\b"
    r"(?:is not|isn't|does not|doesn't|was not|wasn't))\.")
LABEL_FIRST = re.compile(
    r"^(The|This|That) [^.!?]{0,40}\bof (this|the|that) [^.!?]{0,30}\.$")
COY_HEADER = re.compile(r"^#{1,6}\s+(What|Why|Where|The one|The real|The only|"
                        r"The thing|The gap|Enter|Meet)\b", re.I)
QUOTE_HEADER = re.compile(r"^#{1,6}\s+.*[\"“].+[\"”]")
TAILS = re.compile(r",\s+(highlighting|reflecting|ensuring|contributing to|"
                   r"underscoring|showcasing|emphasizing|demonstrating|"
                   r"signaling|cementing|paving the way)\b", re.I)
EMOJI_BULLET = re.compile(r"^\s*([-*]\s*)?[☀-➿\U0001F300-\U0001FAFF]")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"“(])")
WORD = re.compile(r"[A-Za-z0-9'’%$-]+")
SMALL_WORDS = {"a", "an", "the", "and", "or", "but", "of", "in", "on", "at",
               "to", "for", "with", "by", "vs", "from", "as", "is", "it"}


def phrase_re(phrases):
    parts = [re.escape(p) for p in phrases]
    return re.compile(r"(?<![\w'])(" + "|".join(parts) + r")(?![\w'])", re.I)


AI_RE = phrase_re(AI_WORDS)
PUFFERY_RE = phrase_re(PUFFERY)
CONTRAST_RE = re.compile(r"(?<![\w'])(" + "|".join(
    re.escape(p) for p in CONTRAST_PHRASES) + r")", re.I)
SETUP_RE = re.compile(r"(?:^|[.!?]\s+|^\s*[-*]\s+)(" + "|".join(
    re.escape(p) for p in SETUP_COLONS) + r")", re.I)
AUTH_RE = phrase_re(VAGUE_AUTHORITY)
GLUE_RE = re.compile(r"(?:^|[.!?]\s+)(" + "|".join(
    re.escape(p) for p in GLUE_OPENERS) + r"),", re.I)
FILLER_RE = phrase_re(FILLER)
HEDGE_RE = phrase_re(HEDGE_STACKS)
BALANCED_RE = phrase_re(BALANCED)
RESIDUE_RE = re.compile(r"(?<![\w'])(" + "|".join(
    re.escape(p) for p in RESIDUE) + r")", re.I)
METAPHOR_RE = phrase_re(DRESSED_METAPHOR)
STRAW_RE = phrase_re(STRAW_MAN)


# ---- text handling ---------------------------------------------------------

def prose_lines(text):
    """Yield (line_number, line, kind) for lines worth checking.

    kind is "prose", "heading" or "table". Frontmatter, fenced code and
    block quotes are skipped; inline code is blanked out.
    """
    lines = text.split("\n")
    i = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                i = j + 1
                break
    fenced = False
    for n in range(i, len(lines)):
        line = lines[n]
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if fenced or line.lstrip().startswith(">"):
            continue
        line = re.sub(r"`[^`\n]*`", "", line)
        line = re.sub(r"\[\[[^\]]*\]\]", "", line)
        if line.lstrip().startswith("#"):
            kind = "heading"
        elif line.lstrip().startswith("|"):
            kind = "table"
        else:
            kind = "prose"
        yield n + 1, line, kind


def paragraphs(items):
    """Group consecutive prose lines into (first_line, text) paragraphs."""
    block, start = [], None
    for n, line, kind in items:
        is_item = re.match(r"^\s*([-*+]|\d+\.)\s", line)
        if kind != "prose" or not line.strip() or is_item:
            if block:
                yield start, " ".join(block)
            block, start = [], None
            if is_item and kind == "prose":
                yield n, re.sub(r"^\s*([-*+]|\d+\.)\s+", "", line)
            continue
        if start is None:
            start = n
        block.append(line.strip())
    if block:
        yield start, " ".join(block)


def words(sentence):
    return WORD.findall(sentence)


def is_title_case(heading):
    text = re.sub(r"^#+\s*", "", heading).strip()
    ws = [w for w in words(text) if w.lower() not in SMALL_WORDS]
    return len(ws) >= 3 and all(w[0].isupper() for w in ws if w[0].isalpha())


def rule_of_three(sentence):
    m = re.search(r"\b(\w+), (\w+),? and (\w+)\b", sentence)
    if not m:
        return None
    abstract = re.compile(r"(ness|tion|sion|ity|cy|ive|ful|ous|ence|ance|ment|ism|ic|al)$")
    if all(abstract.search(w.lower()) for w in m.groups()):
        return m.group(0)
    return None


# ---- checks ----------------------------------------------------------------

def check_file(path, mode):
    findings = []

    def add(line, check, excerpt):
        excerpt = excerpt.strip()
        if len(excerpt) > 80:
            excerpt = excerpt[:77] + "..."
        findings.append((line, check, excerpt))

    with open(path, encoding="utf-8") as f:
        text = f.read()
    items = list(prose_lines(text))

    for n, line, kind in items:
        if not line.strip():
            continue
        phrase_checks = [
            (AI_RE, "ai-word"), (PUFFERY_RE, "puffery"),
            (AUTH_RE, "vague-authority"), (FILLER_RE, "filler"),
            (HEDGE_RE, "stacked-hedge"), (BALANCED_RE, "false-balance"),
            (RESIDUE_RE, "chatbot-residue"), (METAPHOR_RE, "dressed-metaphor"),
            (STRAW_RE, "straw-man"), (CONTRAST_RE, "contrast-formula"),
        ]
        for regex, name in phrase_checks:
            for m in regex.finditer(line):
                add(n, name, m.group(0))
        for m in EM_DASH.finditer(line):
            add(n, "dash", line[max(0, m.start() - 25):m.end() + 25])
        for m in TAILS.finditer(line):
            add(n, "empty-ing-tail", line[m.start():m.end() + 30])
        if EMOJI_BULLET.search(line):
            add(n, "emoji", line)
        if kind == "heading":
            if COY_HEADER.search(line) or QUOTE_HEADER.search(line):
                add(n, "coy-header", line)
            if mode == "full" and is_title_case(line):
                add(n, "title-case-heading", line)
            continue
        if kind == "table":
            continue
        for m in SETUP_RE.finditer(line):
            add(n, "setup-colon", m.group(1))
        for m in GLUE_RE.finditer(line):
            add(n, "glue-transition", m.group(1))
        if mode == "full":
            for m in SEMICOLON.finditer(line):
                add(n, "semicolon", line[max(0, m.start() - 25):m.end() + 25])
            for m in ABSTRACT_AGENT.finditer(line):
                add(n, "abstraction-agency", m.group(0))
            for m in SIGNIFICANCE.finditer(line):
                add(n, "significance-designation", m.group(0))

    for start, para in paragraphs(items):
        sentences = [s.strip() for s in SENT_SPLIT.split(para) if s.strip()]
        for regex, name in [(NEG_REVEAL, "negation-first-reveal"),
                            (ISNT_ABOUT, "negation-first-reveal"),
                            (NO_NO_JUST, "negation-first-reveal")]:
            for m in regex.finditer(para):
                add(start, name, m.group(0))
        for regex in APHORISM:
            for m in regex.finditer(para):
                add(start, "aphoristic-line", m.group(0))
        if mode != "full":
            continue
        for m in DEFERRED.finditer(para):
            add(start, "deferred-noun", m.group(1))
        for s in sentences:
            if LABEL_FIRST.match(s) and not re.search(
                    r"\b(is|are|was|were|has|have|had|do|does|did|can|will|"
                    r"shows?|holds?|lists?)\b", s):
                add(start, "label-first", s)
            three = rule_of_three(s)
            if three:
                add(start, "rule-of-three", three)
        lengths = [len(words(s)) for s in sentences]
        run = 0
        for k, length in enumerate(lengths):
            run = run + 1 if length <= 4 else 0
            if run == 3:
                add(start, "fragment-cadence",
                    " ".join(sentences[k - 2:k + 1]))
        for k in range(len(lengths) - 2):
            trio = lengths[k:k + 3]
            if min(trio) >= 8 and max(trio) - min(trio) <= 3:
                add(start, "flat-rhythm",
                    "{} sentences of {} words".format(3, "/".join(map(str, trio))))
                break
    findings.sort()
    return findings


def main(argv):
    mode = "full"
    files = []
    k = 0
    while k < len(argv):
        if argv[k] == "--mode" and k + 1 < len(argv):
            mode = argv[k + 1]
            k += 2
            continue
        files.append(argv[k])
        k += 1
    if not files or mode not in ("full", "light"):
        print(__doc__)
        return 2
    total = 0
    for path in files:
        for line, check, excerpt in check_file(path, mode):
            print('{}:{}: {}: "{}"'.format(path, line, check, excerpt))
            total += 1
    print("RESULT: {} findings".format(total))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
