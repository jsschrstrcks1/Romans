#!/bin/bash
# Downloads all Spurgeon sermon PDFs from SpurgeonGems.org
# Run from this directory. Safe to re-run — skips already-downloaded files.

BASE="https://www.spurgeongems.org/sermon"
ROOT="https://www.spurgeongems.org"
SERMONS_DIR="./sermons"
INDEX_DIR="./sermons/indexes"

# Index and reference files (these live at the site root, not /sermon/)
echo "==> Downloading indexes and references..."
for f in chstix sindex_ot sindex_nt; do
  dest="$INDEX_DIR/${f}.pdf"
  if [ ! -f "$dest" ] || [ ! -s "$dest" ]; then
    wget -q --wait=1 -O "$dest" "${ROOT}/${f}.pdf"
    if [ $? -eq 0 ] && [ -s "$dest" ]; then
      echo "  OK: ${f}.pdf"
    else
      rm -f "$dest"
      echo "  MISS: ${f}.pdf"
    fi
  else
    echo "  SKIP (exists): ${f}.pdf"
  fi
done

# Volume prefaces
echo "==> Downloading volume prefaces..."
for i in $(seq 1 64); do
  f="chsp${i}"
  dest="$INDEX_DIR/${f}.pdf"
  if [ ! -f "$dest" ] || [ ! -s "$dest" ]; then
    wget -q --wait=0.5 -O "$dest" "${BASE}/${f}.pdf"
    if [ $? -eq 0 ] && [ -s "$dest" ]; then
      echo "  OK: ${f}.pdf"
    else
      rm -f "$dest"
    fi
  fi
done

# Special combined and variant sermon files known from the index
SPECIAL=(
  "chs7-8" "chs39-40" "chs41-42" "chs61-62" "chs66-67"
  "chs81-82" "chs141-142" "chs154-155" "chs268-270"
  "chs297-298" "chs331-332" "chs389-390"
  "chs388a" "chs388b" "chs364A" "chs369A"
)

echo "==> Downloading special/combined sermon files..."
for f in "${SPECIAL[@]}"; do
  dest="$SERMONS_DIR/${f}.pdf"
  if [ ! -f "$dest" ]; then
    wget -q --wait=1 -O "$dest" "${BASE}/${f}.pdf"
    if [ $? -eq 0 ] && [ -s "$dest" ]; then
      echo "  OK: ${f}.pdf"
    else
      rm -f "$dest"
    fi
  else
    echo "  SKIP (exists): ${f}.pdf"
  fi
done

# Individual sermons 1–3563
echo "==> Downloading individual sermons (1–3563)..."
count=0
miss=0
for i in $(seq 1 3563); do
  f="chs${i}"
  dest="$SERMONS_DIR/${f}.pdf"
  if [ ! -f "$dest" ]; then
    wget -q --wait=0.3 -O "$dest" "${BASE}/${f}.pdf"
    if [ $? -eq 0 ] && [ -s "$dest" ]; then
      count=$((count+1))
      [ $((count % 100)) -eq 0 ] && echo "  ...downloaded $count so far (at sermon $i)"
    else
      rm -f "$dest"
      miss=$((miss+1))
    fi
  fi
done

echo ""
echo "==> Done."
echo "    Downloaded: $count new sermon PDFs"
echo "    Not found:  $miss"
echo "    Location:   $SERMONS_DIR"
