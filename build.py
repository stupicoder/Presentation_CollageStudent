#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reveal.js 프레젠테이션 빌드 스크립트
slides/ 디렉토리의 HTML 파일들을 읽어서 index.html을 생성합니다.
"""

import sys
import os
import re
from pathlib import Path

# Windows 환경에서 UTF-8 출력 설정
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None

def extract_body_content(html_content):
    """HTML 파일에서 body 내용만 추출"""
    # <body>...</body> 태그 안의 내용만 추출
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if body_match:
        content = body_match.group(1).strip()
        return content
    # body 태그가 없으면 전체 내용 반환
    return html_content.strip()

# 템플릿 HTML (헤더 부분)
TEMPLATE_HEADER = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>게임 개발 현업자 강연</title>

    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/theme/black.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/highlight/monokai.css">

    <!-- Tailwind CSS (슬라이드 스타일링용) -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">

    <!-- Font Awesome -->
    <link href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" rel="stylesheet">

    <style>
        /* Reveal.js 기본 폰트 크기를 16px로 고정 (Tailwind 기본값) */
        .reveal {
            font-size: 16px;
        }

        /* Reveal.js 슬라이드 크기 설정 */
        .reveal .slides {
            text-align: left;
        }

        /* 슬라이드가 화면에 꽉 차도록 설정 */
        .reveal .slides section {
            height: 100%;
            width: 100%;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* 슬라이드 내부 컨텐츠가 전체 크기 사용 */
        .reveal .slides section > div {
            width: 100%;
            height: 100%;
        }

        /* Reveal.js의 기본 타이포그래피 스타일 무효화 */
        .reveal h1,
        .reveal h2,
        .reveal h3,
        .reveal h4,
        .reveal h5,
        .reveal h6 {
            text-transform: none;
            text-shadow: none;
            margin: 0;
            line-height: inherit;
        }

        .reveal p {
            margin: 0;
            line-height: inherit;
        }

        .reveal i {
            font-style: normal;
        }

        /* 아이콘이 제대로 표시되도록 */
        .reveal .fas {
            font-family: 'Font Awesome 6 Free';
            font-weight: 900;
            font-style: normal;
        }

        .reveal .far {
            font-family: 'Font Awesome 6 Free';
            font-weight: 400;
            font-style: normal;
        }

        .reveal .fab {
            font-family: 'Font Awesome 6 Brands';
            font-weight: 400;
            font-style: normal;
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
"""

# 템플릿 HTML (푸터 부분)
TEMPLATE_FOOTER = """        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/plugin/highlight/highlight.js"></script>
    <script>
        // reveal.js 초기화
        Reveal.initialize({
            // 슬라이드 크기 설정 (원본 크기에 맞춤)
            width: 1280,
            height: 720,
            margin: 0,
            minScale: 0.2,
            maxScale: 2.0,

            // 기본 설정
            hash: true,
            keyboard: true,
            touch: true,
            overview: true,
            center: false,  // 중앙 정렬 비활성화 (슬라이드 내부에서 제어)

            // 트랜지션 스타일
            transition: 'slide', // none/fade/slide/convex/concave/zoom

            // 플러그인
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        });
    </script>
</body>
</html>
"""

def build_presentation():
    """slides/ 디렉토리의 파일들을 읽어서 index.html 생성"""

    # slides 디렉토리 경로
    slides_dir = Path('slides')

    if not slides_dir.exists():
        print("[ERROR] slides/ 디렉토리가 없습니다.")
        return

    # slides 디렉토리의 모든 HTML 파일 가져오기 (정렬)
    slide_files = sorted(slides_dir.glob('*.html'))

    if not slide_files:
        print("[ERROR] slides/ 디렉토리에 HTML 파일이 없습니다.")
        return

    print(f"[INFO] {len(slide_files)}개의 슬라이드 파일 발견:")

    # HTML 생성
    html_content = TEMPLATE_HEADER

    # 각 슬라이드 파일 내용 추가
    for slide_file in slide_files:
        print(f"  - {slide_file.name}")

        # 파일 내용 읽기
        with open(slide_file, 'r', encoding='utf-8') as f:
            full_html = f.read()

        # body 내용만 추출
        body_content = extract_body_content(full_html)

        # <section> 태그로 감싸기
        html_content += f"            <!-- {slide_file.name} -->\n"
        html_content += "            <section>\n"
        html_content += "                " + body_content.replace('\n', '\n                ') + "\n"
        html_content += "            </section>\n\n"

    # 푸터 추가
    html_content += TEMPLATE_FOOTER

    # index.html 파일 쓰기
    output_file = Path('index.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"[SUCCESS] {output_file} 파일이 생성되었습니다!")

if __name__ == '__main__':
    build_presentation()
