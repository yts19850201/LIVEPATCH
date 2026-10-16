"""LIVEPATCH v5.7 문서 정합화. 원본 백업 후 계약과 파생 문서를 함께 갱신한다."""
from pathlib import Path
import json, re, copy, hashlib, collections, html

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '정리'
DATE = '2026-10-16'
BACKUP = OUT / '수정전백업_261016'
BACKUP.mkdir(exist_ok=True)
SOURCE = [f for f in ROOT.iterdir() if f.is_file() and f.suffix in {'.md', '.html', '.json'}]
for f in SOURCE:
    target = BACKUP / (f.stem + '_수정전_261016' + f.suffix)
    if not target.exists():
        target.write_bytes(f.read_bytes())

def read(name):
    # 재실행해도 이력/헤더가 중복되지 않도록 수정 전 기준에서 재생성한다.
    source = Path(name)
    original = BACKUP / (source.stem + '_수정전_261016' + source.suffix)
    return (original if original.exists() else ROOT/name).read_text(encoding='utf-8-sig')
def write(name, text): (ROOT / name).write_text(text, encoding='utf-8')
def dump(path, data): path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

JNAME = 'LIVEPATCH_v5.6_screen_field_contracts.json'
j = json.loads(read(JNAME))
screens = j['screens']
byid = {s['id']: s for s in screens}

# 기존 화면 ID는 보존한다. 현재 출시 상태와 과거 릴리스 분류를 분리한다.
pages = {
 'M': 'M01 M02 M06 M11 M13 M14 M20 M21 M22 M24 M25 M26 M27 M28 M30 M31 M32 M33 M34'.split(),
 'C': 'C01 C07 C13 C15 C19 C20 C23 C25 C26 C27 C33 C36 C40 C42'.split(),
 'A': 'A01 A02 A03 A06 A10 A13 A18 A19 A21 A24 A30'.split(),
}
overlays = 'O01 O02 O06 O08 O11 O14 O16 O17 O18 O19 O20 O21 O22 O23 O25 O26 O28 O29 O33'.split()
paid = set('M30 M31 C23 C25 C26 C27 A18 A19 O06 O26'.split())
primary = set(sum(pages.values(), []) + overlays)
merge_groups = {
 'M02': 'M03 O04', 'M11': 'M12 O05', 'M01': 'M04 M17',
 'C01': 'C02 C03 C04 C05 C06 C08 C09 C10',
 'C07': 'C12', 'C13': 'C11 C16 C17 O09 O10 O12 O13 O15 O34 O35 O38',
 'C15': 'C14', 'C19': 'C18', 'C20': 'C21', 'C33': 'C31 C32',
 'C23': 'C37', 'O01': 'O32',
 'A03': 'A04 A28 A29 A32 A40 A41 A42 A46',
 'A06': 'A05', 'A10': 'A09 A11 A16 A47',
 'A13': 'A12 A14 A15', 'A18': 'A17 A20 A45',
 'A21': 'A22', 'A24': 'A23',
 'O11': 'O36 O37', 'O17': 'O39', 'O18': 'O40',
}
embedded = {id: host for host, ids in merge_groups.items() for id in ids.split()}
assert not (primary & set(embedded))
assert all(host in primary for host in embedded.values())

j['version'] = '5.7'
j['revision'] = '2026-10-16-document-alignment'
j['canonical_source'] = 'LIVEPATCH_사업기획서.md 27장'
j['release_semantics'] = {
 'release_v56': 'v5.6 이력. 현재 출시 여부를 판단할 때 사용하지 않는다.',
 'release_current': 'PILOT_REQUIRED=폐쇄형 베타 및 유료 MVP 공통, PAID_REQUIRED=유료 출시 추가, EMBEDDED=호스트 화면 내부 상태/섹션, POST_MVP=후속',
 'embedded_route': '내부 경로는 host_route + section/deep-link로 연결하며 기존 별도 라우트는 새로 노출하지 않는다. 토큰·작업 ID는 검증 후 호스트에 전달한다.',
 'actions': 'role_type=action 또는 navigation인 모든 필드 key. primary_action은 현재 기본 상태의 주요 CTA 1개.',
}
j['launch_policy'] = {
 'status': '디자인·구현 기준선. 상용 공개는 release_gates 통과 후.',
 'connector': 'Mode A GitHub. 검증된 정적 HTML/CSS 템플릿과 배포 파이프라인 1종. 소스 매핑 HIGH만 운영 반영.',
 'site_limit': 1, 'customer_role': 'ORG_OWNER 1인; 관리자 계정/권한은 별도',
 'operations': ['텍스트', '기존 이미지 교체', '허용 목록 기반 색·글자 크기·여백'],
 'scope': '선택한 단일 요소. 컴포넌트 전체·페이지 전체·일괄 배포 제외.',
 'voice': '데스크톱 음성 우선. 대상 Chrome/Edge 환경은 테스트 통과 후 공개 지원. STT 공급사·개인정보·숫자 인식 검증은 출시 차단 게이트.',
 'mobile': '공식 웹·계정·작업/청구 조회·문의 지원. 모바일 Studio·QR 페어링·촬영 업로드는 후속.',
 'credits': {
  'estimate': '텍스트 1C, 이미지 2C, 허용 스타일 2C는 작업 기준값. 가격 버전과 서버 견적에 바인딩. 실제 원가 검토 후 상용 노출.',
  'hold': '미리보기 요청 시 예상 사용량 예약. 미리보기 성공만으로 차감하지 않는다.',
  'commit': '운영 배포와 사후 확인이 VERIFIED가 되면 견적 이하로 1회 확정.',
  'release': '배포 전 취소·생성 실패·24시간 초안 만료, 배포 실패 후 원본 유지 또는 자동 복원 확인 시 예약 해제.',
  'unknown': '결과 불명 시 예약 유지·상태 대사. 재배포/재차감 금지. 운영 담당자가 처리하며 만료 배치도 해제하지 않음.',
  'rollback': 'MVP 복원 추가 차감 없음. 정상 반영 후 고객 변심 복원은 원래 작업 차감 유지. 서비스 장애 환급은 사유·원장 기록 후 처리.',
  'preview_limit': '조직당 하루 생성 시도 최대 10회, 동시 생성 1개. 실패 시도도 호출 한도에 포함. 크레딧 차감과 구분.',
  'draft_expiry_hours': 24,
 },
 'approval': '도메인·변경·최대 비용 확인 → 1초 길게 누르기 또는 동등한 접근성 확인 → 패스키 재인증 → 서버 권한·sourceHash·검증·approvalDigest 확인. 음성만으로 배포하지 않음.',
 'rollback': '기본 복원 후보는 마지막 성공 배포 1건. 보존 기간 내·원본 해시/후속 의존성·스냅샷 유효성 통과 시 요청. 복원 배포 및 사후 확인 뒤 완료.',
 'plan': '유료 MVP는 단일 Economy 상품. 월 9,900원·100C는 기존 가격 가설을 인계값으로 유지하며 원가·PG·정책 게이트 통과 후만 판매. 무료 체험은 샘플 데모, 실사이트 무제한 무료 없음.',
 'tracking': 'MVP는 비필수 광고·분석 SDK 미탑재. 서비스 운영 이벤트의 최소수집·보존·고지는 개인정보 검토 게이트에서 확인.',
 'release_gates': ['지원 템플릿의 생성·검증·배포·복원 E2E', '권한·재인증·동시 변경·멱등성·UNKNOWN 대사', 'STT 공급사·개인정보·접근성·한국어 숫자 사용성', '출시 화면 TBD 및 OpenAPI·오류 계약 해소', 'PG 실제 결제·중복 webhook·취소·해지·원장 대사', '가격·보존·약관·개인정보·환불 정책 승인', '원가·운영 담당·모니터링·복구 모의훈련'],
}

