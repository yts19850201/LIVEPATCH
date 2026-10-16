from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parent.parent
brief=ROOT/'docs/design.md'
old=brief.read_text(encoding='utf-8-sig')
evaluation=old[old.index('## 16. 최종 검수 기준'):old.index('## 17.')]
content='''# LIVEPATCH 디자인 브리프

기준일 2026-10-16 · 디자인 기준 v1.0 · 사용자 단계 승인 대기.
제품 기능·출시 범위·과금·권한·승인·복원은 사업기획서 27장(v5.7)을 따른다. 이 문서는 시각·콘텐츠·Figma 제작 기준이다. 현재 사용자 요청 → 이 문서 → style.md 순서로 디자인 판단에 적용한다.

## 1. 프로젝트 기본 정보

- 프로젝트명: LIVEPATCH.
- 서비스: 기존 웹사이트의 고칠 곳을 선택하고 말이나 터치로 변경을 요청한 뒤, 미리보기·검증·승인을 거쳐 운영에 반영하는 웹 서비스.
- 주요 사용자: 지원 환경의 사이트 소유자·관리자 중 비개발자. 운영팀은 회원·사이트·작업·결제·지원·장애를 관리한다.
- 핵심 행동: 선택 → 말하기 → 의도·최대 비용 확인 → 미리보기 → 검증 → 패스키 승인 → 반영·사후 확인 → 필요 시 복원 요청.
- 문제: 작은 사이트 변경에도 기술 설명·외주 요청·반영 확인이 필요한 부담을 줄인다. 시간·원가·무개입 해결률은 파일럿에서 측정한다.
- 출력: 기존 Figma Design 파일의 편집 가능한 레이어·변수·텍스트/효과 스타일.
- Figma: https://www.figma.com/design/VwuyN75CQK9Kn0ZyIVmF4S/LIVEPATCH . 기존 0:1 페이지는 보존한다.
- 이번 제작 범위: PC 1920px. 공식 웹 콘텐츠 최대 1440px·중앙 정렬, 기본 좌우 240px. Studio는 전체 가용폭·별도 작업 공간 규격.
- 구현 환경: LIVEPATCH 앱 프레임워크 미확정. 지원 대상 사이트는 검증된 GitHub 정적 HTML/CSS 템플릿·파이프라인 1종이며 앱 자체의 기술 선택과 구분한다.
- 최초 MVP: 44페이지+19공용 오버레이. 58개 ID는 내부 통합, 52개는 후속. 베타는 36페이지+17오버레이.
- 사용자는 고객 1인·사이트 1개. 모바일 Studio·CMS/SFTP·Mode C·팀·파트너·전문가 판매는 후속.

### 단계별 진행과 승인

1. Foundations: 브리프·CSS 토큰 정리, Figma 기초 변수·스타일·1920px 검토 보드 작성.
2. Components: 1단계 결과에 대한 사용자 진행 승인 후 공용 컴포넌트·상태·Variant 제작.
3. Studio: 2단계 결과에 대한 사용자 진행 승인 후 C13 및 통합 K1~K7 핵심 흐름 제작.

단계 완료 시 간략히 보고하고 다음 단계 승인을 받는다. 자체 검수 통과를 사용자 승인으로 기록하지 않는다. 이번 1단계에서는 Components·Studio 화면과 모바일·태블릿 프레임을 생성하지 않는다.

### 가정과 미확정 항목

- 가격 9,900원·100C, 하루 생성 10회는 현재 가설/작업 기준이며 상용 게이트 통과 전 판매 실적으로 표현하지 않는다.
- STT/PG, 원음·개인정보·스냅샷 보존, OpenAPI·실제 데이터 계약, 앱 프레임워크·공수는 미확정이다.
- 디자인 샘플 값은 실측 고객 데이터·테스트 통과·운영 배포 완료와 구분한다.
- 현재 콘셉트·토큰은 첫 단계 검토안이며 사용자 최종 승인 패턴이 아니다.

## 2. 실제 콘텐츠와 용어

| 용도 | 한국어 콘텐츠 |
|---|---|
| 공식 웹 핵심 제목 | 홈페이지 수정, 이제 말로 하세요. |
| 핵심 설명 | 고칠 곳을 고르고 말해 주세요. 변경안을 확인한 뒤 직접 반영합니다. |
| 공식 웹 주요 행동 | 데모로 바로 해보기 |
| Studio 기본 행동 | 말로 바꾸기 |
| 확인 카드 | 이렇게 바꿀까요? / 예, 미리보기 만들기 / 다시 말하기 |
| 샘플 변경 | 안내 문구 ‘여름 운영 안내’ → ‘가을 운영 안내’ |
| 비용 표시 | 최대 1 크레딧 · 미리보기에서는 예약만 합니다. |
| 반영 확인 | 도메인·변경·최대 비용 확인 / 길게 눌러 반영 / 본인 확인 필요 |
| 결과 불명 | 반영 결과를 확인하고 있습니다. 다시 반영하지 말고 잠시 기다려 주세요. |
| 복원 안내 | 복원 가능 기간과 후속 변경을 확인한 뒤 요청할 수 있습니다. |
| 원본 변경 방식 | 원본 수정 / CMS 필드 변경 / 표시 패치 — 후속 모드는 MVP 선택지에 비노출 |

메뉴는 고객의 사이트·작업·배포/복원·크레딧·구독·문의 맥락으로 구성한다. 같은 단계에 ‘적용/반영/배포’를 섞지 않고 고객 행동은 ‘반영’, 기술 증빙은 ‘배포’로 구분한다.

## 3. 참고 자료와 재사용 범위

| 자료 | 역할 | 가져올 것 | 변형/제외할 것 | 적용 위치 |
|---|---|---|---|---|
| 사업기획서 27장·화면 계약 v5.7 | 제품 정본 | 현재 범위·승인·과금·복원·화면 ID | 이전 α/β 분류와 후속 기능은 현재 메뉴로 복사하지 않음 | 전 플랫폼 |
| 기존 PNG·HTML v5.6-r2 | 구조 참고 | 번호 선택·마이크·확인 카드·비교 흐름 | 이전 치수·문구를 그대로 최종 디자인으로 사용하지 않음 | Studio |
| docs/style.md | 스타일 기준 | 한국어 위계·뉴트럴·구획·실제 콘텐츠 | 홍보용 간격·Hero를 업무 화면에 일괄 적용하지 않음 | 전 플랫폼 |
| 기존 기초 CSS | 구현 기반 | 역할별 변수·간격·형태·포커스·모션 | 검정 Primary 의미·저대비 muted·전역 대상 선택자 정리 | Foundations |

이번 단계에서 외부 사이트를 새로 분석하거나 복제하지 않는다. 외부 참고가 필요한 다음 단계에서만 목적별로 추가한다.

## 4. 디자인 콘셉트

- 작업 콘셉트: 고칠 곳에 집중하는 도구.
- 한 문장 방향: 고객 사이트가 화면의 중심이 되고, 번호·한국어 확인 문구·작은 음성 도구가 수정 과정을 안내한다.
- 핵심 키워드: 명확함·통제감·실무 밀도.
- 대표 모티프: 번호가 붙은 선택 경계와 변경 전후의 짧은 확인 문장.
- 피할 인상: 추상 AI 서비스, 장식적인 SaaS, 알록달록한 편집 도구.
- 대비·정보 위계는 글자·선·여백으로 만들고 강조색은 선택/다음 행동에 제한한다.

## 5. 플랫폼 구조와 우선순위

| 플랫폼 | 구조 | 우선 정보 | 구성 방식 |
|---|---|---|---|
| 공식 웹 | 소개→샘플 체험→지원 범위→이용 방식→가격/정책→가입 | 무엇을 수정할 수 있는지, 승인 전 실제 사이트는 미변경 | 분할 Hero·제품 미리보기·선형 과정·FAQ |
| 고객 콘솔 | 사이트 허브→연결→Studio→작업/복원→구독/지원 | 현재 사이트·연결 상태·다음 작업 | 구획·목록·탭·타임라인 |
| Studio | 상단 맥락→사이트 캔버스→선택 번호→음성 Dock→확인/검증/승인 | 선택한 곳·원본 수정 여부·다음 행동 하나 | 전체폭 작업 공간·필요한 패널만 노출 |
| 관리자 | 작업/장애 관제→대상 상세→조치→감사 | 위험·실행 상태·근거·권한 | 테이블·필터·상세 작업대 |

전체 디자인 순서는 Foundations→Components→Studio→연결→고객 콘솔→관리자→공식 웹→결제→인계다. 현재 사용자 승인 범위는 1단계까지다.

## 6. 공식 웹 Hero 기준

좌측 한국어 메시지, 우측 실제 Studio 시연 구조를 기본으로 한다. 제목은 최대 2~3줄, 주요 행동은 ‘데모로 바로 해보기’ 하나를 우선한다. 샘플 체험·지원 환경 제한·승인 후 반영의 의미가 첫 화면에서 보이도록 한다. 실제 실적이 없는 고객 수·속도·비용 절감 통계, 추상 구체·로봇·그라데이션은 사용하지 않는다. Hero 화면은 후속 승인 단계에서 제작한다.

## 7. 브랜드와 색상

| 역할 | CSS 토큰 | 값 | 사용 |
|---|---|---|---|
| 주요 행동/선택 | --project-primary | #2563EB | 현재 단계의 주요 행동 하나, 선택 경계 |
| hover/pressed | --project-primary-hover / --project-primary-active | #1D4ED8 / #1E40AF | 조작 상태 |
| 약한 선택 면 | --project-primary-soft | #EFF6FF | 선택·포커스 맥락 |
| 강한 제목 | --color-text-strong | #111317 | 주요 제목·핵심 값 |
| 본문 | --color-text | #3B4048 | 일반 내용 |
| 보조 글자 | --color-text-muted | #555C66 | 안내·메타, 흰색/연한 배경 대비 검수 |
| 바탕/면 | --color-bg / --color-bg-subtle | #FFFFFF / #F7F8FA | 페이지·보조 구획 |
| 위험 | --color-error | #C93636 | 위험 조치·차단 사유 |

별도 장식 Accent는 추가하지 않는다. 기존 accent 토큰은 Primary의 호환 별칭으로 유지한다. success/warning/info는 중립 상태 문구와 아이콘 중심이며 초록·주황 배지를 기본 생성하지 않는다. 고객 사이트의 색은 앱의 강조색 면적 평가에서 제외한다. 강한 색의 일정 비율을 채우려고 장식하지 않는다.

## 8. 타이포그래피

기본은 Pretendard Variable, Figma에서는 사용 가능함을 확인한 Pretendard Regular/Medium/SemiBold/Bold를 사용한다. 웹 폰트 로딩은 앱 환경 결정 후 별도 연결하며 선언만으로 로딩 완료를 주장하지 않는다. 디스플레이 전용 폰트는 추가하지 않는다.

| 역할 | PC 크기/행간 | 굵기 | 사용 |
|---|---|---|---|
| Display | 48/60px | 700 | 공식 웹 메시지·Foundations 표제 |
| H1 | 32/42px | 700 | 페이지 제목 |
| H2 | 24/34px | 600 | 섹션 제목 |
| H3 | 20/28px | 600 | 패널 제목 |
| H4 | 18/26px | 600 | 하위 제목 |
| Body Large | 18/28px | 400 | 핵심 설명 |
| Body | 16/26px | 400 | 본문 |
| Body Small | 14/22px | 400 | 정보 밀도가 높은 표·보조 내용 |
| Caption | 13/20px | 400 | 메타·짧은 도움말 |
| Label | 14/20px | 600 | 버튼·컨트롤 |

한글 제목은 keep-all을 우선하고 URL·코드는 넘침 대안을 제공한다. 숫자는 tabular-nums. 본문을 작게 줄여 공간을 만들지 않는다. Figma 스타일과 CSS 크기를 동일 역할로 연결한다.

## 9. 레이아웃과 형태 토큰

- PC 기준 화면: 1920px. 공식 웹 최대 콘텐츠 1440px·중앙, 좌우 240px. 12컬럼·24px gap이면 컬럼 98px.
- 일반 읽기 폭: 736px, 넓은 정책/표 880px. 1440px 전체를 본문 한 줄 길이로 쓰지 않는다.
- Studio: 전체 가용폭, 상단 56px, Inspector 기본 380px(360~420), Mini Dock 접힘 320×56/펼침 380, 안전 여백 16px.
- 공식 웹 헤더: 80px. Studio 상단 바와 같은 토큰으로 묶지 않는다.
- 기본 간격: 4/8/12/16/20/24/32/40/48/64/80/96px. 업무 화면은 8/12/16/24, 홍보 섹션은 72/88/104 중심.
- radius: control 10px, card 12px, media 16px, feature 20px. pill은 번호·태그 등 의미 있는 경우만 사용한다.
- 기본 카드: border 또는 그림자 없음. 떠 있는 Dock·Popover·Dialog에만 효과 스타일을 사용한다.
- 주요 조작 최소 높이: 44px. 표 보조 조작도 포커스·포인터 영역을 별도로 확보한다.

## 10. 다음 단계 컴포넌트 목록

2단계 승인 전에는 아래 컴포넌트를 생성하지 않는다. 먼저 Button·IconButton·Field·Status·Toast·Dialog·Sheet·Tab·Table 등 공통 의존 요소를 만들고, SelectionBoundary·NumberMarker·VoiceDock·Transcript·IntentCard·ValidationSummary·PublishConfirm·RollbackStatus 등 Studio 요소로 확장한다. 기본/hover/pressed/focus/disabled/loading, 기능별 성공·오류·결과 불명 상태를 정의한다. Variant 축이 과도하면 하위 컴포넌트로 분리한다.

## 11. 이미지와 아이콘

이번 Foundations에는 장식 이미지가 필요하지 않다. 후속 Studio는 고객 사이트를 설명하는 현실적인 한국어 샘플을 사용하고 실사이트 배포 결과로 오인시키지 않는다. 아이콘은 Figma 라이브러리에서 사용 가능한 한 세트를 확인한 뒤 동일 선 굵기로 적용한다. 승인된 로고 파일은 없으므로 LIVEPATCH 텍스트 워드마크는 작업용이며 최종 브랜드 로고로 간주하지 않는다.

## 12. 인터랙션과 AX 상태

- 기본 모션: 빠름 160ms, 일반 240ms. 전시용 스크롤 등장 모션은 기본 비활성.
- 음성 시작·듣는 중·인식 결과·의도 확인·미리보기 생성은 별도 단계와 이벤트다.
- 발화 금액·날짜·전화번호는 정규화 결과를 확인한다. 마이크 거부·오인식은 후보 선택·터치·텍스트로 이어간다.
- 확인 버튼이나 1초 길게 누르기는 의도 조작이며 패스키·서버 권한·검증·해시 확인을 대체하지 않는다.
- UNKNOWN은 ‘확인 중’, FAILED는 ‘실패’로 구분하고 실제 확인 전 완료를 표시하지 않는다.
- 보류·차감·반환은 색으로만 구분하지 않는다. 미리보기 HOLD→VERIFIED COMMIT 정책을 유지한다.
- 닫기·작업 취소·운영 복원은 서로 다른 행동이다.
- prefers-reduced-motion에서는 불필요한 모션을 제거한다.

## 13. 반응형 범위

이번 Figma 제작·검수는 PC 1920px만 한다. 모바일·태블릿 프레임은 별도 요청과 승인 후 생성한다. Foundations의 Auto Layout은 텍스트 길이 변경과 필요한 좁은 컨테이너 상황을 고려하되, 이를 모바일 시안 완료로 기록하지 않는다. 제품 구현 단계의 1440/1280/1024/768/390 및 360 추가 점검 요구는 유지한다. 모바일 Studio가 MVP에서 제외돼도 공식 웹·조회·문의의 반응형 기능을 삭제하지 않는다.

## 14. 접근성과 스타일 격리

- 일반 본문·보조 글자는 실제 배경 기준 4.5:1을 프로젝트 기준으로 검수한다. 비활성·장식은 별도 역할로 구분한다.
- 포커스: Primary 3px, offset 2px. 상태는 텍스트·선 형태·아이콘 병행.
- CSS는 [data-livepatch-app] 아래에만 적용한다. 고객 사이트 html/body/제목/이미지에 기본 리셋·앱 토큰을 주입하지 않는다.
- 실행 구조에서는 편집 레이어를 iframe/Shadow DOM 등 적절한 경계에 격리한다. 이 단계는 격리 구현 완료가 아니다.
- 코드에서는 루트 16px 환산을 기준으로 rem을 사용한다. 외부 사이트 컨텍스트의 rem·z-index를 그대로 가정하지 않고 별도 검증한다.
- Figma는 시각·상태·편집 구조 검수, 실제 키보드·음성·패스키·브라우저 동작은 구현 검수로 나눈다.

## 15. 디자인 결정 요약과 금지 패턴

- 콘셉트: 고칠 곳에 집중하는 도구.
- 핵심 행동: 선택·요청·확인·반영.
- 시각 기준: 중립 크롬·파랑 선택·위험 빨강·한국어 위계.
- 모티프: 번호 선택 경계·짧은 변경 확인 문장.
- 이번 수정 파일: docs/design.md, src/styles/design-tokens.css. 토큰 내보내기·Figma 상태 기록은 정리 폴더에 날짜 접미사로 저장.
- 이번 Figma 범위: Foundations 변수·타입/효과 스타일·1920px 검토 보드. 컴포넌트/Studio는 다음 승인 대상.
- 금지: 임의 실적·고객 후기, 추상 AI Hero, 반복 3열 카드, 모든 상태의 색상 배지화, 긴 본문 축소, 기존 PNG를 최종 검수 증거로 사용.

'''
brief.write_text(content+evaluation+'''## 17. 완료와 승인 기록

- Foundations 작성일: 2026-10-16.
- 현재 단계: Foundations 제작 및 자체 검수 중.
- 사용자 승인: 대기. Components 진행 승인 전 생성 금지.
- Figma 노드·변수·스타일 ID와 검수 결과: 정리 폴더의 Foundations 상태 기록으로 관리.
- style.md 승인 패턴 추가: 사용자 승인 전 추가하지 않음.
''',encoding='utf-8')

