# -*- coding: utf-8 -*-
"""PEPPO WORLD 리뉴얼 제안서 — 7막 스토리 덱 생성기 v3. images/IMG-XX.png 교체 가능."""
import html, math, json
from scripts import SCRIPTS

NAVY, PAPER, FIRE, AMBER, LIME, MUTE, CARD = "#0E1220", "#F3EFE6", "#FF6A2A", "#FFB020", "#D6FF3B", "#9A9AA8", "#171B2C"

IMG_DESC = {
 "IMG-01":"표지 — 밤의 캠프, 불 앞의 월드","IMG-02":"세 개의 불","IMG-03":"유리창 너머의 캐릭터",
 "IMG-04":"수백 개의 작은 가상 휴식 공간","IMG-05":"다섯 가지 이유 — 오브제 5종","IMG-06":"(미사용)",
 "IMG-07":"큰 불 앞 실루엣","IMG-08":"Real World → PEPPO Filter → PEPPO World","IMG-09":"캠프사이트 등각 지도",
 "IMG-10":"메인 캠프파이어 — 통나무 자리 100석","IMG-11":"호숫가 자리 — 같은 색 랜턴","IMG-12":"야식 자리 — 불 위의 라면 코펠 (재생성 필요)",
 "IMG-13":"숲길 탐색 노드 — 이스터에그","IMG-14":"네 가지 손동작 4분할 (4번째 패널 재생성 필요)","IMG-15":"태운 것은 별이 된다",
 "IMG-16":"불멍 모드 1인칭","IMG-17":"하루의 네 장면","IMG-18":"불 지킴이의 빈 자리","IMG-19":"캠퍼 라인업 6종",
 "IMG-20":"첫 방문 5분 스토리보드","IMG-21":"바람이 불을 키운다","IMG-22":"별이 현실로 내려오다",
 "IMG-23":"하나의 불에서 캠프 전체로","IMG-24":"별자리 하늘","IMG-25":"채널 브릿지 맵","REF-01":"참고 사례 실제 화면 (2026.11.02 캡처)",
}
ACTS = [("Needs","리뉴얼이 가져야 할 것"),("Signal","지금 사람들은 어디에 모이는가"),("Answer","불닭의 ‘태우다’를 ‘함께’로"),
        ("Principles","끝까지 지킬 세 가지"),("Elements","하나의 캠프, 네 개의 자리, 네 개의 행동"),("Impact","브릿지, 플라이휠, 지표"),("Roadmap","불 하나로 시작해 캠프 전체로")]

def img(i, extra="", h=None):
    d = IMG_DESC[i]; st = f' style="height:{h}px"' if h else ""
    return (f'<figure class="img {extra}" data-id="{i}"{st}><img src="images/{i}.png" alt="{html.escape(d)}" '
            f'onerror="this.closest(\'figure\').classList.add(\'missing\')">'
            f'<figcaption><b>{i}</b> {html.escape(d)}<br><span>images/{i}.png 로 교체</span></figcaption></figure>')

slides = []
def add(kind, **k): slides.append(dict(kind=kind, **k))
def blk(k, body, hi=False): return f'<div class="blk{" hi" if hi else ""}"><p class="k">{k}</p><p>{body}</p></div>'
def card(k, h, body, hi=False, extra=""): return f'<div class="card{" hi" if hi else ""}"><p class="k">{k}</p><h3>{h}</h3><p>{body}</p>{extra}</div>'

# =========================== 표지 ===========================
add("cover", img="IMG-01", eyebrow="PEPPO WORLD · peppoworld.com 리뉴얼 제안",
    title="밤의 캠프,<br>불 앞의 월드", sub="말없이 함께 태우고, 태운 것은 별이 된다.", meta="2026. 11. 02")

# =========================== 1막 Needs ===========================
add("divider", act=1, img="IMG-03", line="관계, 흔적, 그리고 측정 가능한 효과 — 리뉴얼이 가져야 할 세 가지.")

add("text", eyebrow="1막 · Needs", title="리뉴얼이 가져야 할 세 가지", body=f"""
<div class="cards3 big">
 {card("NEEDS 01","캐릭터를 아는 경험에서<br>관계를 맺는 경험으로","공식 채널이 소개하는 PEPPO를 사용자가 직접 체험하는 접점으로 확장한다. 보고 읽는 캐릭터가 아니라, 함께 무언가를 한 캐릭터.")}
 {card("NEEDS 02","내 흔적이 PEPPO의 세계를 바꾸고<br>현실에도 영향을 미친다","참여의 누적이 월드의 변화와 IP의 성장으로 이어지고, 그것이 다시 다음 방문의 이유가 된다.",hi=True)}
 {card("NEEDS 03","브랜드 브릿징 · 단계별 확장 ·<br>기대효과와 KPI","BULDAK ↔ PEPPO ↔ USER 를 잇는 구조, 작게 시작해 넓히는 확장안, 그리고 검증 가능한 지표.")}
</div>
<div class="keep"><b>유지하는 원칙</b> 비로그인 시작·저장 시 로그인 · 눈높이 카메라와 PEPPO 동행 · 공간마다 PEPPO의 반응, 탐색 후 허브 복귀 · 익명 표현과 운영 규정 · 소각 원문 비저장</div>""")

rows = [
 ("캐릭터를 아는 경험 → 관계를 맺는 경험","관계의 첫 단계 = 같은 불 앞에 함께 앉기"),
 ("공식 채널 소개 → 직접 체험하는 접점","URL 하나 · 로그인 0 · 설치 0, 10초 안에 불 앞"),
 ("내 흔적이 PEPPO 세계와 현실을 바꾼다","장작 → 불티 → 별. 별 마일스톤이 현실 보상으로"),
 ("컨텐츠 방향성 — 해소 · 공감 · 의외성 · 사건","4축 유지. 해소·공감 먼저, 의외성·사건은 숲길과 시간 이벤트로"),
 ("Real World → PEPPO Filter → PEPPO World","야근 책상이 통나무 자리로, 모니터 불빛이 모닥불로"),
 ("비로그인 시작, 저장 순간 로그인 가치","유지. 저장할 가치 = 내 별자리 · 캠퍼 · 캠프 네임"),
 ("공간 구조 · 이스터에그 · PEPPO 반응 · 허브 복귀","캠프파이어 = 허브, 모든 오솔길은 불로 돌아온다"),
 ("주요 Interaction &amp; Content","텍스트 0, 행동 4: 장작 넣기 · 바람 보내기 · 불 돋우기 · 라면 끓이기"),
 ("Community / 대나무숲 구조","글 없는 공감 — 바람 보내기 집계가 불 크기로 보인다"),
 ("Personalization / Login / 기록","Guest → Login → My Camp. 캠퍼 · 별자리 · 공유 카드가 기록"),
 ("Brand Bridging 구조","채널 브릿지 8개 — 릴스 · 숏츠 · 블로그 · 패키지 ↔ 월드"),
 ("MVP 및 단계별 확장안","캠프파이어 1개로 검증 → 스포크 → 숲길과 현실"),
 ("기대효과 / KPI 초안","플라이휠 6단계 → 3층위 10개 지표"),
]
nr = "".join(f'<div class="nrow"><div class="nd"><b>N{i+1:02d}</b><p>{a}</p></div><div class="narr">→</div><div class="rs"><p>{b}</p></div></div>' for i,(a,b) in enumerate(rows))
add("text", eyebrow="1막 · Needs → Response", title="열세 가지 Needs, 열세 가지 Response", body=f"""
<div class="nrhead"><span>Needs</span><span></span><span>Response</span></div><div class="nrlist">{nr}</div>""")

# =========================== 2막 Signal ===========================
add("divider", act=2, img="IMG-04", line="2026년 가을, 사람들은 ‘말없이 함께 있는 가상 공간’으로 몰렸다.")

add("split", eyebrow="2막 · Signal · 시장 신호", title="로그인도 채팅도 없는 공간에 사흘 만에 60만 명", img="REF-01", cap="참고 사례 실제 화면 · 2026.11.02 캡처 — 방 정원 100명, 행동 버튼 4개, 채팅 없음", body="""
<div class="nums">
 <div><b>60만</b><span>개인이 만든 가상 휴식 공간 1곳의 공개 사흘 방문 (제작자 집계)</span></div>
 <div><b>100<i>×</i>100</b><span>방 100개 × 정원 100명 — 피크에 만석, 입장 대기 발생</span></div>
 <div><b>300+</b><span>며칠 사이 등장한 유사 공간 (사우나 · 낚시터 · 캠핑장 · 루프탑…)</span></div>
 <div><b>0</b><span>로그인 · 설치 · 채팅 — 아무것도 요구하지 않았다</span></div>
</div>
<p class="note">사람들이 원한 것은 콘텐츠가 아니라 <b>‘지금 여기 누군가 함께 있다’는 기척</b>이었다.</p>""")

add("split", eyebrow="2막 · Signal · 착안점", title="왜 통했나 — 다섯 가지 구조", img="IMG-05", rev=True, body="""
<ol class="five">
 <li><b>무허들</b> URL 하나로 10초 안에 ‘내 캐릭터’</li>
 <li><b>함께 있음</b> 채팅 없이도 혼자가 아닌 감각</li>
 <li><b>반복 행위</b> 짧고 반복 가능한 동작 + 누적감</li>
 <li><b>공유 아바타</b> 같은 몸, 다른 소품 → 캡처 · 밈</li>
 <li><b>희소성</b> 1인 1석, 정원, 대기 — 지금 들어갈 이유</li>
</ol>
<p class="note">우리가 가져올 것은 이 다섯 가지 <b>구조</b>다. 소재와 정서는 가져오지 않는다.</p>""")