for s in screens:
    id = s['id']
    s['release_current'] = ('PAID_REQUIRED' if id in paid else 'PILOT_REQUIRED') if id in primary else ('EMBEDDED' if id in embedded else 'POST_MVP')
    s['host_screen'] = embedded.get(id)
    s['host_route'] = byid[embedded[id]]['route'] if id in embedded else None
    s['launch_condition'] = '호스트 출시 단계 상속' if id in embedded else ('상용 게이트 통과' if id in paid else '공통 게이트 통과' if id in primary else '최초 MVP 비노출')
    s['contract_readiness'] = 'DRAFT_NOT_DEV_READY'
    s['mockup_snapshot_version'] = '5.6-r2 참고 이미지. v5.7 정책·현재 범위는 계약이 우선.'
    s['mockup'] = f"mockups/mockups/{id}.png"
    # generic failure copy cannot assert zero mutations after a timeout.
    for f in s['fields']:
        if f.get('failure_copy') and ('실제 데이터는 바뀌지 않았습니다' in f['failure_copy']):
            f['failure_copy'] = f"‘{f['label']}’ 결과를 확인하지 못했습니다. 상태를 조회한 뒤 다시 진행해 주세요. 중복 실행하지 마세요."
    if s.get('states_copy', {}).get('error'):
        s['states_copy']['error'] = f"{s['title']} 정보를 불러오지 못했습니다. 진행한 작업이 있다면 상태를 확인한 뒤 다시 시도해 주세요."

def field(id, key): return next(f for f in byid[id]['fields'] if f['key'] == key)
def spec(id, key, value, rule=None):
    f = field(id,key); f.update(example_value=value, example_status='SPEC')
    if rule is not None: f['rule'] = rule

# 음성 시작과 미리보기 생성을 다른 행동으로 연결한다.
if not any(f['key']=='voice_start' for f in byid['C13']['fields']):
    voice = copy.deepcopy(field('O11','voice_button'))
    voice.update(key='voice_start',label='말로 바꾸기',rule='녹음만 시작. O36 듣는 중으로 이동; 배포·미리보기 생성 없음.',v57_change='ADDED')
    voice['analytics_event']['name'] = 'c13_voice_start_click'
    byid['C13']['fields'].insert(13,voice)
byid['C13']['glance']['cta'] = {'key':'voice_start','label':'말로 바꾸기'}
byid['C13']['copy']['subtitle'] = '고칠 곳을 고르고 말해 주세요. 확인 후 미리보기를 만듭니다.'
byid['C13']['ui'] = '선택 번호와 하단 마이크를 기본 배치. 텍스트는 보조. O34~O38은 C13·O11의 상태로 조립한다.'
byid['C13']['ux'] = '음성 시작 → 인식 결과 확인 → 범위·견적 확인 → 미리보기 생성. 각 단계의 행동·이벤트를 분리한다.'
field('C13','scope')['rule'] = 'MVP는 selected_element만. 나머지 enum은 후속 기능 플래그 OFF.'
field('C13','instruction_type')['rule'] = '자동 판별·텍스트·이미지 교체·허용 스타일. 구조/DB/로직 변경 차단.'
field('O11','voice_button')['rule'] = '데스크톱 음성 우선. 공급사·개인정보·지원 환경 검증 필수. 권한 거부·오인식 시 터치·텍스트 대안.'
byid['O11']['copy']['subtitle'] = '고칠 곳을 선택하고 말해 주세요. 글자로도 입력할 수 있습니다.'

# 승인 경로는 하나로 통일. 화면의 두 체크박스를 서버 승인 조건으로 혼동하지 않는다.
byid['O17']['fields'] = [f for f in byid['O17']['fields'] if f['key'] not in {'confirm_domain','confirm_impact'}]
if not any(f['key']=='reauth_state' for f in byid['O17']['fields']):
    f = copy.deepcopy(field('O17','rollback_possible'))
    f.update(key='reauth_state',label='본인 확인 상태',rule='패스키 재인증 결과. VERIFIED 전 배포 요청 불가.',example_value='본인 확인 필요',example_status='SPEC',initial_value='REQUIRED',v57_change='ADDED')
    f['unavailable_copy'] = '본인 확인 상태를 확인하지 못했습니다. 반영을 중단하고 다시 확인해 주세요.'
    byid['O17']['fields'].insert(-2,f)
f = field('O17','final_deploy')
f.update(label='길게 눌러 반영',rule=j['launch_policy']['approval'],interaction='도메인·변경·최대 비용을 읽고 의도 확인 후 패스키. 접근성 대안은 버튼 활성화→확인 Dialog→패스키로 동일 서버 게이트 적용.')
f['a11y']['alternative'] = '키보드·스위치 제어 확인 버튼→확인 Dialog→패스키. 음성은 확인 단계 진입만 가능.'
byid['O17']['glance']['cta']['label'] = '길게 눌러 반영'
byid['O17']['ux'] = j['launch_policy']['approval']
byid['O39']['ux'] = 'O17의 길게 누르기 확인 상태. 독립 승인 API를 만들지 않고 같은 approvalDigest·패스키·서버 가드를 사용한다.'
field('O39','hold_publish').update(rule=j['launch_policy']['approval'],interaction=f['interaction'],a11y=copy.deepcopy(f['a11y']))
byid['O39']['dev'] = 'O17 공통 확인 흐름: 1,000ms 또는 접근성 확인→WebAuthn 재인증→권한·해시·approvalDigest 검사→멱등 배포. 음성은 확인 화면 진입만.'
byid['O39']['qa'] = '1초 미만 반영 불가, 접근성 확인 대안·패스키 실패 차단, 음성만으로 배포 불가, 중복 요청 동일 작업 확인.'

byid['O37']['copy']['notice'] = '미리보기에서는 크레딧을 예약만 합니다. 운영 반영 확인 후 차감합니다. 생성은 하루 10회까지입니다.'
spec('O37','before_value','30,000원')
spec('O37','after_value','35,000원','사용자 음성 인식 후보를 확인한 디자인 샘플. 실제값은 선택 요소·확정 의도에서 조회.')
spec('O37','credit_cost','최대 1 크레딧','예상 상한 표시. 미리보기 요청 시 HOLD, VERIFIED 시 COMMIT. 서버 견적 버전 확인.')
field('O37','confirm_yes')['rule'] = '견적·의도 버전을 확인하고 HOLD 후 생성. 미리보기 성공 시 차감 금지.'
spec('O22','charge_policy',j['launch_policy']['credits']['commit'],'HOLD→VERIFIED 후 COMMITTED, 취소/만료/복원 확인 실패 시 RELEASED. UNKNOWN은 예약 유지.')
field('O17','cost_estimate').update(label='예약 크레딧·최대 차감',rule='creditHoldId·expectedCostVersion·최대 차감 표시. VERIFIED 전 확정 차감 없음.')
for id in ['O18','O39','O40']:
    byid[id]['copy']['notice'] = '복원 가능 기간과 후속 변경을 확인한 뒤 되돌리기를 요청할 수 있습니다.'