cssfile=ROOT/'src/styles/design-tokens.css'
css=(ROOT/'정리/Foundations_수정전백업_261016/design-tokens_수정전_261016.css').read_text(encoding='utf-8-sig')
css=css[:css.index('\n*,')]
css=css.replace('Personal design foundation','LIVEPATCH design foundation v1.0 · 2026-10-16')
css=css.replace('아래 Project theme 영역만 수정합니다.','역할 토큰과 프로젝트 기준을 함께 동기화합니다.')
css=css.replace(':root {','[data-livepatch-app] {')
values={
 '--text-display':'3rem','--text-h1':'2rem','--text-h2':'1.5rem','--text-h3':'1.25rem','--text-h4':'1.125rem',
 '--leading-display':'1.25','--leading-heading':'1.3125','--leading-body':'1.625','--leading-caption':'1.538462',
 '--tracking-display':'-0.01em','--tracking-heading':'-0.01em','--tracking-body':'0',
 '--project-primary':'#2563eb','--project-primary-hover':'#1d4ed8','--project-primary-active':'#1e40af','--project-primary-soft':'#eff6ff',
 '--project-accent':'var(--project-primary)','--project-accent-soft':'var(--project-primary-soft)',
 '--color-text-muted':'var(--color-ink-600)',
 '--color-success':'var(--color-ink-700)','--color-success-soft':'var(--color-bg-subtle)',
 '--color-warning':'var(--color-ink-600)','--color-warning-soft':'var(--color-bg-subtle)',
 '--color-info':'var(--color-ink-700)','--color-info-soft':'var(--color-bg-subtle)',
 '--container-main':'90rem','--focus-ring-color':'var(--project-primary)',
}
for key,value in values.items():css=re.sub(r'('+re.escape(key)+r'\s*:)\s*[^;]+;',r'\g<1> '+value+';',css)
css=css.replace('/* 1320px */','/* 1440px · 1920px 프레임에서 좌우 240px */')
css=css.replace('화이트/블랙 중심의 편집형 화면이며 Accent만 절제해 사용합니다.','뉴트럴 베이스이며 Primary는 선택과 현재 주요 행동에만 사용합니다.')
extra='''
  /* LIVEPATCH role tokens · app chrome only */
  --color-text-action: var(--project-primary);
  --color-text-on-primary: var(--color-white);
  --color-line-control: var(--color-ink-500);
  --frame-desktop: 120rem;
  --frame-content-margin: 15rem;
  --layout-columns: 12;
  --control-hit-min: 2.75rem;
  --studio-topbar-height: 3.5rem;
  --studio-dock-width-collapsed: 20rem;
  --studio-dock-width-expanded: 23.75rem;
  --studio-dock-height-collapsed: 3.5rem;
  --studio-inspector-width: 23.75rem;
  --studio-inspector-min: 22.5rem;
  --studio-inspector-max: 26.25rem;
  --studio-safe-area: 1rem;
  --studio-chrome-bg: var(--color-bg);
  --studio-canvas-bg: var(--color-bg-muted);
  --studio-selection: var(--project-primary);
  --studio-patched: var(--color-text);
  --studio-ambiguous: var(--color-text-muted);
  --studio-blocked: var(--color-error);
  --studio-ring-width: 2px;
  --studio-ring-outer: 1px;
  --line-display: 3.75rem;
  --line-h1: 2.625rem;
  --line-h2: 2.125rem;
  --line-h3: 1.75rem;
  --line-h4: 1.625rem;
  --line-body-lg: 1.75rem;
  --line-body: 1.625rem;
  --line-body-sm: 1.375rem;
  --line-caption: 1.25rem;
  --text-label: 0.875rem;
  --line-label: 1.25rem;
'''
css=css.rstrip();css=css[:-1]+extra+'}\n'
css+='''
/* Owned app boundary. Never inject this stylesheet into the customer document. */
:where([data-livepatch-app], [data-livepatch-app] *, [data-livepatch-app] *::before, [data-livepatch-app] *::after) { box-sizing: border-box; }
[data-livepatch-app] { font-family: var(--font-sans); font-weight: var(--font-weight-regular); color: var(--color-text); background: var(--color-bg); font-size: var(--text-body); line-height: var(--leading-body); letter-spacing: var(--tracking-body); overflow-wrap: break-word; font-variant-numeric: tabular-nums; color-scheme: light; }
[data-livepatch-app] :where(h1,h2,h3,h4,p) { margin-block: 0; }
[data-livepatch-app] :where(h1,h2,h3,h4,.heading,.card-title) { color: var(--color-text-strong); font-family: var(--font-display); line-height: var(--leading-heading); letter-spacing: var(--tracking-heading); word-break: keep-all; overflow-wrap: break-word; }
[data-livepatch-app] h1 { font-size: var(--text-h1); line-height: var(--line-h1); font-weight: var(--font-weight-bold); }
[data-livepatch-app] h2 { font-size: var(--text-h2); line-height: var(--line-h2); font-weight: var(--font-weight-semibold); }
[data-livepatch-app] h3 { font-size: var(--text-h3); line-height: var(--line-h3); font-weight: var(--font-weight-semibold); letter-spacing: 0; }
[data-livepatch-app] h4 { font-size: var(--text-h4); line-height: var(--line-h4); font-weight: var(--font-weight-semibold); letter-spacing: 0; }
[data-livepatch-app] .lp-display { font-size: var(--text-display); line-height: var(--line-display); font-weight: var(--font-weight-bold); letter-spacing: var(--tracking-display); }
[data-livepatch-app] .lp-body-lg { font-size: var(--text-body-lg); line-height: var(--line-body-lg); }
[data-livepatch-app] .lp-body-sm { font-size: var(--text-body-sm); line-height: var(--line-body-sm); }
[data-livepatch-app] .lp-caption { font-size: var(--text-caption); line-height: var(--line-caption); }
[data-livepatch-app] .lp-label { font-size: var(--text-label); line-height: var(--line-label); font-weight: var(--font-weight-semibold); }
[data-livepatch-app] :where(a) { color: inherit; text-decoration-thickness: from-font; text-underline-offset: .18em; }
[data-livepatch-app] :where(button,input,select,textarea) { font: inherit; }
[data-livepatch-app] :where(a,button,input,select,textarea):focus-visible { outline: var(--focus-ring-width) solid var(--focus-ring-color); outline-offset: var(--focus-ring-offset); }
[data-livepatch-app] :where(img,svg,video) { display: block; max-width: 100%; }
[data-livepatch-app] .container { width: min(100% - (var(--page-gutter) * 2), var(--container-main)); margin-inline: auto; }
[data-livepatch-app] .container--content { width: min(100% - (var(--page-gutter) * 2), var(--container-content)); margin-inline: auto; }
[data-livepatch-app] .container--wide { width: min(100% - (var(--page-gutter) * 2), var(--container-wide)); margin-inline: auto; }
[data-livepatch-app] .reading-width { width: min(100%,var(--content-reading)); }
[data-livepatch-app] .section { padding-block: var(--section-space-lg); }
[data-livepatch-app] .section-heading { display:grid; gap:var(--space-3); max-width:48rem; }
[data-livepatch-app] .eyebrow { color:var(--color-text-muted); font-size:var(--text-caption); font-weight:var(--font-weight-semibold); line-height:var(--leading-caption); letter-spacing:0; }
[data-livepatch-app] .surface-card { border:1px solid var(--color-line-light); border-radius:var(--radius-card); background:var(--color-white); box-shadow:var(--shadow-none); }
@media (max-width:64rem) { [data-livepatch-app] { --page-gutter:1.5rem; --section-space-xl:5rem; --section-space-lg:4.5rem; --section-space-md:4rem; --grid-gap-lg:1.5rem; } }
@media (max-width:40rem) { [data-livepatch-app] { --page-gutter:1.125rem; --section-space-xl:4rem; --section-space-lg:3.5rem; --section-space-md:3rem; --section-space-sm:2.5rem; --grid-gap:1.125rem; --grid-gap-lg:1.25rem; } [data-livepatch-app] .section-heading { max-width:none; } }
@media (prefers-reduced-motion:reduce) { [data-livepatch-app], [data-livepatch-app] *, [data-livepatch-app] *::before, [data-livepatch-app] *::after { scroll-behavior:auto !important; animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; } }
'''
cssfile.write_text(css,encoding='utf-8')

