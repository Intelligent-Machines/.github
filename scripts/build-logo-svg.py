# scripts/build-logo-svg.py
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PNG_PATH = ROOT / "assets" / "logo-original.png"
OUT_PATH = ROOT / "assets" / "logo-animated.svg"

b64 = base64.b64encode(PNG_PATH.read_bytes()).decode("ascii")

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" role="img" aria-label="Intelligent Machines logo">
  <title>Intelligent Machines</title>
  <style>
    @media (prefers-reduced-motion: reduce) {{
      .bot-parts {{ display: none; }}
      .logo-img {{ opacity: 1 !important; }}
    }}
  </style>
  <defs>
    <clipPath id="frameClip"><rect x="0" y="0" width="120" height="120" rx="26"/></clipPath>
    <radialGradient id="flashGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
      <stop offset="45%" stop-color="#1264ff" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#1264ff" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <g clip-path="url(#frameClip)">
    <rect x="0" y="0" width="120" height="120" fill="#f1f2f4"/>

    <g class="bot-parts">
      <g>
        <rect x="59" y="26" width="2" height="15" rx="1" fill="#10131a"/>
        <circle cx="60" cy="20" r="3" fill="#1264ff"/>
        <animateTransform attributeName="transform" type="rotate"
          values="0 60 41;-10 60 41;8 60 41;0 60 41;0 60 41"
          keyTimes="0;0.06;0.11;0.18;1"
          dur="7s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.22;0.30;1"
          dur="7s" repeatCount="indefinite"/>
      </g>

      <polygon fill="#10131a"
        points="54.5,49 58.04,50.46 59.5,54 58.04,57.54 54.5,59 50.96,57.54 49.5,54 50.96,50.46">
        <animate attributeName="points" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.13;0.15;0.22;0.30;0.34;1"
          values="
            54.5,49 58.04,50.46 59.5,54 58.04,57.54 54.5,59 50.96,57.54 49.5,54 50.96,50.46;
            54.5,53.4 58.04,53.58 59.5,54 58.04,54.42 54.5,54.6 50.96,54.42 49.5,54 50.96,53.58;
            54.5,49 58.04,50.46 59.5,54 58.04,57.54 54.5,59 50.96,57.54 49.5,54 50.96,50.46;
            54.5,49 58.04,50.46 59.5,54 58.04,57.54 54.5,59 50.96,57.54 49.5,54 50.96,50.46;
            52.6,42 63,77 63,77 63,77 54.5,77 46,77 46,77 46,77;
            52.6,42 63,77 63,77 63,77 54.5,77 46,77 46,77 46,77;
            52.6,42 63,77 63,77 63,77 54.5,77 46,77 46,77 46,77"/>
        <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.30;0.34;1"
          dur="7s" repeatCount="indefinite"/>
      </polygon>

      <polygon fill="#10131a"
        points="72.5,49 76.04,50.46 77.5,54 76.04,57.54 72.5,59 68.96,57.54 67.5,54 68.96,50.46">
        <animate attributeName="points" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.13;0.15;0.22;0.30;0.34;1"
          values="
            72.5,49 76.04,50.46 77.5,54 76.04,57.54 72.5,59 68.96,57.54 67.5,54 68.96,50.46;
            72.5,53.4 76.04,53.58 77.5,54 76.04,54.42 72.5,54.6 68.96,54.42 67.5,54 68.96,53.58;
            72.5,49 76.04,50.46 77.5,54 76.04,57.54 72.5,59 68.96,57.54 67.5,54 68.96,50.46;
            72.5,49 76.04,50.46 77.5,54 76.04,57.54 72.5,59 68.96,57.54 67.5,54 68.96,50.46;
            75,42 82,77 82,77 82,77 72.5,77 63,77 63,77 63,77;
            75,42 82,77 82,77 82,77 72.5,77 63,77 63,77 63,77;
            75,42 82,77 82,77 82,77 72.5,77 63,77 63,77 63,77"/>
        <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.30;0.34;1"
          dur="7s" repeatCount="indefinite"/>
      </polygon>

      <rect fill="#10131a" x="34.5" y="46.5" width="14" height="26" rx="7">
        <animate attributeName="x" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.22;0.30;0.34;1" values="34.5;34.5;39.5;39;39"/>
        <animate attributeName="y" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.22;0.30;0.34;1" values="46.5;46.5;40.5;42;42"/>
        <animate attributeName="width" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.22;0.30;0.34;1" values="14;14;4;5;5"/>
        <animate attributeName="height" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.22;0.30;0.34;1" values="26;26;38;35;35"/>
        <animate attributeName="rx" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.22;0.30;0.34;1" values="7;7;2;2;2"/>
        <animate attributeName="opacity" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.30;0.34;1" values="1;1;0;0"/>
      </rect>

      <circle cx="60" cy="59.5" r="2" fill="url(#flashGrad)">
        <animate attributeName="r" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.29;0.33;0.37;1" values="2;2;22;2;2"/>
        <animate attributeName="opacity" dur="7s" repeatCount="indefinite"
          keyTimes="0;0.29;0.33;0.37;1" values="0;0;0.9;0;0"/>
      </circle>
    </g>

    <image class="logo-img" x="23" y="23" width="74" height="74"
      href="data:image/png;base64,{b64}">
      <animate attributeName="opacity" dur="7s" repeatCount="indefinite"
        keyTimes="0;0.30;0.34;1" values="0;0;1;1"/>
    </image>
  </g>
</svg>
"""

OUT_PATH.write_text(SVG_TEMPLATE.format(b64=b64))
print(f"wrote {OUT_PATH} ({OUT_PATH.stat().st_size} bytes)")