byid['O40']['copy']['subtitle'] = '반영 결과와 사후 점검 상태를 확인하세요.'
field('O40','publish_state')['rule'] = 'DEPLOYED이면 반영됨·사후 점검 중. VERIFIED이면 반영 확인 완료. UNKNOWN이면 확인 중으로 표시.'
field('O40','undo')['rule'] = '마지막 성공 배포·보존 기간·스냅샷·후속 의존성 확인 후 O18 진입. 발화만으로 롤백 실행 금지.'
byid['O40']['ux'] = 'O18의 결과/복원 진입 상태. 음성 되돌리기는 복원 검토를 연다. 서버 복원·사후 확인 전 완료 표시 금지.'
for id in ['C13','O17','O18','O39','O40']:
    byid[id]['error_codes'] = sorted(set(byid[id].get('error_codes',[]) + ['STALE_SOURCE','REAUTH_REQUIRED','DEPLOY_UNKNOWN','ROLLBACK_BLOCKED']))

# actions는 전체 행동/이동 목록, primary_action은 기본 상태 CTA로 고정한다.
for s in screens:
    s['actions'] = [f['key'] for f in s['fields'] if f.get('role_type') in {'action','navigation'}]
    g = s.get('glance') or {}; cta = g.get('cta') or {}
    found = next((f for f in s['fields'] if f['key']==cta.get('key')),None)
    if found and cta.get('label') and cta['label']!='—':
        if s['id']=='M01': found['label']='데모로 바로 해보기';cta['label']=found['label']
        else: cta['label']=found['label']
    s['primary_action'] = cta.get('key') if cta.get('key') in s['actions'] else None
    if g and cta:
        g['subline'] = s['copy'].get('subtitle','')
        k = g.get('key') or {}
        g['question'] = f"{k.get('label','핵심 정보')}이 ‘{k.get('value','확인할 값')}’이라는 것과 다음 행동 [{cta.get('label','확인')}]을 3초 안에 찾는다."
        g['answer'] = f"{s['title']} — {k.get('label','핵심 정보')}: {k.get('value','')} → [{cta.get('label','확인')}]"

# 가설/샘플은 명확히 표시하고 TBD를 완료 처리하지 않는다.
all_fields = [f for s in screens for f in s['fields']]
j['counts']['fields'] = len(all_fields)
for prefix, name in [('M','marketing'),('C','customer'),('A','admin'),('O','overlay')]:
    j['counts'][name+'_fields'] = sum(len(s['fields']) for s in screens if s['id'].startswith(prefix))
j['counts']['release_current'] = dict(collections.Counter(s['release_current'] for s in screens))
j['counts']['example_status_current'] = dict(collections.Counter(f.get('example_status') for f in all_fields))
j['counts']['launch_independent_pages'] = sum(len(v) for v in pages.values())
j['counts']['launch_overlay_components'] = len(overlays)
j['changes_v57'] = {'added_fields':['C13.voice_start','O17.reauth_state'], 'removed_fields':['O17.confirm_domain','O17.confirm_impact'], 'baseline_fields':1174,'current_fields':len(all_fields),'source_images':'기존 PNG는 변경하지 않고 v5.6-r2 참고 스냅샷으로 유지'}
dump(ROOT/JNAME,j)

labels={'PILOT_REQUIRED':'베타·MVP 공통','PAID_REQUIRED':'유료 출시 추가','EMBEDDED':'화면 내 통합','POST_MVP':'후속'}
def scope(s): return labels[s['release_current']] + (f" → {s['host_screen']}" if s['host_screen'] else '')
def esc(v):
    if v is None:return '—'
    if isinstance(v,(list,dict)):v=json.dumps(v,ensure_ascii=False)
    return str(v).replace('|','&#124;').replace('\n','<br/>')

plan = ['# LIVEPATCH 출시 MVP 범위와 Figma 디자인 작업 순서','',f'기준일 {DATE} · v5.7. 현재 제작 기준선이며 배포 완료나 상용 판매 승인을 의미하지 않는다. 기존 173개 화면 ID를 보존하고 최초 공개 범위를 아래와 같이 제한한다.','',
 '## 1. 출시할 제품','',
 '검증된 GitHub 정적 HTML/CSS 템플릿과 배포 파이프라인 1종에 한해, 고객 1인·사이트 1개를 연결한다. 선택한 요소 하나의 문구, 기존 이미지, 허용된 색·글자 크기·여백을 음성 또는 터치로 수정한다. 의도 확인·미리보기·검증·패스키 승인·운영 반영·사후 확인·마지막 성공 배포 복원이 한 흐름으로 이어진다. 원본 매핑 HIGH를 확인한 작업만 반영한다.','',
 '최초 고객은 이 지원 환경을 소유하거나 관리 권한을 가진 기존 사이트 운영자다. 임의 사이트·임의 프레임워크 전체 지원을 약속하지 않는다. 데모는 허용된 샘플 사이트만 사용한다.','',
 '데스크톱 Studio에서 음성 입력을 우선한다. 마이크 권한 거부·인식 실패에는 제안 칩·터치·텍스트 대안을 제공한다. 공식 웹·계정·작업/청구 조회·문의는 모바일을 지원하되 모바일 Studio·QR 페어링·촬영 업로드는 후속이다.','',
 '## 2. 현재 정책 정본','',
 '| 항목 | MVP 기준 |','|---|---|',
 '| 연결 | Mode A GitHub, 검증된 정적 템플릿·배포 파이프라인 1종. Mode B/C·빌더 앱은 후속 |',
 '| 변경 범위 | 단일 요소의 텍스트·기존 이미지 교체·허용 스타일. 페이지 구조·인증·결제·서버·DB·일괄 변경 제외 |',
 '| 음성 | 데스크톱 마이크 우선. 인식→정규화→확인→생성을 분리. 공급사·개인정보·숫자 인식 검증 전 공개하지 않음 |',
 '| 크레딧 | 미리보기 요청 시 HOLD, VERIFIED 때 COMMIT. 실패/취소/24시간 초안 만료 시 조건에 따라 RELEASE. UNKNOWN은 예약 유지 및 대사 |',
 '| 무료 생성 한도 | 조직당 하루 10회 생성 시도·동시 1개. 미리보기 차감 없음, 무제한 무료 아님. 실제 원가에 따라 상용 전 조정 |',
 '| 비용 | 서버 견적과 가격 버전에 바인딩, 최종 차감은 견적 이하. 텍스트 1C·이미지 2C·스타일 2C는 현재 인계값 |',
 '| 승인 | 도메인·변경·최대 비용 확인→1초 길게 누르기 또는 동등한 접근성 확인→패스키→서버 게이트. 음성만으로 배포 불가 |',
 '| 복원 | 마지막 성공 배포 1건, 보존 기간·해시·스냅샷·후속 의존성 검토 후 실행. 복원 및 사후 확인 전 완료 표시 금지 |',
 '| 복원 과금 | MVP 복원 추가 차감 없음. 정상 반영 후 고객 변심 복원은 원래 차감 유지. 장애 환급은 사유·원장 기록 |',
 '| 유료 상품 | 단일 Economy. 월 9,900원·100C는 가격 가설. 원가·PG·정책 검토 완료 전 판매 노출 금지. 상위 플랜·자동 충전·쿠폰·추가 크레딧 판매 제외 |',
 '| 개인정보 | 원음 저장 기본 OFF, 명령·URL 토큰을 분석 이벤트에 넣지 않음. 공급사 전달·처리 지역·보존 기간·고지·삭제는 출시 전 확정 |',
 '| 분석 | 비필수 광고·분석 SDK 미탑재. M23/O03 동의 기능은 해당 SDK 도입 시 재설계 |',
 '',
 '배포 결과 불명은 성공이나 실패로 추정하지 않는다. 재시도는 동일 jobId·멱등키로 상태를 대사한 뒤 처리한다. VERIFIED 전에는 크레딧을 확정하지 않으며, 배포 실패 후 원본 유지 또는 자동 복원 확인 시 예약을 해제한다. 복원까지 불명인 경우 예약 만료 배치에서도 자동 해제하지 않는다.','',
 '## 3. MVP 화면 범위','',
 f'유료 MVP는 **독립 페이지 {sum(map(len,pages.values()))}개 + 공용 오버레이 컴포넌트 {len(overlays)}개**를 제작한다. 내부 통합 대상은 별도 페이지나 별도 오버레이로 중복 집계하지 않는다. 폐쇄형 베타는 결제 추가 {sum(x[0]!="O" for x in paid)}페이지와 {sum(x[0]=="O" for x in paid)}오버레이를 제외한 36페이지+17오버레이이며, 베타 참가자의 크레딧은 테스트 원장으로 발급한다. 실결제·실청구로 오인시키지 않는다.','',
 '| 플랫폼 | 독립 페이지 ID | 수량 |','|---|---|---:|']
