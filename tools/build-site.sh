#!/usr/bin/env bash
# Builds the folder Cloudflare Pages serves for esska-focus-meetings.org:
#
#   dist/            the hub page listing the 2027 focus meetings
#   dist/arthroplasty-2027/  the Rome meeting site, named after its subject and year
#
# Each meeting keeps its own Pages project as well (esska-rome-2027 and the rest),
# which stay noindex for review. Only what is copied here is public and indexed, so
# add a line to SITES when a meeting is ready to go live on the domain.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"

# path on the domain : folder under sites/
SITES=(
  "arthroplasty-2027:rome-2027"
)

# old paths kept working, so links already shared do not break
REDIRECTS=(
  "/rome/* /arthroplasty-2027/:splat 301"
  "/arthroplasty/* /arthroplasty-2027/:splat 301"
)

rm -rf "$DIST"
mkdir -p "$DIST"

# the hub page sits at the root of the domain
cp -R "$ROOT/sites/focus-meetings/." "$DIST/"

for entry in "${SITES[@]}"; do
  path="${entry%%:*}"; folder="${entry##*:}"
  [ -d "$ROOT/sites/$folder" ] || { echo "missing sites/$folder"; exit 1; }
  mkdir -p "$DIST/$path"
  cp -R "$ROOT/sites/$folder/." "$DIST/$path/"
  echo "  /$path  <-  sites/$folder"
done

# per-project deploy files and junk have no place in the combined output
find "$DIST" \( -name '_headers' -o -name '_redirects' -o -name 'netlify.toml' \
  -o -name 'wrangler.jsonc' -o -name '.DS_Store' \) -delete

# one headers file for the whole domain: long cache for images, always revalidate
# CSS and JS (they carry a ?v= query), and no noindex, because this domain is public
{
  echo "/assets/img/*"
  echo "  Cache-Control: public, max-age=31536000, immutable"
  echo "/assets/css/*"
  echo "  Cache-Control: public, max-age=0, must-revalidate"
  echo "/assets/js/*"
  echo "  Cache-Control: public, max-age=0, must-revalidate"
  for entry in "${SITES[@]}"; do
    path="${entry%%:*}"
    echo "/$path/assets/img/*"
    echo "  Cache-Control: public, max-age=31536000, immutable"
    echo "/$path/assets/css/*"
    echo "  Cache-Control: public, max-age=0, must-revalidate"
    echo "/$path/assets/js/*"
    echo "  Cache-Control: public, max-age=0, must-revalidate"
  done
  echo "/*"
  echo "  X-Content-Type-Options: nosniff"
  echo "  Referrer-Policy: strict-origin-when-cross-origin"
} > "$DIST/_headers"

{
  echo "User-agent: *"
  echo "Allow: /"
  echo "Sitemap: https://esska-focus-meetings.org/sitemap.xml"
} > "$DIST/robots.txt"

if [ ${#REDIRECTS[@]} -gt 0 ]; then
  printf '%s\n' "${REDIRECTS[@]}" > "$DIST/_redirects"
fi

{
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
  echo '  <url><loc>https://esska-focus-meetings.org/</loc></url>'
  for entry in "${SITES[@]}"; do
    path="${entry%%:*}"
    echo "  <url><loc>https://esska-focus-meetings.org/$path/</loc></url>"
  done
  echo '</urlset>'
} > "$DIST/sitemap.xml"

echo "built $DIST"
