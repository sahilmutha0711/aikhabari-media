#!/usr/bin/env bash
# run inside the Composio remote sandbox: sets up the carousel renderer in $1 (default /tmp/car)
D=${1:-/tmp/car}; mkdir -p $D/fonts; cd $D
R=https://raw.githubusercontent.com/sahilmutha0711/aikhabari-media/main/tools/carousel
for f in car.py car.css; do curl -sSL -o $f $R/$f; done
[ -s fonts/Bricolage.ttf ] || curl -sSL -o fonts/Bricolage.ttf "https://github.com/google/fonts/raw/main/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz,wdth,wght%5D.ttf"
[ -s fonts/DMSans.ttf ] || curl -sSL -o fonts/DMSans.ttf "https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans%5Bopsz,wght%5D.ttf"
python3 -c "import playwright,cv2" 2>/dev/null || (pip install -q playwright "opencv-python==4.11.0.86" && python3 -m playwright install chromium)
python3 -c "import cv2;assert hasattr(cv2,'CascadeClassifier')" || pip install -q --force-reinstall --no-deps "opencv-python==4.11.0.86"
echo ready $D
