"""Compare the July 2026 Senate HSGAC Slack release with the two July 2023 collections.

Usage:
  python3 compare.py SENATE_PM_TXT PUBLIC_OCR_DIR HOUSE_REPORT_TXT [SENATE_AM_TXT]

Inputs are text extracted locally (not stored in this repository):
  pdftotext -layout slack-drop-pm.pdf slack-drop-pm.txt
  pdftotext -layout Final-Report-7.pdf Final-Report-7.txt
  pdftoppm -r 200 -gray -png public-proximal-origin-slack.pdf ocr/p
  for f in ocr/*.png; do tesseract "$f" "$f.out" --psm 4 -l eng; done
See sources/collections.csv for file URLs, sizes and SHA-256 hashes.

Method: parse Senate messages (timestamp, author, text); for each message with
at least three five-word sequences, compute the share of its five-word sequences
found in each 2023 collection. A share of 0.5 or more is a candidate match.
Candidates must then be inspected by hand. Prints CSV of candidates to stdout.
"""
import csv, glob, json, re, sys, collections

def parse_senate(path):
    msgs, bates, cur = [], None, None
    for line in open(path, errors="replace").read().splitlines():
        m = re.search(r"Released by Chairman Rand Paul\s+(SLACK_\d+)", line)
        if m:
            bates = m.group(1); continue
        m = re.match(r"\s*\[(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)\]\s*$", line)
        if m:
            cur = {"ts": m.group(1), "author": None, "text": "", "bates": bates}
            msgs.append(cur); continue
        m = re.match(r"\s*\[([^\]]+)\]\s*$", line)
        if m and cur is not None and cur["author"] is None:
            cur["author"] = m.group(1); continue
        if cur is not None:
            cur["text"] += line.strip() + " "
    return msgs

def words(s): return re.sub(r"[^a-z0-9 ]+", " ", s.lower()).split()
def shingles(w, k=5): return {" ".join(w[i:i + k]) for i in range(len(w) - k + 1)}

def main():
    pm, ocr_dir, house = sys.argv[1:4]
    msgs = parse_senate(pm)
    pub = shingles(words(" ".join(open(f).read() for f in sorted(glob.glob(ocr_dir + "/*.txt")))))
    hou = shingles(words(open(house, errors="replace").read()))
    stats = collections.Counter()
    out = csv.writer(sys.stdout)
    out.writerow(["timestamp", "author", "bates", "shingles", "share_public_2023", "share_house_2023", "text_start"])
    for m in msgs:
        s = shingles(words(m["text"]))
        if len(s) < 3:
            stats["too_short"] += 1; continue
        stats["checked"] += 1
        fp, fh = len(s & pub) / len(s), len(s & hou) / len(s)
        if fp >= 0.5 or fh >= 0.5:
            stats["candidates"] += 1
            out.writerow([m["ts"], m["author"], m["bates"], len(s), round(fp, 2), round(fh, 2), m["text"][:80]])
    ts = sorted(m["ts"] for m in msgs)
    print(json.dumps({"messages": len(msgs), "first": ts[0], "last": ts[-1], **stats,
                      "authors": collections.Counter(m["author"] for m in msgs).most_common()}), file=sys.stderr)
    if len(sys.argv) > 4:
        am = parse_senate(sys.argv[4]); keys = {(m["ts"], m["author"]) for m in msgs}
        print(json.dumps({"am_messages": len(am), "am_in_pm": sum((m["ts"], m["author"]) in keys for m in am)}), file=sys.stderr)

if __name__ == "__main__":
    main()