# Figma 토큰 소스. rem은 standalone app의 16px 루트를 기준으로 환산.
head=css[:css.index('/* Owned app boundary.')]
tokens={k:v.strip() for k,v in re.findall(r'(--[a-z0-9-]+)\s*:\s*([^;]+);',head)}
def resolve(key,seen=None):
 v=tokens[key];m=re.fullmatch(r'var\((--[^)]+)\)',v)
 if m:return resolve(m.group(1),(seen or set())|{key})
 return v
manifest=[]
for key,value in tokens.items():
 raw=resolve(key)
 if re.fullmatch(r'#[0-9a-fA-F]{6}',raw):typ='COLOR';value=raw;group='Color';scopes=['TEXT_FILL'] if 'text-' in key else ['STROKE_COLOR'] if any(x in key for x in ['line','selection','ring-color','patched','ambiguous','blocked']) else ['FRAME_FILL','SHAPE_FILL']
 elif re.fullmatch(r'[0-9.]+(?:rem|px|ms)?',raw):
  typ='FLOAT';number=float(re.search(r'[0-9.]+',raw).group());value=number*16 if raw.endswith('rem') else number
  group='Typography' if key.startswith(('--text-','--font-weight-','--line-','--leading-')) else 'Metrics'
  scopes=['FONT_SIZE'] if key.startswith('--text-') else ['LINE_HEIGHT'] if key.startswith('--line-') else ['FONT_WEIGHT'] if key.startswith('--font-weight-') else ['CORNER_RADIUS'] if key.startswith('--radius-') else ['GAP'] if key.startswith(('--space-','--section-space','--grid-gap','--page-gutter','--studio-safe-area')) else ['WIDTH_HEIGHT'] if any(s in key for s in ['width','height','container','frame-','control-hit','reading','inspector']) else []
 else:continue
 manifest.append({'css':key,'name':key[2:],'type':typ,'group':group,'value':value,'alias_css':re.fullmatch(r'var\((--[^)]+)\)',tokens[key]).group(1) if re.fullmatch(r'var\((--[^)]+)\)',tokens[key]) else None,'scopes':scopes})
