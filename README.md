# Presentation_CollageStudent

Reveal.js를 사용한 HTML 프레젠테이션 프로젝트입니다.

## 프로젝트 구조

```
Presentation_CollageStudent/
├── index.html          # 생성된 프레젠테이션 파일 (빌드 결과물)
├── package.json        # 프로젝트 설정
├── README.md          # 프로젝트 문서
├── build.py           # Python 빌드 스크립트
└── slides/            # 슬라이드 소스 파일들 (각 페이지별 분리)
    ├── 01..html           # 타이틀 슬라이드
    ├── 02.html            # 슬라이드 2
    ├── 03.html            # 슬라이드 3
    └── ...                # 기타 슬라이드들
```

## 사용 방법

### 1. 프레젠테이션 보기

#### 브라우저에서 직접 열기
`index.html` 파일을 더블클릭하거나 브라우저로 드래그하여 엽니다.

**참고**: 로컬 서버 없이도 정상 작동합니다!

### 2. 프레젠테이션 조작 방법

- **다음 슬라이드**: 화살표 키 (→, ↓) 또는 Space
- **이전 슬라이드**: 화살표 키 (←, ↑)
- **전체 보기**: ESC 또는 O
- **발표자 노트**: S
- **전체화면**: F
- **슬라이드 개요**: ESC

### 3. 슬라이드 편집하기

이 프로젝트는 슬라이드를 **파일별로 분리**하여 관리합니다.

#### 워크플로우
1. `slides/` 디렉토리의 HTML 파일 편집
2. 빌드 스크립트 실행 → `index.html` 자동 생성
3. 브라우저에서 확인

#### 기존 슬라이드 수정
`slides/` 디렉토리의 HTML 파일을 텍스트 에디터로 열어 수정합니다.

각 파일은 완전한 HTML 문서 형식입니다:
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8"/>
    <title>슬라이드 제목</title>
    <!-- CSS 링크 등 -->
</head>
<body>
    <!-- 슬라이드 내용 -->
</body>
</html>
```

수정 후 **반드시 빌드 스크립트 실행**:

```bash
python build.py
```

빌드 스크립트는 각 HTML 파일의 `<body>` 내용만 추출하여 Reveal.js의 `<section>` 태그로 변환합니다.

#### 새 슬라이드 파일 추가
1. `slides/` 디렉토리에 새 HTML 파일 생성 (예: `21.html`)
   - 파일명은 숫자로 시작하면 자동으로 정렬됩니다
2. 완전한 HTML 문서 형식으로 작성:
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>새 슬라이드</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet"/>
</head>
<body>
    <div class="flex items-center justify-center w-[1280px] min-h-[720px] bg-gray-900 text-white">
        <h1 class="text-6xl font-bold">새 슬라이드 제목</h1>
    </div>
</body>
</html>
```
3. 빌드 스크립트 실행:
```bash
python build.py
```
   - 파일이 자동으로 감지되어 `index.html`에 포함됩니다

## 고급 설정

### Reveal.js 테마 변경

`build.py` 파일의 `TEMPLATE_HEADER` 부분에서 테마를 변경할 수 있습니다:

```python
# 테마 옵션: black, white, league, beige, sky, night, serif, simple, solarized
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/theme/black.css">
```

테마 변경 후 `python build.py`를 실행하여 index.html을 재생성하세요.

## 추가 기능

- Markdown 지원
- 코드 하이라이팅
- 발표자 노트
- PDF 내보내기 (인쇄 모드)
- 자동 슬라이드 전환
- 터치/스와이프 지원

## 참고 자료

- [Reveal.js 공식 문서](https://revealjs.com/)
- [Reveal.js GitHub](https://github.com/hakimel/reveal.js)