add("split", eyebrow="2막 · Signal · 그러나", title="형식은 하루면 복제된다 — 참고하되 닮지 않는다", img="IMG-04", body=f"""
{blk("관찰","화제가 된 지 며칠 만에 같은 형식의 공간이 300개 넘게 생겼다. 소프트웨어 자체는 더 이상 해자가 아니다.")}
{blk("판단","따라 만들면 우리는 301번째 복제품이 된다. 복제할 수 없는 것은 단 둘 — 14년을 쌓은 <b>브랜드 정체성</b>, 그리고 월드 밖 <b>현실로 돌아오는 보상</b>.")}
{blk("그래서","구조 다섯 가지만 배우고, <b>무대 · 행위 · 정서 · 시간 · 흔적</b> 다섯 가지는 전부 불닭의 것으로 다시 짓는다. 개인 개발자가 하루 만에 따라 할 수 있는 것은 하나도 남기지 않는다. 그 답이 다음 막이다.",hi=True)}""")

# =========================== 3막 Answer ===========================
add("divider", act=3, img="IMG-07", line="삼양 불닭의 정체성 ‘태우다’를, ‘함께’로 확장한다.")

add("identity", eyebrow="3막 · Answer · 아이덴티티", title="불닭은 이미 ‘태우다’의 브랜드다 — 우리는 그 동사에 ‘함께’를 붙인다", img="IMG-02")

add("statement", img="IMG-07", eyebrow="3막 · Answer · 컨셉", title="밤의 캠프,<br>불 앞의 월드",
    sub="혼자 온 사람들이 같은 불 앞에 앉는다. 각자의 스트레스를 장작으로 접어 넣는다.<br>불은 모일수록 커지고, 태운 것은 별이 되어 하늘에 남는다. 별이 모이면, 현실이 바뀐다.",
    tags=["장작 넣기","바람 보내기","불멍 모드","태운 것은 별이 된다","밤 10시 불 피우기"])

add("wide", imgh=470, eyebrow="3막 · Answer · 핵심 컨셉과의 정합", title="Real World → PEPPO Filter → PEPPO World, 그대로 통한다", img="IMG-08", body=f"""
<div class="cards3 tight grow">
 {card("REAL WORLD","익숙한 공간의 단서","야근 책상, 퇴근길 편의점 앞, 비 오는 정류장 — 스트레스가 쌓이는 현실의 장소.")}
 {card("PEPPO FILTER","로우폴리 · 밤 · 불","종이 더미는 장작으로, 모니터 불빛은 모닥불로, 사무실 천장은 밤하늘로. 거친 텍스처와 비현실적 크기의 불.",hi=True)}
 {card("PEPPO WORLD","정체된 것을 해소하는 경험","같은 불 앞에 100명. 말은 없고 행동만 보인다. PEPPO는 화면 앞에서 불을 지키는 동행.")}
</div>""")

# =========================== 4막 Principles ===========================
add("divider", act=4, img="IMG-15", line="불은 살아 있고, 말은 없고, 태운 것은 남는다.")

add("trio", eyebrow="4막 · Principles · 세 가지 원칙", title="불은 살아 있고, 말은 없고, 태운 것은 남는다", items=[
 ("IMG-21","원칙 01","불은 살아 있다","참여자 수와 장작이 불의 크기 · 색을 바꾼다. 같은 공간이 시간과 사람에 따라 다른 공간이 된다. 불이 곧 ‘함께 있음’의 계기판."),
 ("IMG-11","원칙 02","말은 없다","채팅 · 공개 글 없음. 행동 4개와 토스트 한 줄만. 안전하고, 운영 부담이 0이고, 그래서 머문다."),
 ("IMG-15","원칙 03","태운 것은 남는다","장작 하나 = 별 하나. 개인의 별자리, 캠프의 밤하늘, 브랜드의 마일스톤. ‘내 흔적이 세계를 바꾼다’의 구현."),
])

# =========================== 5막 Elements ===========================
add("divider", act=5, img="IMG-09", line="하나의 캠프, 네 개의 자리, 네 개의 행동, 하루의 시간, 그리고 PEPPO.")

add("quad", eyebrow="5막 · Elements · 월드 구조", title="허브는 불, 모든 오솔길은 불로 돌아온다", img="IMG-09", items=[
 ("IMG-10","MVP · 허브","<b>메인 캠프파이어</b> — 캠프사이트 N개 × 통나무 자리 100석. 행동 4개와 사운드. 모든 것의 중심.",True),
 ("IMG-11","PHASE 2 · 스포크","<b>호숫가 자리</b>(글 없는 공감) · <b>야식 자리</b>(브랜드 플레이) · <b>언덕 무대</b>(밤 10시 이벤트).",False),
 ("IMG-13","PHASE 2–3 · 길","<b>숲길 탐색 노드</b> — 로드뷰 · 화살표 이동과 이스터에그. 어디서든 불빛이 보이고, 돌아올 수 있다.",False),
])

add("split", eyebrow="5막 · 공간 01 · 메인 캠프파이어", title="통나무 자리 100석, 1인 1석", img="IMG-10", rev=True, body=f"""
{blk("구조","불을 중심으로 네 겹의 통나무 자리. 자리가 차면 다음 캠프사이트로, 모두 차면 “대기 중 N명”. 희소성이 화제를 만든다.")}
{blk("불의 상태","참여자 수와 장작 투입량이 불의 크기 · 색을 결정한다. 새벽의 잔불과 밤 10시의 큰 불은 다른 공간처럼 느껴진다.")}
{blk("텍스트","장작에 적는 내용은 선택 · 비공개 · 비저장. 누구도 읽을 수 없고, 불티만 올라간다.",hi=True)}""")

add("split", eyebrow="5막 · 공간 02 · 호숫가 자리", title="말은 없고, 랜턴 색이 같아진다", img="IMG-11", body=f"""
{blk("대나무숲의 진화","공개 글 대신 ‘앉기 + 바람 보내기’. 같은 시간에 앉은 사람들의 랜턴이 같은 색으로 맞춰진다 — 공감의 집계가 눈에 보인다.")}
{blk("운영","검수 · 신고 · 개인정보 리스크가 구조적으로 사라진다. 공개되는 것은 이모트 집계뿐.")}
{blk("월드 반영","호숫가 공감 누적이 메인 캠프파이어의 불꽃 레벨(Lv.1–5)을 올린다. ‘집계된 마음을 월드에 반영’을 실시간으로.",hi=True)}""")

add("split", eyebrow="5막 · 공간 03 · 야식 자리", title="불 위에 코펠 하나 — 라면이 끓는 자리", img="IMG-12", rev=True, body=f"""
{blk("불닭먹기 Zone의 계승","모닥불 위 코펠에 불닭을 끓인다. 물이 끓고, 면을 넣고, 소스를 붓는 세 번의 탭. 김이 오르면 주변 캠퍼의 화면에도 매운 김이 번진다.")}
{blk("브랜드 플레이","매움 단계에 따라 국물 색과 김의 양이 바뀐다. 한 젓가락 ‘맵찔이 탈출’에 성공하면 뱃지. 제품 라인업이 자연스럽게 코펠 옆 소품이 된다.")}
{blk("연결","다 끓이면 메인 불에 보너스 장작. 야식이 허브의 불을 키운다.",hi=True)}""")

add("split", eyebrow="5막 · 공간 04 · 숲길 탐색 노드", title="로드뷰 문법은 숲길에서 산다", img="IMG-13", body=f"""
{blk("이동 원칙 유지","눈높이 1인칭, 바닥의 화살표 노드로 이동. PEPPO가 앞서 걷는 동행 포지션.")}
{blk("의외성 · 이스터에그","길가에 비현실적으로 큰 머그컵, 뒤집힌 의자, 나무 둥치의 작은 문. 도달하면 PEPPO가 반응하고 도감에 기록된다.")}
{blk("허브 복귀","어느 길에서도 멀리 불빛이 보인다. 탐색이 끝나면 불로 돌아온다 — 길을 잃지 않는 월드.",hi=True)}""")

add("split", eyebrow="5막 · 행동", title="텍스트 0, 행동 4로 끝나는 밤", img="IMG-14", rev=True, body="""
<div class="btns">
 <div><b>장작 넣기</b><span>스트레스 하나를 접어 불에. 누적 → 내 별자리</span></div>
 <div><b>바람 보내기</b><span>옆 사람의 불을 키워 주는 말 없는 응원</span></div>
 <div><b>불 돋우기</b><span>부지깽이로 불을 쑤시면 불꽃이 튀고 소리가 난다</span></div>
 <div><b>라면 끓이기</b><span>가만히 있어도 젓가락이 면을 휘젓는 idle, 브랜드 플레이</span></div>
</div>
<p class="note">모든 행동은 토스트 한 줄로만 전달된다 — “4단계 밤바람 님이 장작을 넣었어요”.</p>""")

add("split", eyebrow="5막 · 핵심 메커니즘", title="태운 것은 별이 된다", img="IMG-15", body=f"""
{blk("개인","장작 하나 = 불티 하나 = 별 하나. 내가 태운 별들이 이어져 <b>내 별자리</b>가 된다. 저장하려면 로그인.",hi=True)}
{blk("집단","캠프사이트의 하늘은 그 방 사람들이 태운 모든 별로 채워진다. 자정이 가까울수록 하늘이 빽빽해진다.")}
{blk("현실","월드 전체 별 수가 마일스톤에 닿으면 브랜드가 움직인다 — 신제품 선공개, 시즌 장작 교환권, 캠페인 카피 채택.")}""")

