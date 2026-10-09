#!/usr/bin/env bash
# Extrae de la presentación de la sesión 08 las bandas CINFO, las diapositivas fijas
# (¿Cómo te sientes hoy?, ¿Qué es CINFO?, 03 a 06) y las fotos de portada de bloque.
# uso: bash extraer_media.sh [ruta-del-repositorio]
set -euo pipefail
REPO="${1:-$(cd "$(dirname "$0")/../../.." && pwd)}"
AQUI="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
unzip -q -o "$REPO/SESION 08/Sesion08-Introduccion-a-CSS3.pptx" 'ppt/media/*' -d "$TMP"
M="$TMP/ppt/media"; D="$AQUI/media"; mkdir -p "$D"
cp "$M/image-1002-1.png" "$D/band-portada.png"
cp "$M/image-1004-1.jpg" "$D/band-conceptual.jpg"
cp "$M/image-1006-1.jpg" "$D/band-instrumental.jpg"
cp "$M/image-1008-1.jpg" "$D/band-nivelador.jpg"
cp "$M/image-1010-1.jpg" "$D/band-funcional.jpg"
cp "$M/image-1012-1.jpg" "$D/band-orientador.jpg"
cp "$M/image-1-1.png"    "$D/espera.png"
cp "$M/image-3-1.jpg"    "$D/como-te-sientes.jpg"
cp "$M/image-4-1.jpg"    "$D/que-es-cinfo.jpg"
cp "$M/image-5-1.jpg"    "$D/conocimientos-previos.jpg"
cp "$M/image-31-1.jpg"   "$D/cinfo-03-instrumental.jpg"
cp "$M/image-41-1.jpg"   "$D/cinfo-04-nivelador.jpg"
cp "$M/image-44-1.jpg"   "$D/cinfo-05-funcional.jpg"
cp "$M/image-46-1.jpg"   "$D/cinfo-06-orientador.jpg"
cp "$M/image-9-1.jpg"    "$D/foto-bloque-a.jpg"
cp "$M/image-14-1.jpg"   "$D/foto-bloque-b.jpg"
rm -rf "$TMP"
echo "Listo: $(ls "$D" | wc -l) imágenes en $D"