for prefix,title in [('M','공식 웹'),('C','고객 콘솔'),('A','관리자 콘솔')]:plan.append(f"| {title} | {', '.join(pages[prefix])} | {len(pages[prefix])} |")
plan += [f"| 공용 오버레이 | {', '.join(overlays)} | {len(overlays)} |",'',
 '공식 웹은 소개·샘플 체험·지원 범위·가격·보안·FAQ·정책·인증·결제·공통 오류를 포함한다. 고객 콘솔은 사이트 허브·연결 설정·Studio·작업·배포/복원·크레딧·구독/결제수단/영수증/해지·문의·개인보안·삭제 요청·상태를 포함한다. 관리자 콘솔은 로그인/MFA·관제·회원·사이트·작업/복원·정산·환불·크레딧·문의·감사를 포함한다.','',
 '목록과 상세의 분리는 필요한 곳만 유지한다. 한 페이지 안에서 목록→상세 상태를 전환할 때 필터·페이지·선택 항목·돌아가기 맥락을 유지한다. 이 범위는 라우트 템플릿 집계이며 조직이나 사이트 데이터 건수로 늘리지 않는다.','',
 '| 통합 대상 | 호스트 화면 | 처리 방식 |','|---|---|---|']
for host,ids in merge_groups.items():
    plan.append(f"| {', '.join(ids.split())} | {host} {byid[host]['title']} | 단계·탭·섹션 또는 상태로 구현; 별도 메뉴/라우트 비노출 |")
plan += ['',
 'O09/O10/O12/O13/O15와 K1~K7은 Studio의 필수 구성·상태로 포함한다. K6는 O17 승인 상태, K7는 O18 복원 진입/결과 상태다. 통합은 기능 삭제를 의미하지 않는다. 기존 별도 라우트는 신규 메뉴에 노출하지 않으며 내부 링크는 host_route와 화면 상태를 사용한다. 필요한 과거 링크는 리소스 권한을 확인한 뒤 호스트로 연결한다.','',
 '관리자 직원·역할 편집(A37/A38), 전문가 판매/배정, 파트너 리셀, 다중 사이트·팀·2인 고객 승인, 소셜 로그인, CMS/SFTP/표시 패치, AI 선제 제안, 일괄 반영, 모바일 Studio는 후속이다. 관리자 초기 계정은 제한된 운영 절차로 프로비저닝하고 세션 회수·계정 잠금·권한 변경을 감사한다. 위험 조정은 요청자와 승인자를 분리하며 운영 인력 부재 시 실행하지 않는다.','',
 '## 4. Figma 디자인 작업 순서','',
 '| 순서 | 산출물 | 화면/내용 | 완료 기준 |','|---|---|---|---|',
 '| 0 | 작업 보드와 흐름 | 현재 범위·호스트·정책·성공/실패 여정 | 각 ID의 포함/통합/후속과 경로 확인 |',
 '| 1 | 공통 토큰·컴포넌트 | 모노크롬, 선택/CTA 파랑, 위험 빨강, 타입·간격·폼·버튼·토스트·시트·테이블·포커스 | Auto Layout·변형·토큰 바인딩·장문 대응 |',
 '| 2 | Studio 핵심 프로토타입 | C13, O11, O14, O16~O20, O33 및 K1~K7 상태 | 선택→말하기→확인→미리보기→패스키 승인→반영/복원 연결 |',
 '| 3 | 연결 및 첫 성공 | C01/C07, 통합 C02~C10/C12, O21 | 지원/제한/미지원·위임 안내·연결 실패·테스트 복원 처리 |',
 '| 4 | 고객 작업과 지원 | C15/C19/C20/C33/C36/C40/C42, O22/O23 | 작업 복귀·UNKNOWN·복원 차단·삭제 요청·문의 맥락 유지 |',
 '| 5 | 운영 콘솔 | A01/A02/A03/A06/A10/A13/A21/A24/A30, O25/O28/O29 | MFA·권한·긴급 중지·감사·고객/내부 메모 분리 |',
 '| 6 | 공식 웹과 인증 | M01/M02/M06/M11/M13/M14/M20~M22/M24~M28/M32~M34 | 기능/지원 한계와 데모·가입·첫 연결 동선 일치 |',
 '| 7 | 유료 출시 기능 | M30/M31/C23/C25/C26/C27/A18/A19, O06/O26 | 결제 확인 중·중복 webhook·해지·환불·원장 흐름 연결 |',
 '| 8 | 반응형·인계 | 출시 프레임의 1024/768/390 재배치와 오류 상태, 명세/이벤트 인계 | 기존 1440 프레임과 의미 일치, 지원 환경 QA, 미정값 해소 |',
 '',
 '각 단계에서 먼저 대표 1440 프레임으로 구조를 잡고 좁은 화면에서 즉시 확인한다. 마지막 단계까지 반응형 검토를 미루지 않는다. 모바일 Studio는 동작 가능한 것처럼 그리지 않고 데스크톱 전환 안내를 제공한다. 기본·로딩·빈·오류·권한 없음·오프라인에 더해 음성 거부·오인식·원본 변경·재인증 실패·배포/복원 결과 불명을 핵심 상태로 만든다.','',
 'Figma 구성은 `00 작업 기준`, `01 Foundations`, `02 Components`, `03 Studio`, `04 연결과 고객 콘솔`, `05 관리자`, `06 공식 웹`, `07 결제`, `08 검수와 인계` 순서로 계획한다. 레이어 이름에 `/`를 쓰지 않는다. 컨테이너는 Auto Layout을 기본으로 하고 사이트 선택 경계 등 좌표가 필요한 요소만 absolute로 둔다. 화면 ID는 프레임 이름 앞에 유지한다.','',
 '작업 링크: https://www.figma.com/design/VwuyN75CQK9Kn0ZyIVmF4S/LIVEPATCH?node-id=0-1 . 메타데이터 접근 확인 완료. 0:1 페이지 이름은 LIVEPATH_ver1.0이며 조회된 하위 요소는 없다. 읽기 접근만 확인했으며 이번 작업에서 캔버스·페이지 이름을 수정하지 않았다.','',
 '## 5. 출시 차단 게이트','',
 '| 게이트 | 통과 증거 |','|---|---|',
 '| G0 범위·연결 | 지원 템플릿·파이프라인·소유권·매핑 근거, 생성/실배포/복원 E2E |',
 '| G1 안전 | 권한·패스키·sourceHash·approvalDigest·멱등키·UNKNOWN 대사·복원 실패 검증 |',
 '| G2 음성·접근성 | 공급사/개인정보 결정, 대상 브라우저·한국어 금액/전화/날짜, 마이크 거부·보조기기 대안 검증 |',
 '| G3 디자인·계약 | 현재 출시/통합 화면의 TBD·enum·오류코드·API·접근성·이벤트 계약 해소, 핵심 프로토타입 비개발자 5인 테스트 및 4인 이상 3초 핵심 인지 |',
 '| G4 유료 출시 | PG 결제/취소/해지/중복 webhook·실원장 대사, 상품/가격·약관·개인정보·환불·보존 기간 검토 |',
 '| G5 운영 | 초기 운영자 계정·위험 작업 승인자 분리·모니터링·장애/자동 복원 모의훈련, 호출 비용 계측 |',
 '',
 '폐쇄형 베타도 G0~G3 및 개인정보·테스트 운영에 필요한 G5를 통과해야 한다. G4 전에는 결제를 받지 않는다. 비용 한도·가격·보존 기간·STT·PG 공급사·실제 공수와 날짜는 결정/측정 결과를 기록한 뒤 확정한다. 고정 출시일은 근거 없이 부여하지 않는다.','',
 '## 6. 이번 수정의 범위','',
 'R01 이미지 경로, R02 과금, R03 음성/모바일, R04 연결, R05 CTA, R06 actions 의미, R08 복원 안내, R09 레이어 색상, R10 집계 표기, R11 범위를 정리했다. R07의 미정 데이터와 API 계약은 목록을 유지하며 완료로 처리하지 않았다. 과거 PNG는 v5.6-r2 참고 이미지이며 v5.7 화면 검수 증거가 아니다. Figma 작업은 위 순서에 따라 다음 단계에서 시작한다.','']