add("wide", imgh=470, eyebrow="5막 · 시간 설계 · 돌아올 이유", title="해 질 녘 입장, 밤 10시 불 피우기, 새벽 리셋", img="IMG-17", body="""
<div class="cards4 grow">
 <div class="card"><p class="k">18:00 해 질 녘</p><p>캠프가 열린다. 불은 작고 자리는 비어 있다. 먼저 온 사람이 불을 키운다.</p></div>
 <div class="card hi"><p class="k">22:00 불 피우기</p><p>매일 밤 10시, 모든 캠프사이트가 동시에 큰 불을 올린다. ‘함께’가 가장 진한 시간.</p></div>
 <div class="card"><p class="k">00:00 자정</p><p>하늘이 별로 가득 찬다. 별자리 선이 이어지고, 오늘의 집계가 확정된다.</p></div>
 <div class="card"><p class="k">05:00 새벽</p><p>별이 지고 잔불만 남는다. 하늘은 리셋, 내 별자리는 My Camp에 남는다.</p></div>
</div>""")

add("split", eyebrow="5막 · 불멍 모드 · 사운드", title="머무는 이유는 소리와 카메라가 만든다", img="IMG-16", rev=True, body=f"""
{blk("카메라","버튼 하나로 시점이 불 바로 앞으로 내려간다. UI가 사라지고 불꽃만 남는다. 10분을 머물게 하는 화면.")}
{blk("사운드 레이어","장작 타는 소리 · 밤 풀벌레 · 호수 바람 · PEPPO 허밍(선택). 야식 자리에선 보글보글 끓는 브랜드 사운드.")}
{blk("지표로","불멍 모드 평균 체류 시간이 ‘관계’의 선행 지표가 된다. 6막 KPI의 첫 칸.",hi=True)}""")

add("split", eyebrow="5막 · PEPPO의 역할", title="PEPPO는 아바타가 아니라 불 지킴이다", img="IMG-18", body=f"""
{blk("시점 원칙","사용자 눈높이 카메라, PEPPO는 화면 앞쪽의 동행. 사용자가 PEPPO를 ‘조작’하지 않고 PEPPO와 ‘함께’ 있는다.")}
{blk("행동 양식(가안)","장작을 넣으면 부채질로 거든다 · 별이 뜨면 올려다본다 · 자리가 차면 다음 캠프사이트로 이끈다 · 밤 10시엔 큰 장작을 꺼낸다.",hi=True)}
{blk("IP 보호","사용자 아바타는 ‘캠퍼’. PEPPO 본체의 꾸미기 · 변형은 열지 않는다. PEPPO Word는 불 앞에서 한 줄씩 건네는 말로.")}""")

add("split", eyebrow="5막 · 캠퍼 아바타", title="입장 10초 만에 생기는 ‘내 캠퍼’가 공유를 만든다", img="IMG-19", rev=True, body=f"""
{blk("캠프 네임","입장 즉시 랜덤 이름 — 매움 단계 × 밤의 자연물. “4단계 밤바람”, “은근히 매운 호수”, “까르보 새벽안개”.")}
{blk("꾸미기","같은 몸, 다른 소품: 비니 · 담요 망토 · 헤드랜턴 · 귀마개 · 뿔 후드. 장작 누적과 시즌 이벤트로 해금.")}
{blk("공유 카드","“오늘 2,431명과 함께 태웠어요” + 내 캠퍼 + 내 별자리. 캡처 하나로 스레드 · 인스타에. 1인칭에선 불가능했던 ‘내가 보이는’ 확산.",hi=True)}""")

add("sharecard", eyebrow="5막 · 공유 카드 · 예시와 근거", title="‘내가 보이는’ 한 장 — 공유 카드는 이렇게 생겼다")

add("wide", imgh=440, eyebrow="5막 · 첫 방문 5분", title="허들 없이 불 앞까지, 저장할 때 로그인", img="IMG-20", body="""
<div class="steps grow">
 <div><b>00:00</b>URL 클릭<span>로그인 · 설치 없음</span></div>
 <div><b>00:05</b>캠퍼 + 캠프 네임<span>“4단계 밤바람”</span></div>
 <div><b>00:10</b>캠프사이트 입장<span>빈 통나무 자리</span></div>
 <div><b>00:30</b>장작 넣기<span>첫 불티가 별이 된다</span></div>
 <div><b>03:00</b>불멍 · 바람 보내기<span>머무는 이유</span></div>
 <div><b>05:00</b>공유 카드<span>스레드로 확산</span></div>
 <div class="hi"><b>D+1</b>내 별자리 저장<span>로그인 가치 제시</span></div>
</div>""")

# =========================== 6막 Impact ===========================
add("divider", act=6, img="IMG-22", line="브랜드와 캐릭터와 사용자가 하나의 불로 이어지고, 효과는 숫자로 남는다.")

add("bridge", eyebrow="6막 · Impact · Brand Bridging ① 채널 브릿지 맵", title="공식 채널과 월드가 매일 서로를 불러들인다", img="IMG-25")

add("text", eyebrow="6막 · Impact · Brand Bridging ② 콘텐츠 · 포맷 · 주기", title="브릿지 8개 — 무엇을, 어떤 포맷으로, 얼마나 자주", body="""
<table class='t br'>
 <tr><th style='width:90px'>방향</th><th style='width:250px'>채널</th><th style='width:560px'>콘텐츠</th><th style='width:300px'>포맷</th><th style='width:170px'>주기</th><th>연결 지표</th></tr>
 <tr><td class='in' rowspan='4'>IN<br><span>채널→월드</span></td><td class='b'>인스타 릴스 · 유튜브 숏츠</td><td>“오늘 밤 10시 불 피우기” — 불 지킴이 PEPPO가 큰 장작을 꺼내는 15초 루틴, 링크 스티커로 입장</td><td>9:16 · 15초 · 자동 렌더</td><td>매일 21:30</td><td class='m'>공유 경유 유입</td></tr>
 <tr><td class='b'>인스타 스토리 필터</td><td>“내 캠프 네임 뽑기” AR 필터 → 결과 화면에 딥링크, 같은 이름으로 월드 입장</td><td>스토리 필터 · 딥링크</td><td>상시</td><td class='m'>신규 입장</td></tr>
 <tr><td class='b'>buldak.com 블로그</td><td>PEPPO WORLD 소개 글에 ‘지금 밤하늘 별 수 · 접속 중 캠퍼 수’ 라이브 위젯 임베드</td><td>iframe 위젯</td><td>실시간</td><td class='m'>블로그 → 월드 CTR</td></tr>
 <tr><td class='b'>제품 패키지 QR</td><td>라면 봉지 · 컵 QR → ‘시즌 장작’ 1개 지급(까르보 장작, 핵불 장작). 제품이 월드의 소재가 된다</td><td>QR · 한정 장작</td><td>시즌별</td><td class='m'>QR 스캔 → 입장</td></tr>
 <tr><td class='out' rowspan='4'>OUT<br><span>월드→채널</span></td><td class='b'>공유 카드 → 스레드 · 인스타</td><td>“오늘 N명과 함께 태웠어요” + 내 캠퍼 + 내 별자리, 캡처 한 번에 9:16 · 1:1 두 포맷 생성</td><td>1080×1920 · 1080×1080</td><td>사용자 행동 시</td><td class='m'>공유 카드 생성 수</td></tr>
 <tr><td class='b'>공식 릴스 · 숏츠</td><td>‘오늘의 밤하늘’ — 자정에 그날 쌓인 별을 30초 타임랩스로 자동 렌더, 공식 계정 업로드</td><td>9:16 · 30초 · 자동</td><td>매일 00:10</td><td class='m'>릴스 조회 · 저장</td></tr>
 <tr><td class='b'>buldak.com 블로그 · 뉴스룸</td><td>별 마일스톤(10만 · 100만) 달성 포스트 + 신제품 선공개, 완전 연소 캠퍼 명예의 전당</td><td>포스트 · 보도자료</td><td>마일스톤</td><td class='m'>보상 교환율</td></tr>
 <tr><td class='b'>캠페인 카피 · 숏츠 자막</td><td>호숫가 공감 집계가 만든 문장(“오늘 8,120명이 바람을 보냈다”)을 다음 캠페인 카피 · 자막으로 채택</td><td>카피 · 자막 소스</td><td>월간</td><td class='m'>연상 일치도</td></tr>
</table>
<p class='note'>메시지 층위는 하나 — BULDAK ‘태워서 푼다’ → PEPPO ‘불을 지킨다’ → USER ‘함께 태운다’. 위 8개 브릿지는 그 메시지가 채널을 건너는 실제 통로다. 보상 · 편성은 브랜드팀 확인 전 가안.</p>""")

add("wheel", eyebrow="6막 · Impact · 기대효과", title="불이 도는 구조 — 한 바퀴 돌 때마다 지표가 쌓인다", nodes=[
 ("01","들어온다","URL 하나, 10초 안에 불 앞","신규 입장 · 블로그 CTR"),
 ("02","함께 태운다","행동 4 · 불멍 · 기척","CCU 피크 · 장작/인 · 불멍 체류"),
 ("03","별이 남는다","내 별자리 · 캠프의 하늘","로그인 전환 · 점유율"),
 ("04","돌아온다","밤 10시 · 희소 자리 · 시간","D1/D7 재방문"),
 ("05","퍼뜨린다","공유 카드 · 오늘의 밤하늘","공유 카드 수 · 릴스 조회"),
 ("06","현실로 온다","별 마일스톤 → 보상 · 신제품","보상 교환율 · 연상 일치도"),
], center=("관계","캐릭터를 아는 경험에서<br>관계를 맺는 경험으로"))

