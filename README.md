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

## 이미지 세트 원복

현재 `peppo_camp_deck/images/`는 새 배경 이미지, `peppo_camp_deck/image2/`는
교체 전 원본입니다. `REF-01.png`는 실제 사례 자료이므로 양쪽에서 동일합니다.
덱 HTML과 텍스트는 변경하지 않았습니다.

다운로드한 폴더에서 다음처럼 이름을 바꾸면 즉시 원복됩니다.

1. `images` → `images_temp`
2. `image2` → `images`
3. `images_temp` → `image2`

다시 같은 순서를 실행하면 새 이미지로 돌아옵니다. 브라우저를 새로고침하세요.
각 폴더의 `SET.txt`로 원본/신규 세트를 확인할 수 있습니다.

## 최신 이미지 세트 — 불씨 크루의 야식 동네

- `images/`: 현재 적용된 불씨 크루 + 담백한 메타버스 게임 룩 (IMG-01~25).
- `image2/`: 최초 원본 캠퍼 세트.
- `image3/`: 이번 교체 직전의 캠퍼/질감 배경 세트.
- 실제 사례 자료 `REF-01.png`는 변경하지 않았습니다.

표지·공동의 불·행동·별 전환 장면은 함께 태우기와 불멍을 중심으로 제작했습니다.
HTML의 기존 문구/장표 구성은 유지했습니다. 이미지 세트 변경은 원하는 백업 폴더와
`images`의 이름을 임시 이름을 거쳐 맞바꾸면 됩니다.

확인: Code → Download ZIP → 압축 해제 → `peppo_camp_deck/index.html` 열기.

## 최신 개정 — 1인칭 / PEPPO / 개인 모션

- 현재 `images/`: 플레이어 눈높이 1인칭 장면 + PEPPO NPC로 재제작한 IMG-01~25.
- 21페이지: 공간 행동 4종, 22페이지: 개인 버튼 모션 4종(이미지+순서+피드백).
- 모션 설명 시트는 동작을 보여주기 위한 전신 관찰 이미지이며 일반 플레이는 1인칭입니다.
- PEPPO 등장 인원·동시 판정·쿨다운과 모션 길이는 제안 가안이며 실제 게임 구현은 아닙니다.
- 모니터 연출 제거, 화면 대신 종이 장작/별 카드/실물 소품으로 연결합니다.
- `image4/`: 이번 교체 직전의 불씨 크루 이미지 백업. `image2`, `image3`도 보존.
- `image_manifest.json`: 현재 25장 파일의 SHA-256 기록.
- 다운로드 후 `peppo_camp_deck/index.html` 열기. 22페이지는 `index.html#22`.