plan_text='\n'.join(plan)
(OUT/'LIVEPATCH_MVP범위와Figma작업순서_261016.md').write_text(plan_text,encoding='utf-8')

# JSON 파생 필드 명세와 체크리스트를 재생성한다.
field_doc=['# LIVEPATCH v5.7 운영 화면 필드와 현재 출시 계약','',
 '> 정본: 마스터 27장 및 screen_field_contracts.json v5.7. release_current가 현재 범위이며 release_v56는 이력이다. TBD·API 후보는 미정이며 DEV_READY로 간주하지 않는다. PNG는 이전 참고 스냅샷이다.','',
 '## 19-앞. 제작팀 작업 규칙 및 필드 계약','',
 '- required는 입력 요소에만 적용한다. 표시·조작은 presence로 관리한다.',
 '- actions는 모든 행동·이동 key, primary_action은 기본 상태의 주요 CTA다.',
 '- 오류는 invalid_copy, 실행 결과 불명은 failure_copy, 조회 실패는 unavailable_copy로 분리한다.',
 '- 모든 API 후보·오류·예시·권한·상태·접근성 계약을 확정한 화면만 DEV_READY로 전환한다.','']
check=['# LIVEPATCH v5.7 화면별 제작과 검수 체크리스트','',
 '> 현재 범위는 release_current. 통합 화면은 호스트에서 검수하고 후속 화면은 MVP 메뉴에 노출하지 않는다. 기존 v5.6 분류는 이력이다. unchecked 항목은 미완료다.','']
for prefix,no,title in [('M',19,'공식 웹사이트'),('C',20,'고객 콘솔'),('A',21,'관리자 콘솔'),('O',22,'공용 레이어와 상태')]:
    group=[s for s in screens if s['id'].startswith(prefix)]
    field_doc += [f'## {no}. {title} {len(group)}개 설계 ID','']
    check += [f'## {title}','']
    for s in group:
        id=s['id'];fs=s['fields'];cp=s.get('copy') or {};gl=s.get('glance') or {}
        field_doc += [f'### <span id="field-{id.lower()}"></span>{id} · {s["title"]} — `{s["route"]}`','',
         f'- **현재 범위:** {scope(s)} · **기존 분류:** {s["release_v56"]}(이력) · **준비 상태:** {s["contract_readiness"]}',
         f'- **실제 연결 경로:** {s["host_route"] or s["route"]}; 통합 ID는 별도 라우트 비노출.',
         f'- **UI:** {s["ui"]}',f'- **UX:** {s["ux"]}',f'- **DEV:** {s["dev"]}',
         '- **문구:** '+' / '.join(f'{k}: {v}' for k,v in cp.items()),
         f'- **API 후보:** {esc(s.get("api_candidates"))} · **오류 코드 초안:** {esc(s.get("error_codes"))}',
         f'- **성능:** {esc(s.get("perf_budget"))} · **SEO:** {esc(s.get("seo"))}',
         f'- **3초 기준:** {gl.get("question","현재 상태와 다음 행동을 확인한다.")}',
         f'- **참고 목업:** [{id} 이전 스냅샷]({s["mockup"]}) — v5.7 완료 증거로 사용하지 않음.','',
         f'**노출 요소 {len(fs)}개**','',
         '| 키 · 레이블 | 컴포넌트 · 역할 · 필수/표시 | 규칙 · 초기값 · 예시 | 상호작용 · 문구 | 접근성 · 이벤트 · DEV |',
         '|---|---|---|---|---|']
        for f in fs:
            field_doc.append('| '+' | '.join(esc(v) for v in [
             f"`{f['key']}` · {f['label']}",f"{f['component']} (`{f['kind']}`) · {f.get('role_type')} · {f.get('required') if f.get('role_type')=='input' else f.get('presence')}",
             f"{f.get('rule')} / 초기: {f.get('initial_value')} / 예시: {f.get('example_value')} [{f.get('example_status')}]",
             f"{f.get('interaction')} / 오류: {f.get('invalid_copy') or '—'} / 실패: {f.get('failure_copy') or '—'} / 대체: {f.get('unavailable_copy') or '—'}",
             f"접근성: {json.dumps(f.get('a11y',{}),ensure_ascii=False)} / 이벤트: {json.dumps(f.get('analytics_event',{}),ensure_ascii=False)} / {f.get('dev_contract')}"
            ])+' |')
        field_doc += ['',f'**화면 actions:** {", ".join(s["actions"])}. **primary_action:** {s["primary_action"] or "없음/상태별 정의 필요"}.',
         f'**인수 조건:** {s["qa"]}. 현재 출시/통합 화면은 정책·실제 예시값·권한·반응형·실패/결과 불명·접근성을 검수한다.','', '---','']
        tbd=[f['key'] for f in fs if f.get('example_status')=='TBD']
        events=[(f.get('analytics_event') or {}).get('name') for f in fs if (f.get('analytics_event') or {}).get('name')]
        check += [f'### {id} {s["title"]} · **{scope(s)}**','',
         f'- [ ] **범위:** 호스트 {s["host_screen"] or id}; MVP 메뉴/내부 경로와 현재 범위 일치. 후속은 비노출.',
         f'- [ ] **UI:** {s["viewports"]}; 기본·로딩·빈·오류·권한·오프라인 및 기능별 상태. PNG 복사로 완료 처리 금지.',
         f'- [ ] **UX:** {s["ux"]}',
         f'- [ ] **데이터:** TBD {len(tbd)}개 — {", ".join(tbd) or "없음"}; SPEC은 디자인 예시이며 API 검증 완료와 구분.',
         f'- [ ] **DEV:** API 후보 {esc(s.get("api_candidates"))}; 오류 {esc(s.get("error_codes"))}; OpenAPI·enum·권한·멱등성 확정.',
         '- [ ] **A11y:** 포커스·키보드·보조기기·대안 입력·상태 읽기·대비·장문/확대 검증.',
         f'- [ ] **이벤트:** {", ".join(events) or "조회 이벤트 계약 정의"}; 명령 원문·음성·URL 토큰 미수집.',
         f'- [ ] **3초 확인:** {gl.get("question","핵심 상태와 다음 행동을 확인한다.")}',
         f'- [ ] **QA:** {s["qa"]}; 서버 상태와 화면·원장 일치. 결과 불명 상태에서 중복 실행 금지.','']