add("text", eyebrow="6막 · Impact · KPI 대시보드", title="세 층위 열 개 지표 — 한눈에 보는 측정 체계", body="""
<div class="kpiwrap grow">
 <div class="tier"><div class="tname"><b>선행</b><span>행동 지표 · 매일</span></div>
  <div class="tiles">
   <div class="tile"><b>CCU 피크</b><span>캠프사이트별 최대 동시접속</span><i>실시간 집계</i></div>
   <div class="tile"><b>자리 점유율</b><span>100석 중 점유 · 대기 발생 횟수</span><i>시간대별</i></div>
   <div class="tile"><b>장작/인</b><span>1인당 장작 넣기 횟수</span><i>세션 기준</i></div>
   <div class="tile"><b>불멍 체류</b><span>불멍 모드 평균 체류 시간</span><i>분 단위</i></div>
  </div></div>
 <div class="tier"><div class="tname"><b>핵심</b><span>관계 지표 · 주간</span></div>
  <div class="tiles">
   <div class="tile hi"><b>D7 재방문</b><span>첫 방문 후 7일 내 재방문 고유 사용자 비율</span><i>디바이스 ID 기준 · 비로그인 포함</i></div>
   <div class="tile hi"><b>로그인 전환</b><span>별자리 저장 시점의 Guest → Login 전환율</span><i>저장 시점</i></div>
   <div class="tile hi"><b>공유 카드</b><span>생성 수 · 공유 경유 유입 비율</span><i>UTM</i></div>
  </div></div>
 <div class="tier"><div class="tname"><b>결과</b><span>브랜드 지표 · 월간</span></div>
  <div class="tiles">
   <div class="tile m"><b>호감도 변화</b><span>사전/사후 PEPPO · 브랜드 짧은 설문</span><i>설문</i></div>
   <div class="tile m"><b>연상 일치도</b><span>‘태워서 푼다’ 메시지 연상 — 참여자 vs 비참여자</span><i>대조군 비교</i></div>
   <div class="tile m"><b>보상 교환율</b><span>별 마일스톤 보상의 실제 교환 비율</span><i>현실 연결</i></div>
  </div></div>
</div>
<p class="note">목표치는 MVP 운영 2주 후 설정 · 분모 · 중복 제거 · 동의 기반 식별 · 관찰 기간은 측정 명세에서 확정 · 시장 참고치(사흘 60만, 방 100×100)는 벤치마크일 뿐 목표가 아님</p>""")

add("text", eyebrow="6막 · Impact · 측정 설계", title="열 개 지표는 어떻게 재나 — 식별 기준과 한계", body="""
<table class='t ms'>
 <tr><th style='width:200px'>지표</th><th style='width:470px'>측정 방법</th><th style='width:420px'>식별 기준</th><th>한계와 보정</th></tr>
 <tr><td class='b'>CCU 피크 · 자리 점유율</td><td>서버 세션 카운트, 캠프사이트별 1분 단위</td><td>세션 (로그인 불필요)</td><td>탭 중복 → 동일 디바이스 ID 병합</td></tr>
 <tr><td class='b'>장작/인 · 불멍 체류</td><td>행동 이벤트 로그 (장작·바람·돋우기·라면), 불멍 모드 진입/이탈 타임스탬프</td><td>디바이스 ID + 세션</td><td>백그라운드 탭은 visibility 이벤트로 제외</td></tr>
 <tr><td class='b hi'>D7 재방문</td><td>첫 방문 시 <b>1st-party 쿠키 + localStorage에 디바이스 ID 발급(동의 배너)</b>. 7일 내 같은 ID 재접속이면 재방문. 로그인 시 계정에 ID 병합</td><td class='hi'>디바이스 ID 기준 — <b>로그인 없이도 측정</b></td><td>Safari ITP는 스크립트 쿠키를 7일 뒤 삭제 → 서버가 세팅하는 쿠키로 회피, 7일 지표라 영향 최소. 캐시 삭제·기기 변경은 과소 집계(보수적)</td></tr>
 <tr><td class='b'>로그인 전환</td><td>별자리 저장 버튼 노출 → 로그인 완료 퍼널</td><td>디바이스 ID → 계정</td><td>저장 버튼 노출 수를 분모로 (전체 방문 아님)</td></tr>
 <tr><td class='b hi'>공유 카드</td><td>카드 생성 이벤트 수 + 카드에 심은 <b>UTM/딥링크</b>로 공유 경유 유입 수</td><td class='hi'>생성: 디바이스 ID · 유입: UTM</td><td>이미지 저장 후 수동 업로드는 UTM 유실 → 카드에 짧은 입장 코드 인쇄로 보정</td></tr>
 <tr><td class='b'>호감도 변화</td><td>입장 직후 1문항 · 7일 후 재방문 시 1문항 (월드 내 팝업)</td><td>디바이스 ID (동일인 전후 비교)</td><td>응답 편향 → 외부 패널 설문으로 교차 검증(월간)</td></tr>
 <tr><td class='b'>연상 일치도</td><td>‘태워서 푼다’ 자유 연상 설문 — 참여자(월드 내) vs 비참여자(브랜드 채널 팔로워 패널)</td><td>참여 여부로 군 분리</td><td>자기선택 편향 → 인구통계 가중</td></tr>
 <tr><td class='b'>보상 교환율</td><td>별 마일스톤 보상 쿠폰 코드 발급 수 대비 사용 수</td><td>쿠폰 코드</td><td>오프라인 사용은 POS 연동 또는 코드 입력 집계</td></tr>
</table>
<p class="note">원칙: 비로그인 사용자도 디바이스 ID로 추적하되 <b>동의 기반·식별 불가 정보만</b>. 로그인 전환 시 ID를 계정에 병합해 전후 연속성을 확보. 모든 지표의 분모와 중복 제거 규칙은 MVP 착수 1주차 측정 명세에서 확정.</p>""")

# =========================== 7막 Roadmap ===========================
add("divider", act=7, img="IMG-23", line="불 하나로 검증하고, 캠프 전체로 넓힌다.")

add("wide", imgh=400, eyebrow="7막 · Roadmap · MVP 및 단계별 확장", title="불 하나로 검증하고, 캠프 전체로 넓힌다", img="IMG-23", body=f"""
<div class="cards3 tight grow">
 {card("MVP · 6–8주 · 경험 검증","캠프파이어 1 + 행동 4 + 사운드 + 캠퍼","캠프사이트 N × 100석 · 장작 · 바람 · 돋우기 · 라면 · 불멍 모드 · 캠프 네임 · 공유 카드 · 별 누적(저장 시 로그인)",hi=True,extra='<p class="j">판단: CCU · 체류 · 공유 발생</p>')}
 {card("PHASE 2 · 관계 강화","스포크 연결","호숫가 자리(공감 집계) · 야식 자리 · 언덕 무대(밤 10시) · My Camp 컬렉션 · 삭제 경로 · 주간 공동 목표",extra='<p class="j">판단: D7 · 로그인 전환</p>')}
 {card("PHASE 3 · 브랜드 확장","숲길과 현실","로드뷰 탐색 노드 · 이스터에그 · 시즌 장작 · 별 마일스톤 → 실물 보상 · 오프라인 연결 · 글로벌 언어 · 메신저/미니앱",extra='<p class="j">판단: 연상 일치도 · 보상 교환</p>')}
</div>""")

add("text", eyebrow="7막 · Roadmap · 리스크 · 결정 · 다음 2주", title="결정할 것과 2주 안에 할 것", body="""
<div class="cols2 grow">
 <div><h3>리스크와 대응</h3>
  <table class="t sm"><tr><th>리스크</th><th>대응</th></tr>
   <tr><td>트렌드 추종으로 보일 가능성</td><td>무대 · 행위 · 정서 · 시간 · 흔적이 전부 고유. 대외 커뮤니케이션에서 참고 서비스 언급 금지</td></tr>
   <tr><td>형식 복제(수일 내 300+)</td><td>IP 행동 · 사운드 · 실물 보상 · 캠페인 연동 — 개인이 복제할 수 없는 영역에 집중</td></tr>
   <tr><td>유행 소멸</td><td>캠프파이어는 상시 허브, 시간 이벤트 · 시즌 장작 · 숲길 탐색이 재방문 장치</td></tr>
   <tr><td>부정 텍스트 · 개인정보</td><td>공개 텍스트 없음, 장작 내용 비공개 · 비저장</td></tr>
   <tr><td>동시접속 급증</td><td>캠프사이트 단위(100명) 수평 확장, 대기열을 UX로 흡수</td></tr>
  </table></div>
 <div><h3>결정 사항</h3>
  <ol class="list"><li>MVP 범위: 캠프파이어 허브 단독 시작 vs 원안(노드 월드 포함)</li><li>아바타 정책: 캠퍼(더미 기반) 확정</li><li>PEPPO 행동양식 · PEPPO Word 정의</li><li>로그인 방식 · 저장 범위</li><li>현실 보상 항목(브랜드팀)</li></ol>
  <h3 style="margin-top:24px">다음 2주</h3>
  <ol class="list"><li>캠프사이트 1곳 플레이어블 프로토타입(웹, 행동 4, 20석)</li><li>캠퍼 스타일 프레임 3안 + 캠프 네임 생성 규칙</li><li>사운드 데모 2트랙(장작 · 풀벌레 / 보글보글)</li><li>내부 테스트 30명 → CCU · 체류 · 행동 분포 관찰</li><li>현행 사이트 방문 · 재방문 데이터 재확인</li></ol>
 </div>
</div>""")

add("statement", img="IMG-24", eyebrow="마무리", title="태운 것은<br>별이 된다",
    sub="관계는 ‘함께 한 것’에서 생긴다. 불닭의 ‘태우다’를 ‘함께’로 넓히면,<br>캐릭터를 아는 경험은 캐릭터와 관계를 맺는 경험이 된다.", tags=["Needs 13개 전부 응답","복제 불가한 3원칙","측정 가능한 10개 지표"])