manifest.append({'css':'--font-sans','name':'font-sans','type':'STRING','group':'Typography','value':'Pretendard','alias_css':None,'scopes':['FONT_FAMILY']})
manifest.append({'css':'--font-display','name':'font-display','type':'STRING','group':'Typography','value':'Pretendard','alias_css':'--font-sans','scopes':['FONT_FAMILY']})
styles=[('Display',48,60,'Bold','--text-display','--line-display'),('H1',32,42,'Bold','--text-h1','--line-h1'),('H2',24,34,'SemiBold','--text-h2','--line-h2'),('H3',20,28,'SemiBold','--text-h3','--line-h3'),('H4',18,26,'SemiBold','--text-h4','--line-h4'),('Body Large',18,28,'Regular','--text-body-lg','--line-body-lg'),('Body',16,26,'Regular','--text-body','--line-body'),('Body Small',14,22,'Regular','--text-body-sm','--line-body-sm'),('Caption',13,20,'Regular','--text-caption','--line-caption'),('Label',14,20,'SemiBold','--text-label','--line-label')]
data={'version':'1.0','date':'2026-10-16','scope':'Foundations only','frame':1920,'content':1440,'font':'Pretendard','tokens':manifest,'text_styles':[{'name':'LP '+n,'size':sz,'line':ln,'weight':w,'size_css':sc,'line_css':lc} for n,sz,ln,w,sc,lc in styles]}
(ROOT/'정리/LIVEPATCH_Foundations토큰_261016.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'tokens':len(manifest),'text_styles':len(styles),'files':[str(brief),str(cssfile)]},ensure_ascii=False))