fields_text='\n'.join(field_doc)
write('LIVEPATCH_v5.6_운영화면_필드요소_상세명세.md',fields_text)
write('LIVEPATCH_v5.6_페이지별_UI_UX_DEV_체크리스트.md','\n'.join(check))

# 통합 마스터를 업데이트한다. 생성된 19~22장은 JSON에서 유래한 동일 본문으로 대체한다.
m=read('LIVEPATCH_사업기획서.md')
m=m.replace('# LIVEPATCH 통합 마스터 사업기획서 (v5.6 — 정합성·최적화 패치판: UI·UX·DEV·MKT·MGN 감사 반영)', '# LIVEPATCH 통합 마스터 사업기획서 v5.7')
m=m.replace('> **판본 상태**: v5.6 / 2026-10-15', '> **판본 상태**: v5.7 / 2026-10-16')
notice='> **현재 제작 기준:** 27장이 출시 범위·정책 정본이다. 26장의 키보드리스 원칙은 유지하되 앱/Mode C·모바일·과금 실험 제안은 27장에 따라 후속 또는 현재 정책으로 구분한다. 24장 이전 값과 v5.6 릴리스 집계는 이력이다. 현재 화면별 범위는 19~22장의 release_current를 따른다. 173개 설계 ID는 44페이지+19공용 오버레이 MVP로 조합하며 나머지는 내부 통합 또는 후속이다.\n\n'
if notice not in m:m=m.replace('\n\n','\n\n'+notice,1)

replacements={
 '문서 간 충돌값은 **24장 정본(Canonical)**이 우선한다.':'문서 간 충돌값과 현재 출시 범위는 **27장 정본(Canonical)**이 우선한다. 24장 값은 27장과 충돌하지 않는 규격만 사용한다.',
 '이 장은 9·23·24장보다 우선하는 핵심 레이어 정본이다.':'이 장은 핵심 레이어 방향을 규정한다. 현재 MVP 지원 범위·정책·보안 게이트는 27장이 우선한다.',
 '변경안 생성 요청 시 **HOLD** → `PREVIEW_READY`(S1~S3 통과) 시 **COMMIT** → 실패·취소 시 **RELEASE**. 배포·복원 자체는 MVP에서 추가 차감 없음(정책 확정 전 제안)':'미리보기 요청 시 **HOLD** → `PREVIEW_READY`에서는 예약 유지 → 운영 배포·사후 확인 `VERIFIED` 시 **COMMIT**. 취소·실패·초안 만료는 27장 조건에 따라 **RELEASE**, `UNKNOWN`은 예약 유지·대사. 복원 추가 차감 없음.',
 '데스크톱 마이크 STT = **조건부**(기능 플래그·STT 공급사·개인정보 검토 후). 모바일 QR 페어링(C41) = LATER. 실패 시 텍스트 입력 유지':'데스크톱 STT 우선 설계. 공급사·개인정보·한국어 인식·지원 환경 검증이 출시 게이트다. 모바일 Studio·QR 페어링은 후속. 실패 시 터치·텍스트 대안 유지.',
 '미리보기 일 10회 무료 + 반영 시 크레딧 확정 A/B (기존: 미리보기 성공 시 확정)':'v5.7 기본 정책: 조직당 일 10회 생성 시도·미리보기 예약만·VERIFIED 때 차감. 정책별 A/B는 후속',
 '카페24 앱·WP 플러그인·스크립트 1줄. Mode C(표시 패치)를 실험에서 **제한 정식**으로 승격 검토(SEO·깜빡임 기준 통과 시)':'후속 검토: 앱·플러그인·Mode C. 최초 MVP는 검증된 GitHub 정적 템플릿 1종',
 '데스크톱·모바일 모두 마이크를 1순위 CTA로, 텍스트는 보조':'최초 MVP는 데스크톱 마이크 우선·텍스트 보조. 모바일 Studio는 후속',
 '설치는 1줄 또는 앱 1번':'후속 연결 전략은 1줄 또는 앱 1번',
 '카페24·아임웹 앱, WordPress 플러그인, 스크립트 1줄을 1순위 연결로 두고, Git/SFTP는 에이전시용 고급 경로로 둔다.':'최초 MVP는 검증된 GitHub 정적 템플릿으로 제한한다. 앱·플러그인·스크립트·SFTP는 검증 후 후속 연결 경로로 확장한다.',
 '접근성 대안으로 음성 “반영해”와 스위치 제어를 제공한다.':'접근성 대안은 확인 버튼·Dialog·패스키로 같은 서버 승인 게이트를 적용한다. 음성 “반영해”는 확인 단계 진입만 수행한다.',
 '1초 길게 누르기 + 패스키 재인증(음성 “반영해”, 스위치 제어 대안)':'1초 길게 누르기 + 패스키 재인증. 키보드/스위치 확인도 동일 패스키·서버 게이트 적용; 음성만 배포 금지',
 '체크박스 2개 확인을 **1초 길게 누르기**로 바꾼다.':'UI 확인은 **1초 길게 누르기** 또는 동등한 접근성 확인으로 통일한다. 도메인·변경 검토·재인증은 서버 승인 계약에서 검증한다.',
 '핵심 경로(선택 → 요청 → 확인 → 미리보기 → 반영 → 되돌리기)는 **키보드 없이** 끝나야 한다.':'데스크톱 핵심 경로(선택 → 요청 → 확인 → 미리보기 → 반영 → 되돌리기)는 **키보드 없이** 끝나야 한다. 모바일 Studio와 확장 레버는 후속이며 지원 범위는 27장을 따른다.',
 '상세 플로우 K1~K12(O34~O45), 음성 문법, 시각 원칙, 사람 개입 최소화 지표는 마스터 26장을 따른다.':'K1~K7은 MVP 핵심 상태로 통합하고 K8~K12 확장은 후속으로 둔다. 음성 문법·시각 원칙은 26장, 현재 정책은 27장을 따른다.',
 'patched(`#059669` 실선+\'변경안\' 배지) · ambiguous(`#B45309` 점선+\'후보 N\')':'patched(중립 실선+\'변경안\' 배지) · ambiguous(중립 점선+\'후보 N\')',
 '미리보기 일일 무료량 + 반영 시 크레딧 확정을 A/B로 검증한다(D-17).':'현재 MVP는 일 10회 생성 한도·VERIFIED 후 차감으로 통일한다. 과금 A/B는 후속이다(D-17).',
 'HOLD는 생성 요청 시, COMMIT은 PREVIEW_READY, RELEASE는 실패·취소·HOLD 만료(30분)':'HOLD는 생성 요청 시, COMMIT은 VERIFIED, RELEASE는 배포 전 실패·취소·24시간 초안 만료 또는 원본 유지/자동 복원 확인 시. UNKNOWN은 예약 유지·대사',
 '`MEDIUM`은 수동 확인 후 진행, `HIGH`도 S1~S3 실패 시 즉시 차단':'최초 MVP는 `HIGH`만 반영하며 `MEDIUM/LOW/UNKNOWN`은 차단. `HIGH`도 S1~S3 실패 시 차단',
 '다중 요소 묶음 상한 20개':'최초 MVP 단일 요소만; 다중 요소 묶음 20개는 후속 가설',
 '명령 실행 시 크레딧을 **\'예약 잠금(Hold)\'** 처리하고, S1~S3 검증(정적·빌드·화면)을 통과해 미리보기가 정상 생성되었을 때만 확정 차감한다. 확정 차감액은 사전 견적을 넘지 않는다(v5.6). 실패 시 자동 환불하며 고객 콘솔 결제 내역에서 모든 차감·환불 사유를 투명하게 조회할 수 있다.':'미리보기 요청 시 크레딧을 예약(HOLD)하고, 운영 배포 및 사후 확인이 VERIFIED가 된 때 견적 이하로 확정한다. 생성 실패·취소·초안 만료 또는 원본 유지/자동 복원 확인 시 예약을 해제한다. 결과 불명은 예약 유지·대사하며, 확정 거래 환급은 별도 원장 이벤트로 기록한다.',
}
for a,b in replacements.items():m=m.replace(a,b)
m=re.sub(r'mockups/(?!mockups/)([MCAO]\d{2}(?:_mobile)?\.png)',r'mockups/mockups/\1',m)
m=m.replace('실시간 STT 자막창(조건부)','실시간 STT 자막창(데스크톱 우선)')
m=m.replace('데스크톱 STT 기능 플래그 활성 시에만.','데스크톱 STT 공급사·개인정보·사용성 검증 후 공개. ')
m=m.replace('hold-to-confirm(1,000ms, 접근성 대안: 스위치 제어·음성 “반영해”), WebAuthn 재인증, 멱등키, 원본 해시 재검사','hold-to-confirm(1,000ms) 또는 확인 버튼·Dialog 대안 후 WebAuthn 재인증, 멱등키·권한·해시·approvalDigest 검사. 음성은 확인 화면 진입만')
# old top-level strategy flags gain explicit scope.
m=m.replace('| **Mode A — Git 원본 변경**', '| **Mode A — Git 원본 변경**',1)
m=m.replace('**우선 지원** | 번들','**MVP: 검증된 정적 HTML/CSS 템플릿 1종만** | 번들')
m=m.replace('**검증된 어댑터 순차 지원**','**후속: 어댑터 검증 후 지원**')
m=m.replace('**실험 기능 → 후속 정식화**','**최초 MVP 제외; 후속 실험**')
intro='> **현재 출시 범위:** 이 장의 전수 설계 ID와 상세 기능은 전체 제품 재고다. 최초 MVP 포함·내부 통합·후속 여부는 19~22장 현재 범위 및 27장을 따른다. 아래 과거 MVP-α/β 표기는 v5.6 계획 이력이다.\n\n'
for no in [13,14,15,16,17,24,26]:
    pat=rf'(^## {no}\. [^\n]+\n\n)'
    m=re.sub(pat,lambda match:match.group(1)+intro,m,count=1,flags=re.M)