# =========================== RENDER ===========================
def footer(n): return f'<p class="foot">PEPPO WORLD / RENEWAL PROPOSAL · {n:02d}</p>'
def storybar(act):
    return '<div class="sbar">' + "".join(f'<span class="{"on" if i+1==act else ("done" if i+1<act else "")}"><i>{i+1}</i>{a}</span>' for i,(a,_) in enumerate(ACTS)) + '</div>'

def wheel_svg(s):
    cx, cy, r = 600, 430, 290
    cols = ["#FF4A1C","#FF6A2A","#FF8A2A","#FFB020","#E8D234","#D6FF3B"]
    defs = '<defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>' \
           '<radialGradient id="core" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#FFB020" stop-opacity=".95"/><stop offset=".45" stop-color="#FF6A2A" stop-opacity=".85"/><stop offset="1" stop-color="#2A1A12" stop-opacity="1"/></radialGradient>' \
           '<radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FF6A2A" stop-opacity=".35"/><stop offset="1" stop-color="#FF6A2A" stop-opacity="0"/></radialGradient></defs>'
    out = [defs, f'<circle cx="{cx}" cy="{cy}" r="{r+120}" fill="url(#halo)"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1E2338" stroke-width="54"/>']
    seg = 2*math.pi/6; gap = 0.30
    for i in range(6):
        a1 = -math.pi/2 + i*seg + 0.27; a2 = -math.pi/2 + (i+1)*seg - 0.31
        x1,y1 = cx+r*math.cos(a1), cy+r*math.sin(a1); x2,y2 = cx+r*math.cos(a2), cy+r*math.sin(a2)
        out.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{cols[i]}" stroke-width="26" stroke-linecap="round"/>')
        # chevron at the end of arc
        ang = a2 + math.pi/2; tx, ty = x2, y2
        px, py = math.cos(ang), math.sin(ang); nx, ny = math.cos(a2), math.sin(a2)
        tip = (tx+px*22, ty+py*22); l = (tx-px*2+nx*17, ty-py*2+ny*17); rgt = (tx-px*2-nx*17, ty-py*2-ny*17)
        out.append(f'<path d="M{tip[0]:.1f} {tip[1]:.1f} L{l[0]:.1f} {l[1]:.1f} L{rgt[0]:.1f} {rgt[1]:.1f}Z" fill="{cols[i]}"/>')
    for i,(no,t,d,kpi) in enumerate(s["nodes"]):
        a = -math.pi/2 + i*seg; x,y = cx+r*math.cos(a), cy+r*math.sin(a)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="46" fill="#0E1220" stroke="{cols[i]}" stroke-width="5"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="34" fill="{cols[i]}" opacity=".18"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="url(#core)"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="#FFB020" stroke-opacity=".5" stroke-width="2"/>')
    return f'<svg class="wsvg" width="1180" height="860" viewBox="0 0 1180 860">{"".join(out)}</svg>', cx, cy, r

