# PEPPO CAMP

원본: GitHub Release `peppo_buldak`의 `PEPPO_CAMP_deck5.zip`.
덱 원본을 압축 해제해 이 저장소에서 이미지와 텍스트의 변경 이력을 관리합니다.

## 이미지 교체

1. `peppo_camp_deck/images/` 폴더를 엽니다.
2. GitHub에서 **Add file → Upload files**로 교체 이미지를 같은 파일명으로 올립니다.
   예: `IMG-01.png`. 확장자와 대소문자를 유지하세요. 16:9 권장.
3. **Commit changes**를 누릅니다. 기존 HTML이 같은 경로를 참조하므로 재빌드 없이 반영됩니다.
4. 로컬 덱을 새로 받거나 새로고침해 확인합니다. `REF-01.png`는 참고 화면입니다.

## 열기 및 ZIP 다운로드

- 저장소의 **Code → Download ZIP**으로 항상 최신 전체 파일을 받습니다.
- 압축 해제 후 `peppo_camp_deck/index.html`을 브라우저에서 엽니다.
- 덱만 담긴 ZIP은 Python 3에서 `python3 tools/package_deck.py`를 실행합니다.
  결과: `dist/PEPPO_CAMP_latest.zip`. 이미지 참조와 ZIP 무결성을 검사합니다.
- HTML 덱은 `python3 -m http.server 8000 --directory peppo_camp_deck`로 로컬에서 볼 수도 있습니다.

## 텍스트 수정

`index.html`을 직접 수정할 수 있습니다. 생성기로 관리하려면 `build.py`와
`scripts.py`를 수정한 뒤 `peppo_camp_deck` 안에서 `python3 build.py`를 실행하세요.
직접 편집한 HTML은 생성기를 실행하면 덮어써지므로 두 방식을 혼용하지 마세요.

원본 Release ZIP은 고정본입니다. 저장소의 이미지 교체가 기존 Release 첨부 ZIP을
자동 변경하지는 않습니다. 최신본은 Code → Download ZIP으로 받으세요.