start=m.index('## 19-앞.')
end=m.index('## 23.',start)
body=fields_text[fields_text.index('## 19-앞.'):]
m=m[:start]+body+'\n'+m[end:]
# 전수 설계의 오래된 설명에도 현재 안전 게이트를 적용한다.
m=m.replace('hold-to-confirm(1,000ms, 접근성 대안: 스위치 제어·음성 “반영해”), WebAuthn 재인증, 멱등키, 원본 해시 재검사','hold-to-confirm(1,000ms) 또는 확인 버튼·Dialog 대안 후 WebAuthn 재인증, 멱등키·권한·해시·approvalDigest 검사. 음성은 확인 화면 진입만')
# Studio standalone content follows the same master section.
studio_start=m.index('## 23.')
studio_end=m.index('## 24.',studio_start)
studio=m[studio_start:studio_end]
studio=studio.replace('**v5.6 상태 정본:**','**v5.7 상태 정본:**')
studio=studio.replace('적용 위치: 고객 콘솔 `C13` 및 인페이지 레이어 `O09~O20`.','적용 위치: 고객 콘솔 `C13` 및 인페이지 레이어 `O09~O20`의 통합 구성. 현재 MVP 정책은 27장을 따른다.')
studio=re.sub(r'\| `G07` \|[^\n]+', '| `G07` | 마이크 버튼 **(v5.7 데스크톱 우선)** | 녹음·권한·인식 상태 | `말로 바꾸기` / 권한 거부 시 터치·텍스트 대안 | 공급사·개인정보·숫자 인식 검증은 출시 차단 게이트 |',studio)
studio=studio.replace('`PREVIEW_READY/FAILED`','`PREVIEW_READY/FAILED`')
studio += '\n**v5.7 승인·과금 추가 계약:** O17/O39는 동일 승인 흐름이다. 확인 조작 후 패스키를 검증하고 서버의 권한·sourceHash·approvalDigest·검증 통과를 확인한다. 음성만으로 배포하지 않는다. 미리보기 HOLD는 VERIFIED까지 유지하며 결과 불명은 대사 후 해제/확정한다.\n\n'
m=m[:studio_start]+studio+m[studio_end:]
write('LIVEPATCH_v5.6_Studio_GhostDock_명령창_상세계약.md','# LIVEPATCH v5.7 Studio 승인과 음성 계약\n\n'+studio[studio.index('\n\n')+2:])
if '\n## 27.' in m:m=m[:m.index('\n## 27.')]
embedded_plan=plan_text[plan_text.index('\n\n')+2:]
for n in range(1,7):embedded_plan=embedded_plan.replace(f'## {n}. ',f'### 27-{n}. ')
m+='\n\n## 27. v5.7 출시 MVP 범위와 Figma 디자인 작업 순서\n\n'+embedded_plan
write('LIVEPATCH_사업기획서.md',m)

