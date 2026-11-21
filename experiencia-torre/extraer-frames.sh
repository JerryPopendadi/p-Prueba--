#!/usr/bin/env bash
# Convierte tu vídeo final en una secuencia de imágenes para el scroll.
# Uso:  ./extraer-frames.sh recorrido.mp4 [fps] [ancho]
#   fps   -> imágenes por segundo de vídeo (12 por defecto; 20 s x 12 = 240 frames)
#   ancho -> 1920 por defecto (usa 1280 si quieres que cargue más rápido)
set -euo pipefail
VIDEO="${1:?Indica el vídeo: ./extraer-frames.sh recorrido.mp4}"
FPS="${2:-12}"
WIDTH="${3:-1920}"
OUT="$(dirname "$0")/frames"
mkdir -p "$OUT"
rm -f "$OUT"/frame_*.webp
ffmpeg -hide_banner -loglevel error -i "$VIDEO" \
  -vf "fps=${FPS},scale=${WIDTH}:-2:flags=lanczos" \
  -c:v libwebp -quality 78 -compression_level 6 \
  "$OUT/frame_%04d.webp"
COUNT=$(ls "$OUT"/frame_*.webp | wc -l | tr -d ' ')
echo "✓ ${COUNT} frames en ${OUT}"
echo "  Abre index.html?frames=${COUNT}  (o pon count: ${COUNT} en CONFIG)"