def render(s, n):
    k = s["kind"]
    if k == "cover":
        return f"""<section class="slide cover">{img(s['img'],'bg')}<div class="scrim"></div>
<div class="covtxt"><p class="eyebrow">{s['eyebrow']}</p><h1>{s['title']}</h1><p class="sub">{s['sub']}</p></div>
<div class="covbar"><span>peppoworld.com 리뉴얼 제안서 · Needs → Response</span><span class="lime">{s['meta']}</span></div></section>"""
    if k == "divider":
        en, ko = ACTS[s['act']-1]
        return f"""<section class="slide divider">{img(s['img'],'bg')}<div class="scrim3"></div>
<div class="divtxt"><p class="actno">ACT {s['act']}</p><h1>{en}</h1><p class="ko">{ko}</p><p class="line">{s['line']}</p></div>{storybar(s['act'])}{footer(n)}</section>"""
    if k == "statement":
        tags = "".join(f"<span>{t}</span>" for t in s["tags"])
        return f"""<section class="slide statement">{img(s['img'],'bg')}<div class="scrim2"></div>
<p class="eyebrow abs">{s['eyebrow']}</p><div class="sttxt"><h1>{s['title']}</h1><p class="sub">{s['sub']}</p><div class="tags">{tags}</div></div>{footer(n)}</section>"""
    head = f"<header><p class='eyebrow'>{s['eyebrow']}</p><h2>{s['title']}</h2></header>"
    if k == "identity":
        return f"""<section class="slide identity">{head}
<div class="idrow">
 <div class="idcol">
  <p class="idh">BULDAK · 브랜드가 이미 가진 것</p>
  <div class="idc"><b>맵다</b><span>도전 — 한 입이 시험이다</span></div>
  <div class="idc"><b>견딘다</b><span>땀과 눈물, 그래도 멈추지 않는다</span></div>
  <div class="idc"><b>푼다</b><span>해소 — 다 먹고 나면 속이 뚫린다</span></div>
  <div class="idc"><b>함께 먹는다</b><span>챌린지 문화 — 혼자 먹는 불닭보다 함께 찍는 불닭</span></div>
 </div>
 <div class="idmid">
  {img(s['img'],'idimg')}
  <div class="idverb"><p class="k">브랜드의 동사</p><h3>태우다</h3><p>매움을 태우고, 스트레스를 태우고, 밤을 태운다</p></div>
 </div>
 <div class="idcol">
  <p class="idh out">PEPPO CAMP · 우리가 붙이는 것</p>
  <div class="idc out"><b>장작</b><span>맵다 → 스트레스 하나를 접어 불에 넣는다</span></div>
  <div class="idc out"><b>함께 앉는다</b><span>견딘다 → 같은 불 앞 100명, 혼자가 아니다</span></div>
  <div class="idc out"><b>별이 남는다</b><span>푼다 → 태운 것이 하늘에 흔적으로 남는다</span></div>
  <div class="idc out"><b>공유 카드</b><span>함께 먹는다 → “오늘 N명과 함께 태웠어요”</span></div>
 </div>
</div>
<div class="idfoot"><b>태우다 × 함께</b> 현재의 소각장은 방향이 맞다. 빠진 것은 ‘혼자 태운다’는 점 하나 — 불닭이 챌린지로 증명한 ‘함께’를 붙이면, 불닭의 불이 PEPPO의 불이 되고 사용자의 불이 된다.</div>
{footer(n)}</section>"""
    if k == "quad":
        items = "".join(f'<div class="qi"><div class="qimg">{img(i)}</div><div class="blk{" hi" if hi else ""}"><p class="k">{kk}</p><p>{b}</p></div></div>' for i,kk,b,hi in s["items"])
        return f"""<section class="slide quad">{head}<div class="row">{img(s['img'],'qmain')}<div class="qcol">{items}</div></div>{footer(n)}</section>"""
    if k == "trio":
        items = "".join(f'<div class="ti">{img(i,"timg")}<div class="card hi"><p class="k">{kk}</p><h3>{h}</h3><p>{b}</p></div></div>' for i,kk,h,b in s["items"])
        return f"""<section class="slide trio">{head}<div class="trow">{items}</div>{footer(n)}</section>"""
    if k == "bridge":
        left = """<div class="bside"><p class="bh">IN · 채널 → 월드</p>
<div class="bi"><b>릴스 · 숏츠</b><span>밤 10시 불 피우기 15초 루틴 → 링크 스티커</span></div>
<div class="bi"><b>스토리 필터</b><span>내 캠프 네임 뽑기 → 딥링크 입장</span></div>
<div class="bi"><b>buldak.com 블로그</b><span>지금 별 수 · 접속 캠퍼 수 라이브 위젯</span></div>
<div class="bi"><b>패키지 QR</b><span>봉지 · 컵 QR → 시즌 장작 지급</span></div></div>"""
        right = """<div class="bside"><p class="bh out">OUT · 월드 → 채널</p>
<div class="bi out"><b>공유 카드</b><span>“오늘 N명과 함께 태웠어요” 9:16 · 1:1</span></div>
<div class="bi out"><b>오늘의 밤하늘</b><span>자정 30초 타임랩스 자동 렌더 → 공식 릴스</span></div>
<div class="bi out"><b>블로그 · 뉴스룸</b><span>별 마일스톤 포스트 · 신제품 선공개</span></div>
<div class="bi out"><b>캠페인 카피</b><span>공감 집계 문장 → 카피 · 숏츠 자막</span></div></div>"""
        return f"""<section class="slide bridge">{head}<div class="brow">{left}<div class="bmid">{img(s['img'],'bimg')}<p class="bcap">월드가 채널의 소재가 되고, 채널이 월드의 입구가 된다 — 매일.</p></div>{right}</div>{footer(n)}</section>"""
    if k == "wheel":
        svg, cx, cy, r = wheel_svg(s)
        nodes = ""
        for idx,(no,t,d,kpi) in enumerate(s["nodes"]):
            a = -math.pi/2 + idx*2*math.pi/6; x, y = cx + r*math.cos(a), cy + r*math.sin(a)
            lx = x + math.cos(a)*62; ly = y + math.sin(a)*100
            side = "lc" if abs(math.cos(a)) < 0.3 else ("lr" if math.cos(a) > 0 else "ll")
            nodes += f'<div class="wnum" style="left:{x-46:.0f}px;top:{y-46:.0f}px"><b>{no}</b></div>'
            nodes += f'<div class="wn {side}" style="left:{lx:.0f}px;top:{ly:.0f}px"><h3>{t}</h3><p>{d}</p></div>'
        ct, cd = s["center"]
        center = f'<div class="wc" style="left:{cx-150}px;top:{cy-150}px"><p class="k">CORE</p><h3>{ct}</h3><p>{cd}</p></div>'
        side = "".join(f'<div class="wk"><b>{no}</b><span>{t}</span><i>{kpi}</i></div>' for no,t,d,kpi in s["nodes"])
        return f"""<section class="slide wheel">{head}<div class="wrow"><div class="wstage">{svg}{nodes}{center}</div><div class="wside"><p class="bh">각 단계가 남기는 지표</p>{side}<p class="note">한 바퀴 = 한 사용자의 하루. 바퀴가 빨리 돌수록 하늘의 별이 늘고, 별이 늘수록 바퀴가 더 빨리 돈다.</p></div></div>{footer(n)}</section>"""
    if k == "split":
        rev = " rev" if s.get("rev") else ""
        fig = img(s['img']) if not s.get("cap") else f'<div class="figwrap">{img(s["img"])}<p class="figcap">{s["cap"]}</p></div>'
        return f"""<section class="slide split{rev}">{head}<div class="row">{fig}<div class="txt">{s['body']}</div></div>{footer(n)}</section>"""
    if k == "sharecard":
        stars = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F3EFE6"/>' for x,y,r in [(40,60,3),(90,30,2.5),(130,70,3.5),(180,40,2.5),(220,80,3),(260,35,2.5),(70,120,2),(150,130,2.5),(240,125,2),(110,170,2),(200,165,2.5)])
        lines = '<path d="M40 60 L90 30 L130 70 L180 40 L220 80 L260 35" fill="none" stroke="#D6FF3B" stroke-width="1.5" opacity=".9"/>'
        card916 = f"""<div class="sc916"><div class="sctop"><span>PEPPO CAMP</span><span>2026.11.02 · 캠프사이트 7</span></div>
<svg viewBox="0 0 300 200" width="300" height="200">{stars}{lines}</svg>
<p class="scbig">오늘 <b>2,431명</b>과<br>함께 태웠어요</p>
<div class="scme"><div class="scav"></div><div><b>4단계 밤바람</b><span>장작 27 · 바람 보내기 12 · 불멍 18분</span></div></div>
<div class="scbar"><i style="width:25%"></i></div><p class="scsm">내 별자리 27 / 108 · 별이 되어 하늘에 남았습니다</p>
<p class="scurl">peppoworld.com · 입장 코드 <b>NB-4K2</b></p></div>"""
        card11 = f"""<div class="sc11"><p class="scbig">오늘 <b>2,431명</b>과 함께 태웠어요</p><div class="scme"><div class="scav"></div><div><b>4단계 밤바람</b><span>장작 27 · 별자리 27/108</span></div></div><p class="scurl">peppoworld.com · <b>NB-4K2</b></p></div>"""
        right = f"""<div class="txt">
{blk("근거 01 · 참고 사례","아바타 꾸미기 캡처가 밈이 되어 릴스 330만 뷰. 공유를 만든 것은 콘텐츠가 아니라 <b>‘내 캐릭터가 찍힌 한 장’</b>이었다.")}
{blk("근거 02 · 연말 결산형 카드의 관행","음악·학습·결제 서비스의 ‘올해의 나’ 카드는 매년 자발적으로 수백만 장 공유된다. 숫자 하나 + 나 + 서비스명의 공식은 검증돼 있다.")}
{blk("근거 03 · 월드에서 ‘내가 보이는’ 유일한 지점","1인칭 로드뷰와 말 없는 캠프에서 사용자가 자기 모습을 확인하는 순간은 이 카드뿐이다. 그래서 캡처 버튼 하나로 9:16 · 1:1 두 장을 동시에 만든다.",hi=True)}
{blk("지표 연결","카드 생성 수 · 카드 속 입장 코드/UTM 경유 유입 — KPI 대시보드의 ‘공유 카드’ 두 숫자가 여기서 나온다.")}
</div>"""
        return f"""<section class="slide sharecard">{head}<div class="row"><div class="scwrap">{card916}{card11}</div>{right}</div>{footer(n)}</section>"""
    if k == "wide":
        return f"""<section class="slide wide">{head}{img(s['img'],'wideimg',s.get('imgh'))}<div class="txt grow">{s['body']}</div>{footer(n)}</section>"""
    return f"""<section class="slide text">{head}<div class="txt grow">{s['body']}</div>{footer(n)}</section>"""

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300..900&display=swap');
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#05060B;color:{PAPER};font-family:'Noto Sans KR',Arial,sans-serif;height:100%;overflow:hidden}}
#stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:center center}}
.slide{{position:absolute;inset:0;width:1920px;height:1080px;background:{NAVY};padding:96px 128px 118px;display:none;flex-direction:column;gap:30px;overflow:hidden}}
.slide.on{{display:flex}}
body.all{{overflow:auto}} body.all #stage{{position:static;transform:none!important;width:auto;height:auto}}
body.all .slide{{position:relative;display:flex;margin:0 auto 24px}}
.eyebrow{{font-size:22px;font-weight:700;letter-spacing:4px;color:{LIME}}}
h1{{font-size:112px;font-weight:900;line-height:1.02;letter-spacing:-4px}}
h2{{font-size:54px;font-weight:900;line-height:1.14;letter-spacing:-1.5px;margin-top:10px}}
h3{{font-size:30px;font-weight:900;line-height:1.22;word-break:keep-all}}
p,li,td,th{{font-size:23px;line-height:1.5;word-break:keep-all}}
header{{flex:none}}
.row{{display:flex;gap:36px;flex:1;align-items:stretch;min-height:0}}
.split.rev .row{{flex-direction:row-reverse}}
.txt{{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}} .txt.grow{{flex:1;justify-content:flex-start}}
.text .txt.grow{{justify-content:center}}
.split .txt{{justify-content:stretch}} .split .txt>.blk,.split .txt>.five,.split .txt>.btns,.split .txt>.nums{{flex:1}} .split .txt>.blk{{justify-content:center}}
.split .five,.split .btns{{justify-content:space-between}} .split .five li,.split .btns div{{flex:1;display:flex;align-items:center}} .split .btns div{{flex-direction:column;align-items:flex-start;justify-content:center}}
.split .nums{{justify-content:space-around}}
figure.img{{position:relative;margin:0;width:1020px;height:auto;flex:none;border-radius:20px;overflow:hidden;background:{CARD};border:1px solid #2A2F45;min-height:420px}}
figure.img img{{width:100%;height:100%;object-fit:cover;display:block;position:absolute;inset:0}}
figure.img figcaption{{display:none}} figure.img.missing img{{display:none}}
figure.img.missing{{border:2px dashed #3A4060;background:radial-gradient(700px 300px at 50% 110%,rgba(255,106,42,.25),transparent 60%),{CARD}}}
figure.img.missing figcaption{{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center;font-size:26px;color:{MUTE};gap:8px;padding:40px}}
figure.img.missing figcaption b{{color:{AMBER};font-size:30px;letter-spacing:3px}} figure.img.missing figcaption span{{font-size:20px;opacity:.7}}
figure.wideimg{{width:1664px;height:420px;min-height:0}}
figure.bg{{position:absolute;inset:0;width:1920px;height:1080px;border-radius:0;border:0;min-height:0}} figure.bg.missing{{border:0}} figure.bg.missing figcaption{{position:absolute;right:40px;top:40px;height:auto;width:auto;padding:14px 22px;border:2px dashed #3A4060;border-radius:14px;font-size:20px;background:rgba(5,6,11,.6)}} figure.bg.missing figcaption b{{font-size:22px}}
.cover,.statement,.divider{{padding:0}}
.scrim{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,6,11,.86) 0%,rgba(5,6,11,.55) 45%,rgba(5,6,11,.05) 100%)}}
.scrim2{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,6,11,.35),rgba(5,6,11,.88))}}
.scrim3{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,6,11,.72),rgba(5,6,11,.55) 55%,rgba(5,6,11,.92))}}
.covtxt{{position:absolute;left:112px;top:220px;width:900px;display:flex;flex-direction:column;gap:30px}}
.covtxt .sub{{font-size:34px;color:#D8D4C8;font-weight:400}}
.covbar{{position:absolute;left:0;bottom:0;width:100%;height:110px;background:rgba(5,6,11,.9);display:flex;align-items:center;justify-content:space-between;padding:0 112px}}
.covbar span{{font-size:22px;letter-spacing:2px;color:#CFCBBE}} .lime{{color:{LIME}!important;font-weight:700}}
.divtxt{{position:absolute;left:128px;top:260px;width:1500px;display:flex;flex-direction:column;gap:18px}}
.actno{{font-size:26px;font-weight:800;letter-spacing:8px;color:{LIME}}}
.divtxt h1{{font-size:150px;letter-spacing:-5px}} .divtxt .ko{{font-size:44px;font-weight:700;color:{PAPER};letter-spacing:-1px}} .line{{font-size:30px;color:#CFCBBE;line-height:1.5;font-weight:400;margin-top:10px}}
.sbar{{position:absolute;left:128px;right:128px;bottom:120px;display:flex;gap:10px}}
.sbar span{{flex:1;padding:14px 0 0;border-top:3px solid #3A4060;font-size:20px;color:#7F7F90;letter-spacing:1px;display:flex;gap:10px;align-items:baseline}}
.sbar span i{{font-style:normal;font-weight:800;font-size:18px}} .sbar span.done{{border-color:#6A6F8A;color:#B8B4C4}} .sbar span.on{{border-color:{LIME};color:{LIME};font-weight:800}}
.statement .abs{{position:absolute;left:128px;top:96px}}
.sttxt{{position:absolute;left:128px;bottom:200px;width:1500px;display:flex;flex-direction:column;gap:30px}}
.sttxt .sub{{font-size:30px;color:#E6E1D5;line-height:1.5}}
.tags{{display:flex;gap:14px;flex-wrap:wrap}} .tags span{{padding:10px 22px;border-radius:999px;border:1.5px solid rgba(243,239,230,.4);font-size:22px;font-weight:700}}
.foot{{position:absolute;left:128px;bottom:48px;font-size:18px;letter-spacing:3px;color:{MUTE}}} .statement .foot,.divider .foot{{color:#CFCBBE}}
.cards3,.cards4{{display:flex;gap:26px}} .cards3.grow,.cards4.grow{{flex:1}} .cards3>.card,.cards4>.card{{flex:1;display:flex;flex-direction:column;gap:12px;padding:32px 30px;border-radius:24px;background:{CARD};border:1px solid #2A2F45}}
.cards3.tight>.card{{padding:28px 30px;gap:10px}} .cards3.big>.card{{padding:44px 40px;gap:18px}} .cards3.big h3{{font-size:34px}} .cards3.big p{{font-size:24px}} .cards3.tight p,.cards4 p{{font-size:22px}} .cards3.grow>.card,.cards4.grow>.card{{justify-content:center}}
.card.hi{{background:#2A1A12;border-color:{FIRE}}} .k{{font-size:20px!important;font-weight:800;letter-spacing:3px;color:{AMBER}}} .card.hi .k,.blk.hi .k{{color:{LIME}}}
.card p,.blk p{{color:#D6D2C6}} .j{{color:{AMBER}!important;font-weight:700;margin-top:auto}}
.keep{{padding:24px 30px;border-radius:16px;background:{CARD};border:1px solid #2A2F45;font-size:23px;color:#D6D2C6;line-height:1.6}} .keep b{{color:{LIME};margin-right:14px}}
.blk{{padding:20px 26px;border-radius:16px;background:{CARD};border:1px solid #2A2F45;display:flex;flex-direction:column;gap:8px}} .blk.hi{{background:#2A1A12;border-color:{FIRE}}} .blk p{{font-size:23px}}
.t{{width:100%;border-collapse:collapse}} .t th{{text-align:left;padding:11px 18px;background:#1E2338;font-weight:800;color:{PAPER};font-size:21px}}
.t td{{padding:10px 18px;border-top:1px solid #2A2F45;color:#D6D2C6;font-size:21px;vertical-align:top}} .t td.b{{font-weight:800;color:{PAPER}}} .t td.m{{color:{AMBER};font-weight:700}}
.t.sm td,.t.sm th{{font-size:20px;padding:10px 14px}}
.nrhead{{display:grid;grid-template-columns:1fr 70px 1fr;gap:0 20px;padding:0 26px 10px}} .nrhead span{{font-size:22px;font-weight:800;letter-spacing:4px;color:{MUTE}}} .nrhead span:last-child{{color:{LIME}}}
.nrlist{{display:flex;flex-direction:column;gap:9px;flex:1}} .nrow{{display:grid;grid-template-columns:1fr 70px 1fr;gap:0 20px;align-items:center;padding:0 26px;border-radius:14px;background:{CARD};border:1px solid #2A2F45;flex:1}}
.nd{{display:flex;gap:18px;align-items:center}} .nd b{{font-size:17px;letter-spacing:2px;color:{AMBER};width:52px;flex:none}} .nd p,.rs p{{font-size:20px;line-height:1.3}} .rs p{{color:{PAPER};font-weight:700}} .nd p{{color:#D6D2C6}} .narr{{text-align:center;color:#5A5F7A;font-size:26px}}
.nums{{display:flex;flex-direction:column;gap:16px}} .nums div{{display:grid;grid-template-columns:270px 1fr;align-items:center;gap:16px}} .nums b{{font-size:60px;font-weight:900;color:{LIME};line-height:1;letter-spacing:-2px;white-space:nowrap}} .nums b i{{font-style:normal;font-size:40px;margin:0 4px}} .nums span{{font-size:22px;color:#D6D2C6;line-height:1.45}}
.note{{padding:16px 22px;border-radius:14px;background:{CARD};border:1px solid #2A2F45;font-size:21px;color:#D6D2C6}} .note.hi{{background:#2A1A12;border-color:{FIRE};color:{PAPER}}} .note b{{color:{PAPER}}}
.five{{list-style:none;display:flex;flex-direction:column;gap:12px}} .five li{{padding:14px 20px;border-radius:14px;background:{CARD};border:1px solid #2A2F45;font-size:22px;color:#D6D2C6}} .five li b{{color:{LIME};margin-right:14px;font-size:23px}}
.btns{{display:flex;flex-direction:column;gap:12px}} .btns div{{padding:14px 20px;border-radius:14px;background:{CARD};border:1px solid #2A2F45;display:flex;flex-direction:column;gap:3px}} .btns b{{font-size:26px;color:{PAPER}}} .btns span{{font-size:21px;color:#D6D2C6}}
.steps{{display:flex;gap:20px}} .steps.grow{{flex:1}} .steps div{{flex:1;display:flex;flex-direction:column;gap:8px;padding:22px 18px;border-radius:16px;background:{CARD};border:1px solid #2A2F45;font-size:23px;font-weight:800;justify-content:center}} .steps div b{{color:{AMBER};font-size:19px;letter-spacing:3px}} .steps div span{{font-size:19px;font-weight:400;color:#D6D2C6}} .steps div.hi{{background:#2A1A12;border-color:{FIRE}}}
.cols2{{display:flex;gap:40px}} .cols2.grow{{flex:1}} .cols2>div{{flex:1;display:flex;flex-direction:column;gap:14px}} .list{{padding-left:30px;display:flex;flex-direction:column;gap:7px;color:#D6D2C6}} .list li{{font-size:21px}}
.quad .row{{align-items:stretch}} figure.qmain{{width:960px;height:auto}} .qcol{{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}}
.qi{{display:flex;gap:14px;align-items:stretch;flex:1}} .qimg figure.img{{width:300px;height:100%;min-height:150px;border-radius:14px}} .qimg{{flex:none;display:flex}} .qi .blk{{flex:1;justify-content:center}} .qi .blk p{{font-size:21px}}
.qimg figure.img.missing figcaption{{font-size:18px;padding:12px;gap:4px}} .qimg figure.img.missing figcaption b{{font-size:20px}} .qimg figure.img.missing figcaption span{{display:none}}
.trow{{display:flex;gap:26px;flex:1}} .ti{{flex:1;display:flex;flex-direction:column;gap:16px}} figure.timg{{width:100%;flex:1;height:auto;min-height:300px;border-radius:18px}} .ti .card{{flex:none;display:flex;flex-direction:column;gap:10px;padding:28px 30px;border-radius:22px}}
.brow{{display:flex;gap:28px;align-items:stretch;flex:1}} .bside{{width:420px;flex:none;display:flex;flex-direction:column;gap:12px}} .bmid{{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}}
figure.bimg{{width:100%;flex:1;height:auto;min-height:400px;border-radius:18px}} .bcap{{text-align:center;font-size:22px;color:#D6D2C6}}
.bh{{font-size:20px;font-weight:800;letter-spacing:3px;color:{LIME}}} .bh.out{{color:{AMBER}}}
.bi{{padding:14px 18px;border-radius:14px;background:{CARD};border:1px solid #2A2F45;display:flex;flex-direction:column;gap:3px;flex:1;justify-content:center}} .bi b{{font-size:24px}} .bi span{{font-size:19px;color:#D6D2C6;line-height:1.4}} .bi.out{{border-color:#5A3A20;background:#1F1A14}}
.t.br td.in,.t.br td.out{{font-weight:900;font-size:26px;color:{LIME};vertical-align:middle;text-align:center;letter-spacing:2px}} .t.br td.out{{color:{AMBER}}} .t.br td.in span,.t.br td.out span{{display:block;font-size:16px;color:{MUTE};letter-spacing:0;font-weight:600}}
.t.br td,.t.br th{{font-size:19px;padding:9px 14px}} .t.br td.b{{font-size:20px}}
.idrow{{display:flex;gap:26px;flex:1;align-items:stretch}} .idcol{{width:470px;flex:none;display:flex;flex-direction:column;gap:12px}} .idmid{{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}}
.idh{{font-size:19px;font-weight:800;letter-spacing:3px;color:{AMBER}}} .idh.out{{color:{LIME}}}
.idc{{flex:1;padding:14px 22px;border-radius:14px;background:{CARD};border:1px solid #2A2F45;display:flex;flex-direction:column;justify-content:center;gap:2px}} .idc b{{font-size:28px}} .idc span{{font-size:20px;color:#D6D2C6}} .idc.out{{background:#2A1A12;border-color:{FIRE}}}
figure.idimg{{width:100%;flex:1;height:auto;min-height:300px;border-radius:18px}}
.idverb{{display:flex;align-items:center;gap:26px;padding:18px 28px;border-radius:16px;background:#1E2338;border:1px solid #2A2F45}} .idverb h3{{font-size:52px;color:{LIME};letter-spacing:-2px}} .idverb p{{font-size:21px;color:#D6D2C6}} .idverb .k{{width:110px}}
.idfoot{{padding:20px 28px;border-radius:16px;background:#2A1A12;border:1px solid {FIRE};font-size:23px;color:{PAPER};line-height:1.55}} .idfoot b{{color:{LIME};margin-right:16px;font-size:26px}}
.wrow{{display:flex;gap:26px;flex:1;align-items:stretch}} .wstage{{position:relative;width:1180px;height:860px;flex:none;margin-top:-26px}} .wsvg{{position:absolute;left:0;top:0}}
.wnum{{position:absolute;width:92px;height:92px;display:flex;align-items:center;justify-content:center}} .wnum b{{font-size:30px;font-weight:900;color:{PAPER};letter-spacing:1px}}
.wn{{position:absolute;width:225px;display:flex;flex-direction:column;gap:3px}} .wn.lr{{transform:translate(0,-50%)}} .wn.ll{{transform:translate(-100%,-50%);text-align:right}} .wn.lc{{transform:translate(-50%,-50%);text-align:center}}
.wn h3{{font-size:28px}} .wn p{{font-size:19px;color:#B8B4C4;line-height:1.35}}
.wc{{position:absolute;width:300px;height:300px;border-radius:50%;text-align:center;display:flex;flex-direction:column;gap:6px;align-items:center;justify-content:center;padding:30px}} .wc h3{{font-size:48px;color:{PAPER};letter-spacing:-2px;text-shadow:0 2px 14px rgba(0,0,0,.5)}} .wc p{{font-size:19px;color:#FFF1E0;line-height:1.35}} .wc .k{{color:#FFE9B0}}
.wside{{flex:1;display:flex;flex-direction:column;gap:10px;min-width:0;justify-content:center}} .wk{{display:grid;grid-template-columns:40px 150px 1fr;align-items:center;gap:12px;padding:12px 16px;border-radius:12px;background:{CARD};border:1px solid #2A2F45}} .wk b{{color:{AMBER};font-size:16px;letter-spacing:2px}} .wk span{{font-size:21px;font-weight:800}} .wk i{{font-style:normal;font-size:18px;color:{LIME}}}
.kpiwrap{{display:flex;flex-direction:column;gap:14px}} .kpiwrap.grow{{flex:1}} .tier{{display:flex;gap:16px;align-items:stretch;flex:1}}
.tname{{width:190px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:4px;padding:16px 20px;border-radius:16px;background:#1E2338}} .tname b{{font-size:30px;font-weight:900}} .tname span{{font-size:18px;color:{MUTE}}}
.tiles{{flex:1;display:flex;gap:14px}} .tile{{flex:1;display:flex;flex-direction:column;gap:6px;padding:18px 20px;border-radius:16px;background:{CARD};border:1px solid #2A2F45;justify-content:center}}
.tile b{{font-size:30px;font-weight:900;color:{PAPER};letter-spacing:-1px}} .tile span{{font-size:19px;color:#D6D2C6;line-height:1.4}} .tile i{{font-style:normal;font-size:17px;color:{AMBER};letter-spacing:1px;margin-top:6px}}
.tile.hi{{background:#2A1A12;border-color:{FIRE}}} .tile.hi b{{color:{AMBER}}} .tile.m{{border-color:{LIME}}} .tile.m b{{color:{LIME}}} .tile.m i{{color:{LIME}}}
#script{{display:none;position:fixed;right:0;bottom:0;width:50vw;height:50vh;z-index:8;background:rgba(8,10,18,.94);border-top:2px solid {LIME};border-left:2px solid {LIME};padding:28px 34px 40px;overflow:auto;font-size:clamp(14px,1.25vw,20px);line-height:1.7;color:{PAPER}}}
body.sc #script{{display:block}} .sch{{display:flex;gap:16px;align-items:baseline;margin-bottom:14px}} .sch span{{font-size:.8em;letter-spacing:3px;color:{LIME};font-weight:800}} .sch em{{font-style:normal;font-size:.85em;color:{AMBER}}} #script p{{font-size:1em;line-height:1.75}}
.scblock{{display:none}} body.all.sc .scblock{{display:block;width:1920px;margin:-14px auto 30px;padding:22px 128px;background:#0B0D16;border-left:4px solid {LIME}}} .scblock b{{font-size:18px;letter-spacing:3px;color:{LIME};margin-right:16px}} .scblock em{{font-style:normal;font-size:18px;color:{AMBER}}} .scblock p{{font-size:22px;line-height:1.7;margin-top:8px}}
.figwrap{{display:flex;flex-direction:column;gap:10px;flex:none;width:1020px}} .figwrap figure.img{{flex:1;width:100%}} .figcap{{font-size:19px;color:{MUTE};letter-spacing:.5px}}
.t.ms td,.t.ms th{{font-size:19px;padding:9px 14px}} .t.ms td.hi{{color:{LIME};font-weight:700}} .t.ms td.b.hi{{color:{AMBER}}}
.scwrap{{display:flex;gap:26px;align-items:flex-end;flex:none}}
.sc916{{width:372px;height:662px;border-radius:28px;background:linear-gradient(180deg,#141A33 0%,#0E1220 55%,#2A1A12 100%);border:1px solid #3A4060;padding:26px 30px;display:flex;flex-direction:column;gap:14px;box-shadow:0 30px 60px rgba(0,0,0,.5)}}
.sctop{{display:flex;justify-content:space-between;font-size:14px;letter-spacing:2px;color:{AMBER};font-weight:800}} .sctop span:last-child{{color:{MUTE};letter-spacing:0;font-weight:500}}
.sc916 svg{{width:100%;height:auto}} .scbig{{font-size:38px;font-weight:900;line-height:1.15;letter-spacing:-1px}} .scbig b{{color:{LIME}}}
.scme{{display:flex;gap:14px;align-items:center}} .scav{{width:56px;height:56px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#FFD9B0,#D98A55 70%);border:3px solid {FIRE};flex:none}} .scme b{{font-size:21px;display:block}} .scme span{{font-size:15px;color:#CFCBBE}}
.scbar{{height:10px;border-radius:5px;background:#2A2F45;overflow:hidden}} .scbar i{{display:block;height:100%;background:linear-gradient(90deg,{FIRE},{LIME})}} .scsm{{font-size:15px;color:#CFCBBE}}
.scurl{{margin-top:auto;font-size:15px;color:{MUTE};letter-spacing:1px}} .scurl b{{color:{PAPER};letter-spacing:3px}}
.sc11{{width:300px;height:300px;border-radius:24px;background:linear-gradient(160deg,#141A33,#2A1A12);border:1px solid #3A4060;padding:24px;display:flex;flex-direction:column;gap:14px;box-shadow:0 20px 40px rgba(0,0,0,.45)}} .sc11 .scbig{{font-size:27px}} .sc11 .scav{{width:44px;height:44px}} .sc11 .scme b{{font-size:18px}} .sc11 .scme span{{font-size:14px}}
#nav{{position:fixed;right:18px;bottom:14px;font:14px/1 Arial;color:#777;letter-spacing:1px;z-index:9}}
#pdfbtn{{position:fixed;right:18px;top:14px;z-index:9;padding:10px 16px;border-radius:999px;background:rgba(214,255,59,.92);color:#0E1220;font:700 14px/1 'Noto Sans KR',Arial;letter-spacing:1px;border:0;cursor:pointer}}
@media print{{
 @page{{size:A4 landscape;margin:0}}
 html,body{{height:auto!important;overflow:visible!important;background:{NAVY}}}
 #nav,#pdfbtn,#script,.scblock{{display:none!important}}
 body.all #stage{{display:block;transform:none!important}}
 html,body{{width:1122px!important}}
 body.all #stage{{width:1122px;margin:0}}
 body.all .slide{{display:flex;zoom:0.5844;margin:139px 0 0!important;page-break-after:always;break-after:page}}
 body.all .slide:last-child{{page-break-after:auto;break-after:auto}}
}}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')];let i=Math.max(0,Math.min(slides.length-1,(parseInt(location.hash.slice(1))||1)-1));
const all=location.search.includes('all');if(all)document.body.classList.add('all');
var show=function(){slides.forEach((s,k)=>s.classList.toggle('on',all||k===i));document.getElementById('nav').textContent=(i+1)+' / '+slides.length+'   ←→ 이동 · A 전체보기 · S 스크립트';if(!all)history.replaceState(null,'','#'+(i+1));}
function fit(){const s=Math.min(innerWidth/1920,innerHeight/1080);document.getElementById('stage').style.transform=`translate(-50%,-50%) scale(${s})`;}
addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){i=Math.min(slides.length-1,i+1);show()}if(e.key==='ArrowLeft'||e.key==='PageUp'){i=Math.max(0,i-1);show()}if(e.key==='Home'){i=0;show()}if(e.key==='End'){i=slides.length-1;show()}if(e.key==='a'||e.key==='A'){location.search=all?'':'?all'}});
document.getElementById('pdfbtn').addEventListener('click',()=>{document.body.classList.add('all');slides.forEach(s=>s.classList.add('on'));setTimeout(()=>window.print(),300);});
addEventListener('afterprint',()=>{if(!all){document.body.classList.remove('all');show();}});
const SC=__SCRIPTS__;let scOn=false;const sp=document.getElementById('script');
function renderScript(){const d=SC[i+1]||['',''];sp.innerHTML='<div class="sch"><span>SCRIPT · '+(i+1)+' / '+slides.length+'</span>'+(d[0]?'<em>'+d[0]+'</em>':'')+'</div><p>'+d[1]+'</p>';}
addEventListener('keydown',e=>{if(e.key==='s'||e.key==='S'){scOn=!scOn;document.body.classList.toggle('sc',scOn);renderScript();}});
const _show=show;show=function(){_show();if(scOn)renderScript();};
addEventListener('resize',fit);fit();show();
if(all&&location.search.includes('print=1')){setTimeout(()=>window.print(),900);}
"""

out = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>PEPPO WORLD 리뉴얼 제안서 — 밤의 캠프, 불 앞의 월드</title>
<meta name="viewport" content="width=device-width,initial-scale=1"><style>{CSS}</style></head><body>
<button id="pdfbtn" title="A4 가로 PDF로 저장">PDF 다운로드</button>
<div id="stage">{''.join(render(s, n+1) + f'<div class="scblock"><b>SCRIPT · {n+1:02d}</b>' + (f'<em>{SCRIPTS[n+1][0]}</em>' if SCRIPTS[n+1][0] else '') + f'<p>{SCRIPTS[n+1][1]}</p></div>' for n, s in enumerate(slides))}</div><div id="nav"></div><div id="script"></div><script>{JS.replace('__SCRIPTS__', json.dumps({k:[a,b] for k,(a,b) in SCRIPTS.items()}, ensure_ascii=False))}</script></body></html>"""
open("index.html","w",encoding="utf-8").write(out)
print("slides:", len(slides))