log='''\n\n## v5.7 정합화 및 MVP 기준선 2026-10-16

현재 정본은 마스터 27장과 JSON v5.7이다. 과거 로그는 당시 의사결정 이력이며 현재 실행 정책으로 사용하지 않는다.

- D-17: 과금 실험 제안에서 현재 구현 기준으로 분리. 미리보기 HOLD, VERIFIED 확정, UNKNOWN 대사, 일 10회 생성 한도.
- D-18: 앱·Mode C 승격은 후속. 최초 지원은 검증된 GitHub 정적 템플릿·파이프라인 1종.
- D-19: 데스크톱 음성 우선은 유지. 공급사·개인정보·사용성 검증은 필수. 모바일 Studio는 후속.
- D-20/D-21: 파트너 마진·전문가 고정가 판매는 최초 MVP 제외.
- MVP: 독립 44페이지+공용 19오버레이. 폐쇄형 베타 36페이지+17오버레이, 유료 추가 8페이지+2오버레이. 내부 통합 ID는 중복 집계하지 않음.
- 문서 및 JSON에 실제 이미지 경로를 반영. PNG는 과거 스냅샷으로 표시.
- actions 전체 행동/이동 목록과 primary_action 분리. C13 음성 시작 추가, O17 체크박스 2개 제거 및 재인증 상태 추가. 총 필드 1174 유지.
- 가격·보존 기간·STT/PG·미정 필드·OpenAPI·실공수는 해결된 것으로 표시하지 않음.
- Figma 링크 메타데이터 읽기만 수행. 캔버스 생성·이름 변경 없음.
'''
write('LIVEPATCH_기획메모장.md',read('LIVEPATCH_기획메모장.md')+log)
old_report=read('LIVEPATCH_v5.6_변경검수보고서.md')
old_report=old_report.replace('| 필드 계약 | 1,041 | 1174 (추가 17 · 제거 2 · 수정 9) |','| 필드 계약 | 1,041 | 1,174 (v5.6-r2 현재 총수. 아래 추가 17·제거 2·수정 9는 일부 보정 작업의 집계이며 전체 버전 증분이 아님) |')
write('LIVEPATCH_v5.6_변경검수보고서.md', '# v5.7 현재 판정\n\n현재 범위·정책은 마스터 27장과 정리 폴더의 v5.7 변경검수 결과를 따른다. 아래 v5.6 검수는 이력이며 현재 완료 증거가 아니다.\n\n'+old_report)

# 목업 HTML은 기존 비주얼을 보존하며 문구·내비 범위만 정합화한다.
mock=read('LIVEPATCH_v5.6_화면목업.html')
mock=mock.replace('LIVEPATCH v5.6 화면 목업 · 3초 핵심 노출','LIVEPATCH v5.7 정책 반영 참고 목업')
mock=mock.replace('문제가 있으면 언제든 되돌릴 수 있습니다.','복원 가능 기간과 후속 변경을 확인한 뒤 요청할 수 있습니다.')
mock=mock.replace('반영 후에도 되돌릴 수 있습니다','복원 조건을 확인한 뒤 되돌리기를 요청할 수 있습니다')
mock=mock.replace('미리보기는 무료로 다시 만들 수 있으며 실제 사이트는 바뀌지 않습니다.','미리보기는 예약만 하며 하루 10회까지 생성합니다. 반영 확인 후 차감합니다.')
mock=mock.replace('음성 “반영해”, 스위치 제어로도 확인할 수 있습니다','접근성 확인도 패스키와 서버 승인 검사를 거칩니다. 음성만으로 반영하지 않습니다')
mock=mock.replace('“되돌려 줘”','“복원 확인 열어 줘”')
mock=mock.replace('<button data-f="alpha">MVP-α</button><button data-f="new">v5.6 신규</button>', '<button data-f="alpha">현재 MVP</button><button data-f="embedded">내부 통합</button><button data-f="later">후속</button><button data-f="new">기존 신규 표시</button>')
mock=mock.replace("(filt==='alpha'&&n.rel==='MVP-α')", "(filt==='alpha'&&['PILOT_REQUIRED','PAID_REQUIRED'].includes(n.scope_code))||(filt==='embedded'&&n.scope_code==='EMBEDDED')||(filt==='later'&&n.scope_code==='POST_MVP')")
nav_match=re.search(r'const NAV=(\[.*?\]);',mock,re.S)
assert nav_match,'NAV missing'
nav=json.loads(nav_match.group(1))
for item in nav:
    s=byid[item['id']];g=s.get('glance') or {}
    item['rel']=scope(s);item['q']=g.get('question',item.get('q',''))
    item['cta']=(g.get('cta') or {}).get('label',item.get('cta',''))
    item['scope_code']=s['release_current'];item['host']=s['host_screen']
mock=mock[:nav_match.start(1)]+json.dumps(nav,ensure_ascii=False)+mock[nav_match.end(1):]
banner='<div style="position:fixed;bottom:0;left:0;right:0;z-index:99999;padding:8px 16px;background:#0f172a;color:white;font:12px/1.5 sans-serif">v5.7 범위·정책 확인용 참고 목업 · 44페이지+19공용 오버레이 · 비주얼은 v5.6-r2 기반이며 구현·검수 완료 아님 · 최신 계약은 마스터 27장</div>'
mock=mock.replace('</body>',banner+'\n</body>')
write('LIVEPATCH_v5.6_화면목업.html',mock)

# 173개 ID의 현재 범위를 별도 기계 판독 파일로 저장한다.
manifest={'version':'5.7','date':DATE,'figma':{'file_key':'VwuyN75CQK9Kn0ZyIVmF4S','node_id':'0:1','page_name':'LIVEPATH_ver1.0','access':'metadata_read_confirmed','mutation':False},
 'counts':j['counts'],'policy':j['launch_policy'],
 'screens':[{'id':s['id'],'title':s['title'],'release_current':s['release_current'],'host_screen':s['host_screen'],'route':s['route'],'effective_route':s['host_route'] or s['route'],'legacy_route_exposed':False if s['host_screen'] or s['release_current']=='POST_MVP' else True,'tbd_fields':[f['key'] for f in s['fields'] if f.get('example_status')=='TBD']} for s in screens]}
dump(OUT/'LIVEPATCH_MVP범위계약_261016.json',manifest)

todo=[{'screen_id':s['id'],'screen_title':s['title'],'release_current':s['release_current'],'host_screen':s['host_screen'],'key':f['key'],'label':f['label'],'rule':f.get('rule'),'example_value':f.get('example_value')} for s in screens for f in s['fields'] if f.get('example_status')=='TBD']
dump(OUT/'LIVEPATCH_미정필드목록_261016.json',{'version':'5.7','count':len(todo),'by_scope':dict(collections.Counter(f['release_current'] for f in todo)),'fields':todo})
dump(OUT/'LIVEPATCH_화면작업인덱스_261016.json',{'version':'5.7','date':DATE,'screens':[{'id':s['id'],'title':s['title'],'route':s['route'],'effective_route':s['host_route'] or s['route'],'scope':scope(s),'release_current':s['release_current'],'host_screen':s['host_screen'],'fields':len(s['fields']),'tbd_count':sum(f.get('example_status')=='TBD' for f in s['fields']),'actions':s['actions'],'primary_action':s['primary_action'],'actual_mockup':s['mockup'],'snapshot_version':s['mockup_snapshot_version']} for s in screens]})

assert len(screens)==173 and len(all_fields)==1174
assert len(primary)==63 and len(paid)==10
assert all((ROOT/s['mockup']).exists() for s in screens)
assert all(not(set(s['actions'])-{f['key'] for f in s['fields']}) for s in screens)
assert len({s['id'] for s in screens})==len(screens)
assert all(len({f['key'] for f in s['fields']})==len(s['fields']) for s in screens)
print(json.dumps({'screens':len(screens),'fields':len(all_fields),'scope_counts':j['counts']['release_current'],'examples':j['counts']['example_status_current'],'embedded':len(embedded),'backup_files':len(list(BACKUP.iterdir()))},ensure_ascii=False))
