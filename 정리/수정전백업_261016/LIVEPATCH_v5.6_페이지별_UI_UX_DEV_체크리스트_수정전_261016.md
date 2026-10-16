# LIVEPATCH v5.6 — 화면별 UI·UX·DEV·QA 제작 체크리스트

> v5.6 JSON 계약에서 자동 생성한 **화면별 고유 체크리스트**다(v5.5의 동일 4줄 반복을 대체). 페이지 128개 + 오버레이 45개. 체크는 산출물·테스트 증거 확인 후에만 완료 처리한다.

**릴리스 표기:** `MVP-α`(클로즈드 베타 필수) · `MVP-β`(제한 상용 전 필수) · `조건부` · `LATER`. 먼저 MVP-α 화면부터 착수한다.

## 공식 웹사이트 (37개)

### M01 홈 랜딩 · `/` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: trusted_capabilities, faq_teaser
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m01_hero_demo_click`, `m01_hero_signup_click`, `m01_hero_login_nav`, `m01_cookie_preferences_nav` (PII 미포함 검증)
- [ ] **SEO:** index, follow · Organization, WebSite, SoftwareApplication · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 핵심 약속이 ‘말로 고치고 승인 후 반영’이라는 것과 다음 행동 [데모로 바로 해보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M01.png`)
- [ ] **QA:** 360/768/1440 화면·키보드 내비 통과, CTA→데모·로그인 이동, 사이트 100% 지원 오인 없음

### M02 라이브 샘플 체험 · `/demo` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 체험할 샘플 사이트, 변경 명령 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `GET /v1/public/demo-templates`, `POST /v1/demo-sessions`, `POST /v1/demo-sessions/{id}/preview` / 오류 코드 `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: sample_site, selected_element, instruction, suggestions, demo_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 체험용 안내 / axe 위반 0
- [ ] **이벤트:** `m02_sample_site_change`, `m02_before_after_change`, `m02_run_preview_click`, `m02_reset_demo_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 체험 상태가 ‘샘플 사이트 · 실제 사이트 미변경’이라는 것과 다음 행동 [미리보기 생성] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M02.png`)
- [ ] **QA:** 샘플 요소 선택→문구 변경→diff→리셋 완료, 임의 URL·운영 배포 요청 차단

### M03 데모 결과·가입 유도 · `/demo/result/:demoId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/public/demo-templates`, `POST /v1/demo-sessions`, `POST /v1/demo-sessions/{id}/preview` / 오류 코드 `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: preview_before, preview_after
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 체험 처리 상태 / axe 위반 0
- [ ] **이벤트:** `m03_signup_cta_click`, `m03_retry_demo_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 체험 결과가 ‘변경안 1건 생성 · 비용 0원’이라는 것과 다음 행동 [내 사이트 연결하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M03.png`)
- [ ] **QA:** TTL 만료 결과 미노출·새 체험 연결 정상·실제 사이트 저장 변화 없음

### M04 기능 전체 안내 · `/features` · **MVP-β**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 기능 유형 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: steps, feature_filter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m04_start_demo_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 연결 방식 비교가 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [샘플 체험하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M04.png`)
- [ ] **QA:** 지원·미지원 표현이 호환성 매트릭스와 동일, CTA 경로 일치

### M05 기능 상세 · `/features/:slug` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: feature_name, feature_status, before_after
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m05_start_feature_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 출시·실험·미지원이 ‘정확한 공개 상태’라는 것과 다음 행동 [체험/문의] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M05.png`)
- [ ] **QA:** 기능별 지원모드 안내·존재하지 않는 기능 페이지 정상 404

### M06 호환성·지원 범위 · `/compatibility` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: framework_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m06_connection_mode_change`, `m06_support_level_change`, `m06_diagnose_cta_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · TechArticle · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 지원 등급이 ‘SUPPORTED 3 · LIMITED 2 · PREVIEW_ONLY 1’이라는 것과 다음 행동 [내 사이트 진단하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M06.png`)
- [ ] **QA:** 지원되지 않는 환경을 지원으로 오표시하지 않음, 필터·접근성 정상

### M07 업종별 활용 목록 · `/use-cases` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 0·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 0건·대체 문구 2건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: industry_filter, limitations
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 실제 적용 시 주의사항 / axe 위반 0
- [ ] **이벤트:** `m07_industry_cta_nav` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 0개’라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/M07.png`)
- [ ] **QA:** 각 업종 카드 이동, 법적 보장 문구·실제 고객 오인 요소 없음

### M08 업종별 활용 상세 · `/use-cases/:industry` · **MVP-β**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: industry_title, approval_scope
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 고객 검수 책임 / axe 위반 0
- [ ] **이벤트:** `m08_consult_cta_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · Article, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 0개’라는 것과 다음 행동 [사이트 지원 여부 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M08.png`)
- [ ] **QA:** 각 업종별 제약·면책/승인 과정 표시, CTA 진단 화면 연결

### M09 사례·데모 갤러리 · `/cases` · **LATER**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 0·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 0건·대체 문구 2건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: category, case_types, case_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m09_category_change` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 데모/실제 구분이 ‘구분 유지’라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/M09.png`)
- [ ] **QA:** 비공개/미승인 사례 미노출, 필터·모바일 그리드 정상

### M10 사례 상세 · `/cases/:slug` · **LATER**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: case_title, case_source, before_after, tech_stack
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m10_case_cta_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 실제 사례/합성 데모가 ‘오인 금지’라는 것과 다음 행동 [유사 작업 상담] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M10.png`)
- [ ] **QA:** 실사용자 사진·고객명은 공개 동의 확인 후에만 표시

### M11 요금제 비교 · `/pricing` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 6개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 결제주기 / 실패 문구 1건·대체 문구 6건 검토
- [ ] **DEV:** API `GET /v1/public/plans` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: site_limit, expert_quota, refund_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 해지·환불 요약 / axe 위반 0
- [ ] **이벤트:** `m11_billing_cycle_change`, `m11_select_plan_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · SoftwareApplication+Offer(가격 버전 동기화) · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 추천이 ‘Business 월 55,000원 · 사이트 3 · 600C’라는 것과 다음 행동 [플랜 선택] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M11.png`)
- [ ] **QA:** 표시 요금/서버 주문금액 일치, 지원금 확정 할인처럼 보이지 않음

### M12 상품·플랜 상세 · `/pricing/:planId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 결제주기 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `GET /v1/public/plans` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: plan_name, site_count
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m12_billing_cycle_change`, `m12_checkout_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 최종 청구액이 ‘서버 견적값 또는 입력 금액’이라는 것과 다음 행동 [이 플랜 선택] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M12.png`)
- [ ] **QA:** 없는 planId 404·플랜별 기능과 실제 권한 스키마 정합

### M13 보안·데이터 보호 안내 · `/security` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: security_sections
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m13_data_rights_nav`, `m13_security_contact_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 데이터 보존 기간이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [보안 문의] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M13.png`)
- [ ] **QA:** 데이터 보존·접근 범위 실제 서비스 정책과 불일치 없음

### M14 자주 묻는 질문 · `/faq` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 질문 카테고리 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: faq_search, faq_category, faq_items
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m14_contact_cta_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · FAQPage · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 1개 · 질문 카테고리 외’라는 것과 다음 행동 [해결되지 않았나요?] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M14.png`)
- [ ] **QA:** 질문 열기·검색·키보드 조작, 콘텐츠가 고객지원 안내와 일치

### M15 파트너 프로그램 소개 · `/partners` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m15_partner_apply_click`, `m15_agreement_preview_nav` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 수수료 산정 기준이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [파트너 신청하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M15.png`)
- [ ] **QA:** 가설 수수료를 확정 정책처럼 제시하지 않음

### M16 파트너 신청 · `/partners/apply` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 9·조작 1·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 회사·사업체명, 사업 유형, 담당자명, 업무 이메일, 현재 관리 사이트 수, 개인정보 수집 동의 / 실패 문구 1건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/public/partner-applications` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: company_name, contact_name, additional_info
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: company_name=organization, contact_name=name, contact_email=email, phone=tel, website=url / axe 위반 0
- [ ] **이벤트:** `m16_company_type_change`, `m16_submit_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 6개 · 회사·사업체명 외’라는 것과 다음 행동 [신청서 보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M16.png`)
- [ ] **QA:** 중복 제출에 중복 신청 생성 없음, 개인정보 동의 이력 확인

### M17 문의 접수 · `/contact` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 7·조작 1·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 문의 유형, 성함/담당자명, 회신 이메일, 문의 제목, 문의 내용, 개인정보 수집 동의 / 실패 문구 1건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/public/inquiries` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: full_name, subject, content
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: email=email / axe 위반 0
- [ ] **이벤트:** `m17_contact_category_change`, `m17_send_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 6개 · 문의 유형 외’라는 것과 다음 행동 [문의 접수] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M17.png`)
- [ ] **QA:** 오류 후 입력 보존, 비밀값 전송 가이드·접수 중복 차단

### M18 공지사항 목록 · `/notices` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 0·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 공지 분류 / 실패 문구 0건·대체 문구 1건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: notice_type, search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m18_notice_pager_nav` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 공지 목록이 ‘128건 · 확인 필요 3건’이라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/M18.png`)
- [ ] **QA:** 게시 전 초안 비노출·중요 공지 우선순위 정확

### M19 공지사항 상세 · `/notices/:noticeId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 0·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 0건·대체 문구 5건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: notice_title, notice_date, notice_body, prev_next
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 게시·수정 시각이 ‘KST 표기’라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/M19.png`)
- [ ] **QA:** 스크립트 삽입 차단·공개 취소 시 상태 정확

### M20 이용약관 · `/legal/terms` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 약관 버전 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: table_contents, policy_body
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m20_policy_version_change`, `m20_print_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 시행일이 ‘2026-10-15 14:30 (KST)’라는 것과 다음 행동 [인쇄하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M20.png`)
- [ ] **QA:** 결제 약관 버전과 공개 문서 내용 일치

### M21 개인정보 처리방침 · `/legal/privacy` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 0·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 개인정보방침 버전 / 실패 문구 0건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m21_policy_version_change`, `m21_request_rights_nav` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 수집 항목·목적이 ‘128건 · 확인 필요 3건’이라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/M21.png`)
- [ ] **QA:** 실제 데이터 처리 흐름과 공개 문서 일치 확인

### M22 환불·해지 정책 · `/legal/refund` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 4개 시각 위계 / 위험 조작 확인 단계: 환불 문의
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: cancellation_effect, policy_version
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 해지 적용 시점 / axe 위반 0
- [ ] **이벤트:** `m22_contact_cta_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · WebPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 환불 기준이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [환불 문의] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M22.png`)
- [ ] **QA:** 결제 전 고객이 환불 조건에 접근 가능

### M23 쿠키·추적 설정 · `/privacy/preferences` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: essential_cookies, cookie_details
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m23_analytics_consent_change`, `m23_marketing_consent_change`, `m23_save_preferences_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 필수 항목이 ‘사용 거절 불가 사유’라는 것과 다음 행동 [설정 저장] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M23.png`)
- [ ] **QA:** 동의 철회 뒤 비필수 추적 중단·재방문 선택 유지

### M24 로그인 · `/login` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 3·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 이메일, 비밀번호 / 실패 문구 3건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/auth/sessions`, `GET /v1/auth/oidc/{provider}/start` / 오류 코드 `AUTH_REQUIRED`, `RATE_LIMITED` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: email=username, password=current-password / axe 위반 0
- [ ] **이벤트:** `m24_password_visibility_change`, `m24_login_click`, `m24_social_kakao_click`, `m24_social_google_click`, `m24_forgot_link_nav`, `m24_signup_link_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 로그인 방식이 ‘이메일 · 카카오 · Google’라는 것과 다음 행동 [로그인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M24.png`)
- [ ] **QA:** 오픈 리다이렉트 방어·권한 없는 콘솔 이동 차단

### M25 회원가입 · `/signup` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 9·조작 2·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 이메일(로그인 ID), 비밀번호, 이름/표시명, 만 14세 이상입니다, 이용약관 동의, 개인정보 처리방침 확인 / 실패 문구 2건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/auth/signups` / 오류 코드 `RATE_LIMITED` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: password_visibility, display_name, age_14_confirm, partner_referral_code
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: email=email, password=new-password, display_name=name / axe 위반 0
- [ ] **이벤트:** `m25_password_visibility_change`, `m25_signup_click`, `m25_social_signup_click`, `m25_login_link_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 가입 소요가 ‘필수 4항목 · 약 1분’이라는 것과 다음 행동 [계정 만들기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M25.png`)
- [ ] **QA:** 중복 생성 없음·필수 동의 누락 방지·첫 온보딩 정상

### M26 이메일 인증 상태 · `/verify-email` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `POST /v1/auth/email-verifications/{token}` / 오류 코드 `SITE_NOT_VERIFIED`, `RATE_LIMITED` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: verified_email
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 인증 상태 / axe 위반 0
- [ ] **이벤트:** `m26_resend_email_click`, `m26_change_email_nav`, `m26_go_login_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 인증 상태가 ‘메일 발송됨 · 10분 내 확인’이라는 것과 다음 행동 [인증 메일 다시 보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M26.png`)
- [ ] **QA:** 만료 링크 재사용 불가·성공 후 목적지 유지

### M27 비밀번호 재설정 신청 · `/forgot-password` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 가입한 이메일 / 실패 문구 1건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/auth/password-resets` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: email=email / axe 위반 0
- [ ] **이벤트:** `m27_send_reset_click`, `m27_back_login_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 1개 · 가입한 이메일 외’라는 것과 다음 행동 [재설정 메일 보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M27.png`)
- [ ] **QA:** 존재/미존재 이메일에 동일 응답·유출 방지

### M28 새 비밀번호 설정 · `/reset-password` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 새 비밀번호, 새 비밀번호 확인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `PUT /v1/auth/password-resets/{token}` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: new_password=new-password, new_password_confirm=new-password / aria-live: 링크 유효성 / axe 위반 0
- [ ] **이벤트:** `m28_reset_submit_click`, `m28_request_again_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 링크 유효성이 ‘만료’라는 것과 다음 행동 [새 비밀번호 저장] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M28.png`)
- [ ] **QA:** 토큰 재사용 불가·세션 무효화 정책 검증

### M29 인증 연동 결과 · `/auth/result` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: provider, account
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 연동 결과 / axe 위반 0
- [ ] **이벤트:** `m29_retry_auth_click`, `m29_return_to_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 연동 결과가 ‘성공’이라는 것과 다음 행동 [다시 시도] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M29.png`)
- [ ] **QA:** 잘못된 state 차단·중복 연동 계정 안내

### M30 결제 주문 확인 · `/checkout` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 6·조작 1·표시 6개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 결제 이메일, 결제 수단, 결제·정기구독 약관 동의 / 실패 문구 1건·대체 문구 6건 검토
- [ ] **DEV:** API `POST /v1/checkout/intents`, `GET /v1/checkout/intents/{id}` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `AUTH_REQUIRED` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: chosen_plan, billing_cycle, site_count, coupon_code, business_reg_no, auto_renew, withdrawal_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: buyer_email=email / aria-live: 자동갱신 안내, 청약철회·환불 안내 / axe 위반 0
- [ ] **이벤트:** `m30_payment_method_change`, `m30_receipt_type_change`, `m30_pay_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 최종 결제 금액이 ‘55,000원 / 월 (VAT 포함)’이라는 것과 다음 행동 [결제 계속] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M30.png`)
- [ ] **QA:** 클라이언트 금액 변조로 결제 불가·중복 intent 처리

### M31 결제 결과·확인 중 · `/checkout/result` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `POST /v1/checkout/intents`, `GET /v1/checkout/intents/{id}` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `AUTH_REQUIRED` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 결제 확인 상태 / axe 위반 0
- [ ] **이벤트:** `m31_retry_check_click`, `m31_go_console_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 결제 상태가 ‘확인 중 — 완료 아님’이라는 것과 다음 행동 [결제 상태 다시 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M31.png`)
- [ ] **QA:** 웹훅 지연 시 거짓 성공 없음·중복 결제 안내 정확

### M32 접근할 수 없는 링크(404) · `/404` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: missing_path
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m32_home_link_click`, `m32_search_help_nav`, `m32_support_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 상태가 ‘페이지를 찾을 수 없음’이라는 것과 다음 행동 [홈으로] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M32.png`)
- [ ] **QA:** 존재하지 않는 경로의 올바른 HTTP 상태 반환

### M33 일시적 서버 오류(500) · `/error` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m33_retry_click`, `m33_home_link_nav`, `m33_status_link_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 상태가 ‘일시 오류 · 데이터 변경 없음’이라는 것과 다음 행동 [다시 시도] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M33.png`)
- [ ] **QA:** 고객에 stack trace 비노출·재시도 안전

### M34 점검·이용 제한 공지 · `/maintenance` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 점검 상황 / axe 위반 0
- [ ] **이벤트:** `m34_retry_click` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 점검 종료 예정이 ‘10월 16일 03:00 (KST)’라는 것과 다음 행동 [다시 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M34.png`)
- [ ] **QA:** 점검 중 무단 배포 가능하다고 보이지 않음

### M35 팀 초대 수락 · `/invite/:token` · **조건부** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 4개 시각 위계 / 위험 조작 확인 단계: 초대 거절
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/invitations/{token}`, `POST /v1/invitations/{token}/accept` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSR(no-store) 또는 CSR — 개인화/토큰 화면 / 예시값 TBD 해소: org_name, inviter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 부여될 역할 / axe 위반 0
- [ ] **이벤트:** `m35_accept_click`, `m35_decline_click`, `m35_switch_account_nav` (PII 미포함 검증)
- [ ] **SEO:** noindex, nofollow
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 부여될 역할이 ‘SITE_EDITOR · 블루치과의원’이라는 것과 다음 행동 [초대 수락] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M35.png`)
- [ ] **QA:** 만료/재사용/타 계정 수락 차단, 가입→수락 복귀 E2E, 수락 후 권한 즉시 반영

### M36 가이드·리소스 허브 · `/guides` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: guide_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `m36_category_filter_change`, `m36_industry_filter_change`, `m36_cta_demo_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · CollectionPage, BreadcrumbList · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 최근 업데이트가 ‘2026-10-15 14:30 (KST)’라는 것과 다음 행동 [데모로 직접 해보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M36.png`)
- [ ] **QA:** LCP·CLS 기준 충족, 구조화데이터 검증 통과, 빈 카테고리 처리

### M37 가이드 상세 · `/guides/:slug` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 SSG/ISR + 섹션 단위 지연 하이드레이션 / 예시값 TBD 해소: summary, toc, limitations
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 지원 범위·제약 / axe 위반 0
- [ ] **이벤트:** `m37_cta_signup_click` (PII 미포함 검증)
- [ ] **SEO:** index, follow · Article, HowTo/FAQPage(해당 시) · title/description/canonical/OG
- [ ] **성능:** LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1 (p75 실사용자), 초기 JS ≤ 170KB(gzip)
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 0개’라는 것과 다음 행동 [내 사이트로 시작하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/M37.png`)
- [ ] **QA:** 구조화데이터 오류 0, 모바일 가독성, 목차 앵커 이동·키보드 접근

## 고객 콘솔 (44개)

### C01 콘솔 홈·대시보드 · `/app` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 현재 조직 / 실패 문구 2건·대체 문구 5건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: current_org, active_site, alerts
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 장애·만료 알림 / axe 위반 0
- [ ] **이벤트:** `c01_current_org_change`, `c01_active_site_change`, `c01_new_site_click`, `c01_launch_studio_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 확인할 일이 ‘승인 대기 1건’이라는 것과 다음 행동 [눌러서 말하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C01.png`)
- [ ] **QA:** 첫 로그인 후 연결 CTA, 권한별 조회·새로고침 일치

### C02 처음 시작 온보딩 · `/app/onboarding` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 3·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 조직 이름 / 실패 문구 3건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: step_progress, profile_name, organization_name, user_role
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: profile_name=name, organization_name=organization / aria-live: 안전 배포 원칙 안내 / axe 위반 0
- [ ] **이벤트:** `c02_continue_click`, `c02_skip_site_click`, `c02_delegate_setup_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 진행이 ‘3 / 5 단계 · 사이트 연결’이라는 것과 다음 행동 [다음 단계] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C02.png`)
- [ ] **QA:** 새 계정·중단 계정·초대 계정별 흐름 구분

### C03 내 사이트 목록 · `/app/sites` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/orgs/{orgId}/sites`, `GET /v1/sites/{siteId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_search, site_quota
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c03_status_filter_change`, `c03_mode_filter_change`, `c03_add_site_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사이트가 ‘2 / 3 사용 · 1곳 확인 필요’라는 것과 다음 행동 [사이트 추가] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C03.png`)
- [ ] **QA:** 사이트 0/많음/오류/다른 조직 권한 상태 검증

### C04 사이트 등록 · `/app/sites/new` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 사이트 표시 이름, 운영 사이트 URL, 접속 환경, 관리 권한 보유 확인 / 실패 문구 1건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/orgs/{orgId}/sites` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: display_name
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: display_name=name / axe 위반 0
- [ ] **이벤트:** `c04_environment_change`, `c04_platform_guess_change`, `c04_create_site_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 4개 · 사이트 표시 이름 외’라는 것과 다음 행동 [사이트 등록] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C04.png`)
- [ ] **QA:** 사설망 URL·도메인 중복·타 조직 추가 실패 처리

### C05 사이트 소유권 증명 · `/app/sites/:siteId/verify` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 확인 방식 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `POST /v1/sites/{id}/ownership-challenges`, `POST /v1/sites/{id}/ownership-challenges/{cid}/verify` / 오류 코드 `SITE_NOT_VERIFIED`, `RATE_LIMITED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_domain, proof_value, proof_instructions, token_expiry, last_error
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: proof_value=off / aria-live: 검증 실패 사유 / axe 위반 0
- [ ] **이벤트:** `c05_verification_method_change`, `c05_verify_now_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 소유권이 ‘미확인 · DNS 전파 대기’라는 것과 다음 행동 [소유권 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C05.png`)
- [ ] **QA:** 미검증 사이트 운영 수정 불가·만료 challenge 재사용 안 됨

### C06 연결 방식 선택 · `/app/sites/:siteId/connect` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 선택 연결 방식 / 실패 문구 2건·대체 문구 5건 검토
- [ ] **DEV:** API `POST /v1/sites/{id}/connectors`, `POST /v1/sites/{id}/connectors/{cid}/probe` / 오류 코드 `SITE_COMPATIBILITY_LIMITED`, `UNSUPPORTED_ACTION`, `RATE_LIMITED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_id, support_level
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c06_mode_choice_change`, `c06_continue_click`, `c06_delegate_setup_invite_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 권장 방식이 ‘Mode A · Git 연동’이라는 것과 다음 행동 [연결 설정] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C06.png`)
- [ ] **QA:** 연결 모드 차이를 사용자에게 설명할 수 있음

### C07 연결 인증·설정 · `/app/sites/:siteId/connect/setup` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 11·조작 2·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 커넥터 종류, 요청 권한 목록 / 실패 문구 2건·대체 문구 0건 검토
- [ ] **DEV:** API `POST /v1/sites/{id}/connectors`, `POST /v1/sites/{id}/connectors/{cid}/probe` / 오류 코드 `SITE_COMPATIBILITY_LIMITED`, `UNSUPPORTED_ACTION`, `RATE_LIMITED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: account_scope, repository, branch, root_path, host, username, permission_scope
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: credential=off / axe 위반 0
- [ ] **이벤트:** `c07_connector_type_change`, `c07_account_scope_change`, `c07_repository_change`, `c07_branch_change`, `c07_permission_scope_change`, `c07_test_connection_click`, `c07_save_connection_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 2개 · 커넥터 종류 외’라는 것과 다음 행동 [연결 테스트] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C07.png`)
- [ ] **QA:** 브라우저 로그/분석에 키 원문 노출 0·취소 후 상태 복구

### C08 연결 진단 결과 · `/app/sites/:siteId/diagnostics` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 8개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 8건 검토
- [ ] **DEV:** API `GET /v1/sites/{id}/compatibility` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_platform, auth_status, render_grade, deploy_capability
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 연결 상태, 인증·권한 검사, 브라우저 렌더 호환성 / axe 위반 0
- [ ] **이벤트:** `c08_rerun_click`, `c08_continue_test_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 진단 결과가 ‘LIMITED · 텍스트·이미지 가능’이라는 것과 다음 행동 [테스트 수정하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C08.png`)
- [ ] **QA:** 권한 없는 재검사 차단·지원 상태와 Studio 기능 일치

### C09 테스트 수정·복구 확인 · `/app/sites/:siteId/test-patch` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 테스트할 페이지, 테스트 요소, 시험 명령 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `POST /v1/jobs (testPatch=true)`, `POST /v1/deployments/{id}/rollback` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: target_page, test_element, sample_instruction, restore_check
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 복원 가능 검증 / axe 위반 0
- [ ] **이벤트:** `c09_target_page_change`, `c09_test_element_change`, `c09_test_execute_click`, `c09_complete_setup_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 복구 확인이 ‘PASS · 테스트 변경 원복 완료’라는 것과 다음 행동 [사이트 연결 완료] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C09.png`)
- [ ] **QA:** 테스트 실패 환경에서 Studio 운영 배포 CTA 비활성

### C10 사이트 개요 · `/app/sites/:siteId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 6개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 현재 환경 / 실패 문구 2건·대체 문구 6건 검토
- [ ] **DEV:** API `GET /v1/orgs/{orgId}/sites`, `GET /v1/sites/{siteId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_identity, support_mode, editing_rights
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 최근 배포 / axe 위반 0
- [ ] **이벤트:** `c10_current_environment_change`, `c10_edit_site_click`, `c10_settings_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 지원 등급이 ‘SUPPORTED · 원본 수정’이라는 것과 다음 행동 [Studio 열기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C10.png`)
- [ ] **QA:** 동일 도메인의 조직 간 데이터 혼재 없음

### C11 사이트 페이지 탐색기 · `/app/sites/:siteId/pages` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/orgs/{orgId}/sites`, `GET /v1/sites/{siteId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: page_search, page_url, page_title, robots_note
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 수집 제한 안내 / axe 위반 0
- [ ] **이벤트:** `c11_page_status_filter_change`, `c11_open_selected_click`, `c11_rescan_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 선택 페이지 주소가 ‘검증 호스트’라는 것과 다음 행동 [선택 페이지 편집] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C11.png`)
- [ ] **QA:** 금지/비공개 URL 탐색 차단·페이지 선택 맥락 유지

### C12 사이트 설정·연결 관리 · `/app/sites/:siteId/settings` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 4개 시각 위계 / 위험 조작 확인 단계: 연결 해제
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 사이트 이름, 기본 편집 환경 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/orgs/{orgId}/sites`, `GET /v1/sites/{siteId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_name, site_url, connector_status, connector_scope, webhook_status
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 연동 상태 / axe 위반 0
- [ ] **이벤트:** `c12_environment_change`, `c12_auto_deploy_change`, `c12_retest_click`, `c12_disconnect_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 연동 상태가 ‘연결 유효성’이라는 것과 다음 행동 [연결 재진단] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C12.png`)
- [ ] **QA:** 진행 중 작업 보호·연결 해제 후 편집 차단

### C13 Visual Patch Studio 편집 · `/app/sites/:siteId/studio` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 7·조작 6·표시 6개 시각 위계 / 위험 조작 확인 단계: 배포 승인 요청, 운영에 반영, 복원하기
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 편집 페이지 경로, 화면 크기, 수정 명령, 명령 유형, 적용 범위 / 실패 문구 6건·대체 문구 6건 검토
- [ ] **DEV:** API `POST /v1/sites/{id}/captures`, `POST /v1/source-mappings/resolve`, `POST /v1/jobs`, `GET /v1/jobs/{id}/events (SSE)`, `POST /v1/jobs/{id}/approvals`, `POST /v1/jobs/{id}/deploy` / 오류 코드 `SITE_NOT_VERIFIED`, `SITE_COMPATIBILITY_LIMITED`, `UNSUPPORTED_ACTION`, `SOURCE_AMBIGUOUS`, `MAPPING_LOW_CONFIDENCE`, `STALE_SOURCE`, `CREDIT_INSUFFICIENT`, `JOB_VALIDATION_FAILED`, `DEPLOYMENT_IN_PROGRESS` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_context, presence_indicator, page_path, target_descriptor, instruction_text
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 동시 편집자, 원본 매핑 신뢰도, 반영 방식 / axe 위반 0
- [ ] **이벤트:** `c13_viewport_change`, `c13_selection_mode_change`, `c13_freeze_toggle_change`, `c13_instruction_type_change`, `c13_scope_change`, `c13_create_preview_click`, `c13_compare_click`, `c13_validate_click`, `c13_request_approval_click`, `c13_deploy_click`, `c13_rollback_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 바꿀 수 있는 곳이 ‘번호 1~12 · 원본 수정’이라는 것과 다음 행동 [말로 바꾸기(마이크)] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C13.png`)
- [ ] **QA:** 잘못된 원본 편집 0 목표·오프라인 복귀·배포 미승인 차단

### C14 작업 목록 · `/app/jobs` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/jobs`, `GET /v1/jobs/{id}`, `GET /v1/jobs/{id}/artifacts` / 오류 코드 `FORBIDDEN`, `JOB_VALIDATION_FAILED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: job_search, site_filter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c14_site_filter_change`, `c14_status_filter_change`, `c14_date_range_change`, `c14_job_detail_nav`, `c14_new_job_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 진행 중이 ‘2건 · 실패 1건’이라는 것과 다음 행동 [새 수정 시작] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C14.png`)
- [ ] **QA:** 20개 이상 작업 검색·새로고침·권한별 결과 정상

### C15 작업 상세·증빙 · `/app/jobs/:jobId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 9개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 9건 검토
- [ ] **DEV:** API `GET /v1/jobs`, `GET /v1/jobs/{id}`, `GET /v1/jobs/{id}/artifacts` / 오류 코드 `FORBIDDEN`, `JOB_VALIDATION_FAILED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: target_site, instruction, target_element
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c15_request_approval_click`, `c15_support_ticket_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 작업 상태가 ‘검증 통과 · 승인 대기’라는 것과 다음 행동 [승인 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C15.png`)
- [ ] **QA:** 실패 시 근거·복구 경로 명시, 타 조직 Job 조회 불가

### C16 승인 대기함 · `/app/approvals` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/approvals?status=pending`, `POST /v1/jobs/{id}/approvals`, `POST /v1/jobs/{id}/approvals/reject` / 오류 코드 `STALE_SOURCE`, `FORBIDDEN`, `JOB_VALIDATION_FAILED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_filter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c16_approval_filter_change`, `c16_site_filter_change`, `c16_review_action_click`, `c16_bulk_approve_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 승인 대기가 ‘3건 · 가장 오래된 2시간’이라는 것과 다음 행동 [검토하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C16.png`)
- [ ] **QA:** Editor에게 승인 버튼 없음·만료 작업 제외

### C17 승인 상세·결재 · `/app/approvals/:jobId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 6개 시각 위계 / 위험 조작 확인 단계: 반려하기
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 배포 대상 재확인 / 실패 문구 2건·대체 문구 6건 검토
- [ ] **DEV:** API `GET /v1/approvals?status=pending`, `POST /v1/jobs/{id}/approvals`, `POST /v1/jobs/{id}/approvals/reject` / 오류 코드 `STALE_SOURCE`, `FORBIDDEN`, `JOB_VALIDATION_FAILED` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: target_environment, source_hash, risk_notice, approval_comment
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 예상 영향 범위 / axe 위반 0
- [ ] **이벤트:** `c17_approve_click`, `c17_reject_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 검증 결과가 ‘S0~S5 PASS · 운영 환경’이라는 것과 다음 행동 [승인하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C17.png`)
- [ ] **QA:** STALE_SOURCE에서 승인 불가·승인자 권한 재확인

### C18 배포 이력 목록 · `/app/deployments` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 1개 시각 위계 / 위험 조작 확인 단계: 상세/복원
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/deployments`, `POST /v1/deployments/{id}/rollback` / 오류 코드 `DEPLOYMENT_IN_PROGRESS`, `POST_DEPLOY_VERIFY_FAILED`, `ROLLBACK_REQUIRES_REVIEW`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_filter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c18_site_filter_change`, `c18_environment_change`, `c18_date_range_change`, `c18_deploy_status_change`, `c18_deployment_detail_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 최근 배포가 ‘확인됨 12 · 확인 필요 1’이라는 것과 다음 행동 [상세/복원] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C18.png`)
- [ ] **QA:** 완료/부분실패/복원예정 구분·시간대 일치

### C19 배포 상세·복원 · `/app/deployments/:deploymentId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 7개 시각 위계 / 위험 조작 확인 단계: 복원 요청
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 7건 검토
- [ ] **DEV:** API `GET /v1/deployments`, `POST /v1/deployments/{id}/rollback` / 오류 코드 `DEPLOYMENT_IN_PROGRESS`, `POST_DEPLOY_VERIFY_FAILED`, `ROLLBACK_REQUIRES_REVIEW`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: original_hash, deployed_hash, status, rollback_target, rollback_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 운영 상태 / axe 위반 0
- [ ] **이벤트:** `c19_rollback_target_change`, `c19_request_rollback_click`, `c19_support_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사후 점검이 ‘정상 · 10:42 확인’이라는 것과 다음 행동 [복원 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C19.png`)
- [ ] **QA:** 복원 후 검증·부분 실패가 성공으로 표시되지 않음

### C20 크레딧 잔액 개요 · `/app/credits` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 6개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 6건 검토
- [ ] **DEV:** API `GET /v1/credits/ledger`, `GET /v1/credits/summary` / 오류 코드 `CREDIT_INSUFFICIENT`, `HOLD_EXPIRED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c20_purchase_credits_click`, `c20_history_nav` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사용 가능 크레딧이 ‘480C (HOLD 20C 별도)’라는 것과 다음 행동 [추가 구매] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C20.png`)
- [ ] **QA:** HOLD 실패/해제 시 잔액 정합·중복 차감 없음

### C21 크레딧 거래 원장 · `/app/credits/history` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/credits/ledger`, `GET /v1/credits/summary` / 오류 코드 `CREDIT_INSUFFICIENT`, `HOLD_EXPIRED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: job_id
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c21_date_range_change`, `c21_transaction_type_change`, `c21_export_history_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 거래 원장이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [내역 내려받기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C21.png`)
- [ ] **QA:** 원본 원장 불변·거래 합계=현재 잔액 규칙 설명

### C22 크레딧 추가 구매 · `/app/credits/purchase` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 크레딧 상품, 구매 수량, 추가 결제 동의 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `GET /v1/credits/ledger`, `GET /v1/credits/summary` / 오류 코드 `CREDIT_INSUFFICIENT`, `HOLD_EXPIRED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: package_choice, expiry_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 사용·만료 조건 / axe 위반 0
- [ ] **이벤트:** `c22_package_choice_change`, `c22_checkout_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 결제 금액이 ‘33,000원 · 300C’라는 것과 다음 행동 [구매하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C22.png`)
- [ ] **QA:** 결제 실패/중복 callback 시 중복 지급 없음

### C23 구독·계약 현황 · `/app/billing` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 7개 시각 위계 / 위험 조작 확인 단계: 구독 해지
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 7건 검토
- [ ] **DEV:** API `GET /v1/billing/subscription`, `GET /v1/billing/invoices` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: current_plan, billing_period, connected_sites, payment_method
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c23_change_plan_click`, `c23_cancel_plan_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 현재 플랜이 ‘Business · 11월 15일 갱신’이라는 것과 다음 행동 [플랜 변경] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C23.png`)
- [ ] **QA:** 결제 담당자 외 변경 불가·표시 금액/기간 일치

### C24 플랜 변경 · `/app/billing/change-plan` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 4개 시각 위계 / 위험 조작 확인 단계: 변경 확정
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 변경할 플랜, 결제 주기 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/billing/subscription`, `GET /v1/billing/invoices` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: current_plan, new_plan, effective_date, site_limit_warning
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 사이트 수 초과 영향 / axe 위반 0
- [ ] **이벤트:** `c24_new_plan_change`, `c24_billing_period_change`, `c24_confirm_change_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 일할 계산·환불 예상이 ‘서버 견적값 또는 입력 금액’이라는 것과 다음 행동 [변경 확정] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C24.png`)
- [ ] **QA:** 새 플랜 적용 시점·금액·한도 정확

### C25 결제수단 관리 · `/app/billing/payment-methods` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 2개 시각 위계 / 위험 조작 확인 단계: 결제수단 삭제
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 기본 결제수단 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/billing/subscription`, `GET /v1/billing/invoices` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: default_method, billing_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 다음 청구 적용 시점 / axe 위반 0
- [ ] **이벤트:** `c25_default_method_change`, `c25_add_card_click`, `c25_remove_card_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 1개 · 기본 결제수단 외’라는 것과 다음 행동 [새 결제수단 등록] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C25.png`)
- [ ] **QA:** 카드 원문 프런트/로그 미보관·등록 실패 복구

### C26 청구·영수증·증빙 · `/app/billing/invoices` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/billing/subscription`, `GET /v1/billing/invoices` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c26_date_range_change`, `c26_document_type_change`, `c26_download_click`, `c26_support_invoice_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 발행 내역이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [다운로드] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C26.png`)
- [ ] **QA:** 사업자별 증빙 가시성·다운로드 권한 및 기간 검증

### C27 구독 해지·정지 · `/app/billing/cancel` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 4개 시각 위계 / 위험 조작 확인 단계: 해지 신청
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 해지 적용 시점, 구독 해지 확인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/billing/subscription`, `GET /v1/billing/invoices` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: current_plan, cancel_effect, site_access_effect, credit_expiration, cancel_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 사이트 접근 영향, 남은 크레딧 처리 / axe 위반 0
- [ ] **이벤트:** `c27_cancel_effect_change`, `c27_cancel_reason_change`, `c27_downgrade_option_nav`, `c27_cancel_submit_click`, `c27_keep_subscription_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 이용 종료일이 ‘11월 14일까지 이용 가능’이라는 것과 다음 행동 [해지 신청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C27.png`)
- [ ] **QA:** 갱신 중단 후 서비스 종료일·권한 표시 정확

### C28 팀원·초대 목록 · `/app/team` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/orgs/{orgId}/members`, `POST /v1/orgs/{orgId}/invitations` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c28_role_filter_change`, `c28_invite_member_click`, `c28_remove_member_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 팀원 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [팀원 초대] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C28.png`)
- [ ] **QA:** 자기 승격·최종 Owner 삭제 차단

### C29 팀원 초대·권한 설정 · `/app/team/invite` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 초대 이메일, 초대 역할, 접근 사이트, 초대 만료일 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/invitations/{token}`, `POST /v1/invitations/{token}/accept` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_scope, message
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: invite_email=email / axe 위반 0
- [ ] **이벤트:** `c29_invite_role_change`, `c29_site_scope_change`, `c29_invite_expiry_change`, `c29_send_invite_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 권한 미리보기가 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [초대 보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C29.png`)
- [ ] **QA:** 다른 조직 사이트 지정 금지·초대 토큰 일회성

### C30 알림 센터 · `/app/notifications` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/notifications` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c30_category_filter_change`, `c30_mark_read_click`, `c30_target_link_nav`, `c30_preferences_nav` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 읽지 않은 알림이 ‘1,240’이라는 것과 다음 행동 [읽음 처리] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C30.png`)
- [ ] **QA:** 타 조직 알림 교차 노출 없음·누락 알림 조회 가능

### C31 1:1 문의 목록 · `/app/support` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/support/tickets`, `POST /v1/support/tickets` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: ticket_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c31_ticket_filter_change`, `c31_new_ticket_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 답변 대기가 ‘1건 · 평균 응답 4시간’이라는 것과 다음 행동 [문의하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C31.png`)
- [ ] **QA:** 고객간 문의 접근 차단·답변 표시 일관

### C32 새 문의 작성 · `/app/support/new` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 7·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 문의 유형, 문의 제목, 문의 내용 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/support/tickets`, `POST /v1/support/tickets` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_id, job_id, subject, body
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c32_category_change`, `c32_site_id_change`, `c32_send_ticket_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 3개 · 문의 유형 외’라는 것과 다음 행동 [문의 접수] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C32.png`)
- [ ] **QA:** 고객 동의 없이 캡처 자동 전송하지 않음

### C33 문의 상세·대화 · `/app/support/:ticketId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `GET /v1/support/tickets`, `POST /v1/support/tickets` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: reply_text
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 처리 상태 / axe 위반 0
- [ ] **이벤트:** `c33_send_reply_click`, `c33_reopen_ticket_click`, `c33_related_job_nav` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 처리 상태가 ‘접수’라는 것과 다음 행동 [답변 보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C33.png`)
- [ ] **QA:** 운영 내부 메모 비노출·권한 밖 첨부 접근 방어

### C34 전문가 작업 요청 · `/app/expert-tickets/new` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 8·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 대상 사이트, 요청 유형, 작업 제목, 변경 요청 상세, 원하는 완료 결과, 추가 과금 안내 확인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `POST /v1/expert-tickets`, `GET /v1/expert-tickets/{id}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: site_id, subject, description, desired_outcome, included_hours
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c34_site_id_change`, `c34_request_category_change`, `c34_submit_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 잔여 포함 시간이 ‘실제 계약’이라는 것과 다음 행동 [전문가 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C34.png`)
- [ ] **QA:** 사전 확인 없는 유료 작업 청구 불가

### C35 전문가 진행 상세 · `/app/expert-tickets/:ticketId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 5건 검토
- [ ] **DEV:** API `POST /v1/expert-tickets`, `GET /v1/expert-tickets/{id}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: assignee, time_budget, customer_comment
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c35_accept_result_click`, `c35_reopen_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 담당 전문가/팀이 ‘개인정보 정책’이라는 것과 다음 행동 [완료 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C35.png`)
- [ ] **QA:** 시간 총계·작업 승인·잔여시간 일치

### C36 개인 프로필·보안 · `/app/settings/profile` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 표시 이름, 언어, 시간대 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET/PATCH /v1/me`, `GET/PATCH /v1/orgs/{orgId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: display_name, email, language
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: display_name=name, phone=tel / axe 위반 0
- [ ] **이벤트:** `c36_language_change`, `c36_timezone_change`, `c36_change_password_click`, `c36_save_profile_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 로그인된 기기가 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [비밀번호 변경] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C36.png`)
- [ ] **QA:** 비정상 세션 종료·재인증 실패 시 안전 유지

### C37 조직 정보·사업자 설정 · `/app/settings/organization` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 7·조작 1·표시 0개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 조직명, 증빙 이메일 / 실패 문구 1건·대체 문구 0건 검토
- [ ] **DEV:** API `GET/PATCH /v1/me`, `GET/PATCH /v1/orgs/{orgId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: organization_name, business_number, representative, business_address
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: organization_name=organization, billing_email=email, contact_phone=tel / axe 위반 0
- [ ] **이벤트:** `c37_save_organization_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 2개 · 조직명 외’라는 것과 다음 행동 [조직 정보 저장] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C37.png`)
- [ ] **QA:** 조직 변경 후 세금 증빙·권한 영향 정확

### C38 알림 수신 설정 · `/app/settings/notifications` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET/PATCH /v1/me`, `GET/PATCH /v1/orgs/{orgId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: email_security
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c38_email_deploy_change`, `c38_email_approval_change`, `c38_email_credit_change`, `c38_email_support_change`, `c38_save_prefs_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 보안 안내가 ‘필수 알림 중단 불가’라는 것과 다음 행동 [설정 저장] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C38.png`)
- [ ] **QA:** 설정 변경 후 채널/이벤트 일치, 필수 알림 유지

### C39 연동·키 관리 · `/app/settings/integrations` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 3·표시 2개 시각 위계 / 위험 조작 확인 단계: 연결 해제
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 3건·대체 문구 2건 검토
- [ ] **DEV:** API `GET/PATCH /v1/me`, `GET/PATCH /v1/orgs/{orgId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: key_label, scopes
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: api_key=off / axe 위반 0
- [ ] **이벤트:** `c39_new_connector_click`, `c39_api_provider_change`, `c39_test_integration_click`, `c39_revoke_integration_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 연결 서비스 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [새 서비스 연결] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C39.png`)
- [ ] **QA:** 키 원문 재표시 금지·연결 해제 후 기능 차단

### C40 데이터 보존·삭제 요청 · `/app/settings/data` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 2·표시 2개 시각 위계 / 위험 조작 확인 단계: 삭제 요청
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 삭제 범위, 삭제·복구 불가 안내 확인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET/PATCH /v1/me`, `GET/PATCH /v1/orgs/{orgId}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: delete_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `c40_export_format_change`, `c40_export_request_click`, `c40_delete_scope_change`, `c40_submit_delete_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 보유 데이터 구분이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [삭제 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C40.png`)
- [ ] **QA:** 다른 조직 데이터 삭제 금지·법정 보존 차이 설명

### C41 모바일 웹 마이크·QR 페어링 · `/app/mic/:sessionId` · **LATER**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 3·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 3건·대체 문구 3건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: paired_session, mic_permission, transcription
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: QR 인증 상태, 마이크 권한 / axe 위반 0
- [ ] **이벤트:** `c41_push_to_talk_click`, `c41_send_command_click`, `c41_end_pairing_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** QR 인증 상태가 ‘대기’라는 것과 다음 행동 [누르고 말하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C41.png`)
- [ ] **QA:** 만료 QR 재사용 차단·의도하지 않은 배포 없음

### C42 고객용 서비스 상태·작업 제한 · `/app/service-status` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `정적 콘텐츠(CMS revision) 또는 OpenAPI 작성 시 정의` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: work_restrictions
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 전체 서비스 상태, 현재 제한사항 / axe 위반 0
- [ ] **이벤트:** `c42_refresh_status_click`, `c42_support_link_nav` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 서비스 상태가 ‘부분 장애 · 배포 일시 제한’이라는 것과 다음 행동 [상태 새로고침] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C42.png`)
- [ ] **QA:** 배포 중지와 조회 중단을 구분해 안내

### C43 파트너 고객사 관리 · `/app/partner/clients` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `GET /v1/partner/clients`, `GET /v1/partner/commissions` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: client_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 위임 범위 / axe 위반 0
- [ ] **이벤트:** `c43_open_client_click`, `c43_invite_client_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 고객 승인 대기가 ‘4건 · 고객사 3곳’이라는 것과 다음 행동 [고객사 콘솔 열기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C43.png`)
- [ ] **QA:** 위임 범위 밖 사이트 조회·배포 차단, 위임 해지 후 접근 불가, 고객 승인 우회 불가

### C44 파트너 수수료·정산 내역 · `/app/partner/payouts` · **조건부** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1024/768/390 · 테스트 +360/1920 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 정산 기간 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `GET /v1/partner/clients`, `GET /v1/partner/commissions` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(앱 셸) + 라우트 코드 분할 + 서버 상태 캐시(stale-while-revalidate) / 예시값 TBD 해소: tax_invoice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 지급 상태, 세금계산서 상태 / axe 위반 0
- [ ] **이벤트:** `c44_period_change`, `c44_dispute_click` (PII 미포함 검증)
- [ ] **성능:** 라우트 전환 시 100ms 내 스켈레톤, 라우트 JS ≤ 250KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 정산 예정액이 ‘1,284,000원 (VAT 별도)’라는 것과 다음 행동 [정산 문의] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/C44.png`)
- [ ] **QA:** 환불 발생 월 역거래 반영, 중복 정산 0건, 타 파트너 데이터 비노출

## 관리자 콘솔 (47개)

### A01 관리자 로그인 · `/admin/login` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 관리자 이메일, 비밀번호 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `POST /v1/auth/sessions`, `GET /v1/auth/oidc/{provider}/start` / 오류 코드 `AUTH_REQUIRED`, `RATE_LIMITED` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: device_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: admin_email=email, password=new-password / aria-live: 인가된 기기 안내 / axe 위반 0
- [ ] **이벤트:** `a01_login_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 접속이 ‘사내 SSO · MFA 필수’라는 것과 다음 행동 [관리자 로그인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A01.png`)
- [ ] **QA:** 고객 세션으로 관리자 인증 불가·로그인 실패 사유 과노출 없음

### A02 MFA 재인증 · `/admin/mfa` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 3·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 3건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/dashboard` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: challenge_type
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: mfa_code=one-time-code / axe 위반 0
- [ ] **이벤트:** `a02_security_key_click`, `a02_verify_click`, `a02_logout_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 재인증 방식이 ‘TOTP/WebAuthn 정책’이라는 것과 다음 행동 [보안키 인증] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A02.png`)
- [ ] **QA:** 만료 challenge 차단·MFA 없이 고위험 작업 불가

### A03 운영 통합 대시보드 · `/admin` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 0·표시 7개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 관제 기간, 조직 범위 / 실패 문구 0건·대체 문구 7건 검토
- [ ] **DEV:** API `GET /v1/admin/dashboard` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: tenant_scope, quick_links
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a03_time_range_change`, `a03_tenant_scope_change` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** P0/P1이 ‘P1 1건 · 배포 실패 3’이라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/A03.png`)
- [ ] **QA:** P0 우선 표시·계정별 불필요 정보 비노출

### A04 운영 알림·할 일 · `/admin/notifications` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/dashboard` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: severity_filter, assignment_filter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a04_severity_filter_change`, `a04_kind_filter_change`, `a04_assignment_filter_change`, `a04_ack_alert_click`, `a04_open_target_nav` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 알림·할 일이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [수신 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A04.png`)
- [ ] **QA:** 삭제된 대상 링크 접근 차단·중복 경보 구분

### A05 회원 조회 목록 · `/admin/accounts` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/accounts` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: email_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a05_account_status_change`, `a05_joined_range_change`, `a05_open_account_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 회원 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [회원 상세 보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A05.png`)
- [ ] **QA:** 다른 고객 조회 시 업무상 필요 필드만 노출

### A06 회원 상세·계정 조치 · `/admin/accounts/:userId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 6개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 6건 검토
- [ ] **DEV:** API `GET /v1/admin/accounts` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: email_masked, account_state, action_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 계정 상태 / axe 위반 0
- [ ] **이벤트:** `a06_action_type_change`, `a06_confirm_action_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 계정 상태가 ‘이유 표시’라는 것과 다음 행동 [계정 조치 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A06.png`)
- [ ] **QA:** 비권한 조치 차단·계정 조치 전후 감사 증거 확보

### A07 조직 목록 · `/admin/organizations` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/accounts?type=org` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: org_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a07_billing_filter_change`, `a07_org_status_change`, `a07_open_org_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 조직 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [조직 상세] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A07.png`)
- [ ] **QA:** 조직/유저 간 관계 명확, 개인정보 마스킹

### A08 조직 상세 · `/admin/organizations/:orgId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 0·표시 7개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 0건·대체 문구 7건 검토
- [ ] **DEV:** API `GET /v1/admin/accounts?type=org` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: org_name, owner, account_issues
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 정합성 경고 / axe 위반 0
- [ ] **이벤트:** `a08_open_billing_nav` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 연결 사이트가 ‘128건 · 확인 필요 3건’이라는 것을 3초 안에 읽는다(조회 전용 화면). — 비개발자 80% 이상 정답 (목업 `mockups/A08.png`)
- [ ] **QA:** 다른 조직 대상 데이터 쓰기 방지

### A09 사이트·커넥터 목록 · `/admin/sites` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/sites` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: site_search, tenant_filter
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a09_mode_filter_change`, `a09_diagnostic_status_change`, `a09_open_site_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사이트 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [사이트 상세] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A09.png`)
- [ ] **QA:** 지원 등급 최신값 표시·사이트 소유 확인 안 된 조작 방지

### A10 사이트 상세·연결 진단 · `/admin/sites/:siteId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 7개 시각 위계 / 위험 조작 확인 단계: 연결 일시중지
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 7건 검토
- [ ] **DEV:** API `GET /v1/admin/sites` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: domain, verified_owner, connector_type, scope_summary
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 소유권 확인 상태 / axe 위반 0
- [ ] **이벤트:** `a10_disable_connector_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 소유권 확인 상태가 ‘검증방식’이라는 것과 다음 행동 [연결 일시중지] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A10.png`)
- [ ] **QA:** 시크릿 원문 표시 0·권한 있는 진단만 허용

### A11 사이트 진단 이력 상세 · `/admin/sites/:siteId/diagnostics` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 7개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 7건 검토
- [ ] **DEV:** API `GET /v1/sites/{id}/compatibility` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: network_probe, permission_probe, render_probe, deploy_probe, diagnostic_log
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 접속 검사, 권한 검사, 렌더 검사, 배포 검증 / axe 위반 0
- [ ] **이벤트:** `a11_rerun_probe_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 접속 검사가 ‘응답상태’라는 것과 다음 행동 [재진단 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A11.png`)
- [ ] **QA:** 진단 로그에 API 키/세션 비밀 미노출

### A12 패치 작업 목록 · `/admin/jobs` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/jobs/{id}` / 오류 코드 `FORBIDDEN`, `JOB_VALIDATION_FAILED` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: job_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a12_job_status_change`, `a12_source_mode_change`, `a12_period_change`, `a12_inspect_job_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 작업 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [원인 조사] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A12.png`)
- [ ] **QA:** 타 테넌트 상세를 ID로 직접 조회해도 차단

### A13 패치 작업 상세·원인 조사 · `/admin/jobs/:jobId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 8개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 8건 검토
- [ ] **DEV:** API `GET /v1/admin/jobs/{id}` / 오류 코드 `FORBIDDEN`, `JOB_VALIDATION_FAILED` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: tenant_site, instruction_masked, retry_allowed
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 재시도 허용 여부 / axe 위반 0
- [ ] **이벤트:** `a13_credit_transaction_nav`, `a13_open_incident_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 실패 단계가 ‘S3 화면 회귀 · 390px’라는 것과 다음 행동 [사고 접수] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A13.png`)
- [ ] **QA:** 내부 원본·토큰 마스킹, 재현 결과와 고객 안내 일치

### A14 배포 이력 목록 · `/admin/deployments` · **MVP-β**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 1개 시각 위계 / 위험 조작 확인 단계: 배포 상세
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/deployments`, `POST /v1/admin/deployments/hold` / 오류 코드 `DEPLOYMENT_IN_PROGRESS`, `POST_DEPLOY_VERIFY_FAILED`, `ROLLBACK_REQUIRES_REVIEW`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: deploy_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a14_environment_change`, `a14_deploy_status_change`, `a14_period_change`, `a14_open_deploy_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 배포 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [배포 상세] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A14.png`)
- [ ] **QA:** 부분 실패·검증 미완료 표시 정확

### A15 배포 상세·복원 통제 · `/admin/deployments/:deploymentId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 8개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 8건 검토
- [ ] **DEV:** API `GET /v1/admin/deployments`, `POST /v1/admin/deployments/hold` / 오류 코드 `DEPLOYMENT_IN_PROGRESS`, `POST_DEPLOY_VERIFY_FAILED`, `ROLLBACK_REQUIRES_REVIEW`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: environment, target_site, before_after_hash, approver, deploy_status, dependency_notice, rollback_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 배포 상태, 후속 배포 의존 / axe 위반 0
- [ ] **이벤트:** `a15_rollback_request_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사후 검증이 ‘실패 · 롤백 검토 필요’라는 것과 다음 행동 [롤백 심사 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A15.png`)
- [ ] **QA:** 잘못된 배포 대상으로 복원 불가·승인 이력 확인

### A16 배포 일시중지·해제 승인 · `/admin/deployment-controls` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 중지 대상, 조치 사유, 동작 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `POST /v1/admin/deployments/hold` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: reason, incident_id, current_state, second_approver
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 현재 통제 상태 / axe 위반 0
- [ ] **이벤트:** `a16_scope_change`, `a16_requested_action_change`, `a16_second_approver_change`, `a16_submit_request_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 배포 상태가 ‘전체 정상 · 일시중지 없음’이라는 것과 다음 행동 [통제 변경 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A16.png`)
- [ ] **QA:** 고객 범위 밖 중단 없음·재개 사유·승인 기록 누락 없음

### A17 구독 계약 목록 · `/admin/billing/subscriptions` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/billing/*` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: organization_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a17_plan_filter_change`, `a17_status_change`, `a17_open_contract_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 계약 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [계약 상세] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A17.png`)
- [ ] **QA:** 청구 실패와 구독 종료가 별도 상태로 표시

### A18 거래·정산 대사 · `/admin/billing/transactions` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/billing/*` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: transaction_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a18_date_range_change`, `a18_payment_status_change`, `a18_reconciliation_change`, `a18_inspect_discrepancy_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 대사 차이가 ‘−55,000원 · 2건’이라는 것과 다음 행동 [불일치 조사] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A18.png`)
- [ ] **QA:** 웹훅 순서 역전 시에도 거래 상태 일관

### A19 환불 요청·승인 · `/admin/billing/refunds` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 2개 시각 위계 / 위험 조작 확인 단계: 환불 심사
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `POST /v1/admin/billing/refunds/requests`, `POST /v1/admin/billing/refunds/{id}/approve` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: refund_search, refund_reason, refund_approver
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a19_refund_status_change`, `a19_date_range_change`, `a19_open_review_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 심사 대기가 ‘2건 · 환불 가능액 확인’이라는 것과 다음 행동 [환불 심사] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A19.png`)
- [ ] **QA:** 부분 환불·중복 클릭·UNKNOWN 처리 시 과환불 0 목표

### A20 청구서·세금 증빙 조회 · `/admin/billing/invoices` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/billing/*` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: organization
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 발행 상태 / axe 위반 0
- [ ] **이벤트:** `a20_document_type_change`, `a20_date_range_change`, `a20_download_document_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 발행 상태가 ‘발행’이라는 것과 다음 행동 [문서 다운로드] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A20.png`)
- [ ] **QA:** 비권한 PDF 조회 차단·지연 발급 상태 정확

### A21 크레딧 원장 조회 · `/admin/credits` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/credits`, `POST /v1/admin/credits/adjustments` / 오류 코드 `CREDIT_INSUFFICIENT`, `HOLD_EXPIRED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: ledger_search, organization, reconcile_status
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 정합성 검사 / axe 위반 0
- [ ] **이벤트:** `a21_ledger_type_change`, `a21_date_range_change`, `a21_open_adjustment_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 정합성 검사가 ‘실제 검사’라는 것과 다음 행동 [수동 조정 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A21.png`)
- [ ] **QA:** 원장 행 덮어쓰기 불가·합계 추적 가능

### A22 크레딧 수동 조정 승인 · `/admin/credits/adjustments` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 6·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 조정 대상 조직, 조정 종류, 크레딧 수량, 조정 이유 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/credits`, `POST /v1/admin/credits/adjustments` / 오류 코드 `CREDIT_INSUFFICIENT`, `HOLD_EXPIRED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: organization, current_balance, reference_job, adjustment_reason, second_approver
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a22_adjustment_type_change`, `a22_second_approver_change`, `a22_request_adjustment_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 예상 조정 후 잔액이 ‘1,240’이라는 것과 다음 행동 [조정 승인 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A22.png`)
- [ ] **QA:** 중복 조정 불가·승인 없이는 잔액 변동 없음

### A23 고객 문의 큐 · `/admin/tickets` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `PATCH /v1/admin/tickets/{id}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: ticket_search, assignee
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a23_category_change`, `a23_status_change`, `a23_assignee_change`, `a23_urgency_change`, `a23_open_ticket_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** SLA 임박이 ‘3건 · 1시간 이내’라는 것과 다음 행동 [문의 열기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A23.png`)
- [ ] **QA:** 역할별 큐 분리·SLA 지난 건 표시 정상

### A24 문의 상세·답변 작업대 · `/admin/tickets/:ticketId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 3·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 작성 모드 / 실패 문구 3건·대체 문구 3건 검토
- [ ] **DEV:** API `PATCH /v1/admin/tickets/{id}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: customer_identity, reply_text, assignee, priority
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a24_linked_job_nav`, `a24_visibility_mode_change`, `a24_assignee_change`, `a24_priority_change`, `a24_send_reply_click`, `a24_save_internal_click`, `a24_close_ticket_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 고객·조직이 ‘확인’이라는 것과 다음 행동 [고객에게 보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A24.png`)
- [ ] **QA:** 내부 메모 고객 미전달, 답변 중 네트워크 끊김 중복전송 방지

### A25 전문가 작업 큐 · `/admin/expert-tickets` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/expert-tickets`, `GET /v1/admin/expert-capacity` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a25_status_change`, `a25_skill_change`, `a25_deadline_change`, `a25_assign_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 작업 큐가 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [담당자 배정] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A25.png`)
- [ ] **QA:** 월 최대 전문가시간 초과 예약 차단

### A26 전문가 작업 상세·타이머 · `/admin/expert-tickets/:ticketId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 담당 전문가, 배정 작업시간(분) / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `GET /v1/admin/expert-tickets`, `GET /v1/admin/expert-capacity` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: customer_scope, request_details, customer_report
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 작업 타이머 / axe 위반 0
- [ ] **이벤트:** `a26_assignee_change`, `a26_submit_review_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 작업 타이머가 ‘시작’이라는 것과 다음 행동 [검수 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A26.png`)
- [ ] **QA:** 중복 타이머·시간 이중 차감 없음, 고객 승인 확인

### A27 전문가 가용시간·배정 캘린더 · `/admin/expert-capacity` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 기준 주 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `GET /v1/admin/expert-tickets`, `GET /v1/admin/expert-capacity` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: expert_filter, calendar, capacity_warning
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 초과 배정 경고 / axe 위반 0
- [ ] **이벤트:** `a27_week_start_change`, `a27_expert_filter_change`, `a27_skill_filter_change`, `a27_reschedule_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 가용/배정 시간이 ‘1,240’이라는 것과 다음 행동 [배정 변경] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A27.png`)
- [ ] **QA:** 배정 전후 가용 시간 정합·중복 예약 알림

### A28 장애·사고 목록 · `/admin/incidents` · **MVP-β**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `POST /v1/admin/incidents`, `POST /v1/admin/incidents/{id}/actions` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: incident_search, severity, owner
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a28_severity_change`, `a28_status_change`, `a28_owner_change`, `a28_new_incident_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사고 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [사고 등록] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A28.png`)
- [ ] **QA:** 고위험 사고 우선·해결되지 않은 사고가 완료 표시되지 않음

### A29 사고 상세·대응 타임라인 · `/admin/incidents/:incidentId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 6·조작 2·표시 3개 시각 위계 / 위험 조작 확인 단계: 배포 중지 요청
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 등급, 영향 범위, 사고 설명, 책임자 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `POST /v1/admin/incidents`, `POST /v1/admin/incidents/{id}/actions` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: severity, description, incident_owner, mitigation
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 고객 공지 여부 / axe 위반 0
- [ ] **이벤트:** `a29_severity_change`, `a29_affected_scope_change`, `a29_incident_owner_change`, `a29_pause_deploy_click`, `a29_close_incident_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 사고 상태가 ‘P1 진행 중 · 배포 잠금’이라는 것과 다음 행동 [배포 중지 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A29.png`)
- [ ] **QA:** P0 종료 게이트 검증·고객 통지 누락 감지

### A30 감사로그 탐색 · `/admin/audit` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 조회 기간 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/audit`, `POST /v1/admin/audit/exports` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: actor_search, resource_id, event_detail
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a30_time_range_change`, `a30_action_filter_change`, `a30_request_export_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 감사 이벤트가 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [자료 내보내기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A30.png`)
- [ ] **QA:** 권한 없는 감사 로그 열람 불가·행 수정 기능 없음

### A31 감사 증거 내보내기 · `/admin/audit/exports` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 내보내기 자료, 내보낼 기간, 조직·사이트 범위, 이용 목적 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/audit`, `POST /v1/admin/audit/exports` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: scopes, purpose, sensitivity, requested_by, second_approval
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a31_export_type_change`, `a31_date_range_change`, `a31_scopes_change`, `a31_second_approval_change`, `a31_request_export_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 민감도 분류가 ‘개인정보 포함 여부’라는 것과 다음 행동 [추출 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A31.png`)
- [ ] **QA:** 승인 없는 대량 로그 추출 차단·기한 후 링크 폐기

### A32 시스템 상태 관제 · `/admin/system` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 관측 기간 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `GET /v1/admin/system/health`, `POST /v1/admin/system/circuit-breakers` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a32_time_range_change`, `a32_refresh_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 전체 상태가 ‘정상 5 · 저하 1(AI 공급사)’라는 것과 다음 행동 [상태 새로고침] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A32.png`)
- [ ] **QA:** 갱신중단 지표를 정상으로 표시하지 않음

### A33 작업 큐·워커 상태 · `/admin/system/workers` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 3개 시각 위계 / 위험 조작 확인 단계: 큐 일시중지
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 작업 큐 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `GET /v1/admin/system/health`, `POST /v1/admin/system/circuit-breakers` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: queue_name
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a33_queue_name_change`, `a33_worker_status_change`, `a33_pause_queue_click`, `a33_retry_job_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 재시도 횟수가 ‘1,240’이라는 것과 다음 행동 [큐 일시중지] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A33.png`)
- [ ] **QA:** 실행 중 작업 중복 실행 없이 상태 복귀

### A34 AI 모델·서킷브레이커 설정 · `/admin/system/models` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 모델 공급자, 모델 ID, 월 비용 상한 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/system/health`, `POST /v1/admin/system/circuit-breakers` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: model_provider, model_name, current_route, fallback_model, change_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 차단기 상태 / axe 위반 0
- [ ] **이벤트:** `a34_model_provider_change`, `a34_model_name_change`, `a34_fallback_model_change`, `a34_dry_run_click`, `a34_request_change_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 차단기 상태가 ‘OPEN’이라는 것과 다음 행동 [테스트 실행] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A34.png`)
- [ ] **QA:** 정책 변경시 감사·영향 범위 기록·비용 급증 경보

### A35 운영 콘텐츠 목록 · `/admin/content` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 1건 검토
- [ ] **DEV:** API `GET/POST /v1/admin/content-revisions` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: content_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a35_content_type_change`, `a35_publication_status_change`, `a35_new_content_click`, `a35_open_content_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 콘텐츠 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [콘텐츠 작성] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A35.png`)
- [ ] **QA:** 게시 전 콘텐츠 외부 노출 0, 삭제/복원 정책 작동

### A36 콘텐츠 편집·미리보기 · `/admin/content/:contentId` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 7·조작 3·표시 1개 시각 위계 / 위험 조작 확인 단계: 게시 승인
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 콘텐츠 종류, 제목, 본문, 게시 상태 / 실패 문구 3건·대체 문구 1건 검토
- [ ] **DEV:** API `GET/POST /v1/admin/content-revisions` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: title, slug, body, seo_description
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a36_content_type_change`, `a36_publish_at_change`, `a36_status_change`, `a36_preview_click`, `a36_request_review_click`, `a36_publish_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 4개 · 콘텐츠 종류 외’라는 것과 다음 행동 [검토 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A36.png`)
- [ ] **QA:** 공개 화면과 미리보기 일치·승인 없는 게시 차단

### A37 직원 계정 목록 · `/admin/staff` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 1건 검토
- [ ] **DEV:** API `POST /v1/admin/roles/changes` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: staff_search
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a37_role_filter_change`, `a37_status_filter_change`, `a37_invite_staff_click`, `a37_open_staff_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 직원 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [직원 초대] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A37.png`)
- [ ] **QA:** 퇴사자 접근 폐기·관리자 역할 필터 정확

### A38 직원 초대·역할·세션 상세 · `/admin/staff/:staffId` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 5·조작 2·표시 3개 시각 위계 / 위험 조작 확인 단계: 전체 세션 회수
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 직원 이메일, 직원 이름, 역할 목록, 관리 대상 조직·서비스 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `POST /v1/admin/roles/changes` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: staff_name, roles, scope, mfa_status, change_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / autocomplete: staff_email=email / aria-live: MFA 등록 상태 / axe 위반 0
- [ ] **이벤트:** `a38_roles_change`, `a38_scope_change`, `a38_save_staff_click`, `a38_revoke_sessions_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** MFA 등록 상태가 ‘활성화 요구’라는 것과 다음 행동 [변경 승인 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A38.png`)
- [ ] **QA:** 자기승격/최종 Admin 제거 불가, 세션 재평가

### A39 권한 정책·접근 매트릭스 · `/admin/settings/permissions` · **조건부**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 역할 선택 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `POST /v1/admin/roles/changes` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: role, policy_version
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a39_role_change`, `a39_change_request_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 권한 매트릭스가 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [권한 정책 변경 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A39.png`)
- [ ] **QA:** 권한 정책 변경 후 메뉴/API 권한 일치

### A40 내 관리자 프로필·세션 · `/admin/settings/profile` · **MVP-β**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 3·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 관리자 표시명 / 실패 문구 3건·대체 문구 3건 검토
- [ ] **DEV:** API `POST /v1/admin/roles/changes` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: staff_name, admin_email
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a40_signout_other_click`, `a40_password_change_click`, `a40_save_profile_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 인증기 등록 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [비밀번호 변경] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A40.png`)
- [ ] **QA:** 본인 세션 종료 후 재로그인 필요·MFA 유지

### A41 관리자 접근 거절(403) · `/admin/forbidden` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/dashboard` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: requested_resource, required_role
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a41_back_dashboard_click`, `a41_request_access_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 접근 요청 메뉴가 ‘민감 경로 제거’라는 것과 다음 행동 [대시보드] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A41.png`)
- [ ] **QA:** 403 요청에서 기밀 데이터 렌더링 0

### A42 운영 관제 점검·오류 · `/admin/error` · **MVP-α**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/dashboard` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: service_status
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 관제 상태 / axe 위반 0
- [ ] **이벤트:** `a42_retry_click`, `a42_logout_click`, `a42_incident_link_nav` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 관제 상태가 ‘가능한 정보’라는 것과 다음 행동 [다시 조회] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A42.png`)
- [ ] **QA:** 관리자만 보는 로그가 고객에게 공유되지 않음

### A43 파트너·에이전시 관리 · `/admin/partners` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 1개 시각 위계 / 위험 조작 확인 단계: 신청 반려
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 1건 검토
- [ ] **DEV:** API `GET /v1/admin/partners`, `PATCH /v1/admin/partners/{id}` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: commission_rate, decision_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a43_status_filter_change`, `a43_approve_partner_click`, `a43_reject_partner_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 파트너 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [파트너 승인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A43.png`)
- [ ] **QA:** 수수료율 변경 이력 보존, 반려 메일 내부 메모 미노출, 권한 없는 직원 변경 차단

### A44 파트너 수수료 정산 · `/admin/partners/payouts` · **조건부** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 2개 시각 위계 / 위험 조작 확인 단계: 정산 확정
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 정산 월 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `GET /v1/admin/partner-payouts`, `POST /v1/admin/partner-payouts/{id}/confirm` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: hold_reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a44_payout_period_change`, `a44_confirm_payout_click`, `a44_export_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 원장 대사 차이가 ‘1,240’이라는 것과 다음 행동 [정산 확정] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A44.png`)
- [ ] **QA:** 환불 역거래 반영, 이중 확정 차단, 대사 차이 0 확인 후 확정

### A45 요금제·가격 버전·쿠폰 · `/admin/billing/plans` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 2개 시각 위계 / 위험 조작 확인 단계: 가격 버전 게시 예약
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET/POST /v1/admin/price-versions`, `GET/POST /v1/admin/coupons` / 오류 코드 `PAYMENT_PENDING`, `PAYMENT_ALREADY_PROCESSED`, `FORBIDDEN` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a45_effective_at_change`, `a45_apply_existing_change`, `a45_publish_version_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 가격 버전이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [가격 버전 게시 예약] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A45.png`)
- [ ] **QA:** 게시 전 가격 비노출, 결제 중 버전 변경 시 intent 기준 금액 유지, 쿠폰 중복 사용 차단

### A46 단위경제·제품 KPI · `/admin/analytics` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 기간 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `GET /v1/admin/analytics/unit-economics` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a46_period_change`, `a46_export_csv_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 첫 운영 반영 도달률이 ‘38% · 목표 50%’라는 것과 다음 행동 [집계 내려받기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A46.png`)
- [ ] **QA:** 원장 합계와 대시보드 합계 일치, 기간 필터 정확, 권한 없는 직원 접근 차단

### A47 호환성 매트릭스·어댑터 버전 · `/admin/compatibility` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 디자인 1440/1280/1024 · 모바일 390은 조회·긴급 확인 한정 / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `GET/PATCH /v1/admin/compatibility-profiles` / 오류 코드 `AUTH_REQUIRED`, `FORBIDDEN`, `RATE_LIMITED`, `INTERNAL_RETRYABLE` / 렌더링 CSR(관리자 앱 셸) + 서버 페이지네이션/필터 URL 동기화 / 예시값 TBD 해소: evidence_url
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `a47_adapter_filter_change`, `a47_grade_change`, `a47_save_grade_click` (PII 미포함 검증)
- [ ] **성능:** 테이블 첫 페이지 표시 ≤ 1.5s(p75), 라우트 JS ≤ 300KB(gzip), INP ≤ 200ms
- [ ] **3초 테스트:** 강등 예정이 ‘SFTP·PHP 이미지 → LIMITED’라는 것과 다음 행동 [등급 변경 저장] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/A47.png`)
- [ ] **QA:** 강등 후 해당 환경 자동 배포 차단, 공개 페이지 동기화, 근거 없는 승격 차단

## 모달·Drawer·Studio 오버레이 (45개)

### O01 전 플랫폼 알림·토스트·상태 경고 · `공통` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: message
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 메시지 수준 / axe 위반 0
- [ ] **이벤트:** `o01_retry_click`, `o01_dismiss_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 메시지 수준이 ‘정보’라는 것과 다음 행동 [다시 시도] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O01.png`)
- [ ] **QA:** 스크린리더 읽기·중요 알림 소실 없음

### O02 모바일 내비게이션 Drawer · `공식/고객/관리자` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: active_menu, menu_items
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o02_close_click`, `o02_logout_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 0개’라는 것과 다음 행동 [닫기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O02.png`)
- [ ] **QA:** Escape·터치·키보드 통과

### O03 쿠키/개인정보 동의 패널 · `공식` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: necessary
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o03_analytics_change`, `o03_marketing_change`, `o03_reject_click`, `o03_save_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 필수 쿠키가 ‘개인정보방침 링크’라는 것과 다음 행동 [선택 쿠키 거부] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O03.png`)
- [ ] **QA:** 거절해도 데이터 분석 SDK 불활성

### O04 데모 온보딩 코치마크 · `공식 데모` · **MVP-β**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: step, coach_text
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o04_next_click`, `o04_skip_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 현재 단계 안내가 ‘실제 조작 위치’라는 것과 다음 행동 [다음] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O04.png`)
- [ ] **QA:** 모바일 작은 화면/스크린리더 사용 가능

### O05 요금제 비교 팝오버 · `공식/고객` · **MVP-β**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 비교 플랜 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: current_plan, proposed_plan
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o05_proposed_plan_change`, `o05_close_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 예상 청구 금액이 ‘서버 견적값 또는 입력 금액’이라는 것과 다음 행동 [돌아가기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O05.png`)
- [ ] **QA:** 서버 최종청구액과 표시 일치

### O06 결제 처리 대기/오류 Dialog · `공식/고객` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: processing_status
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 결제 확인 중 / axe 위반 0
- [ ] **이벤트:** `o06_check_again_click`, `o06_support_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 결제 확인 중이 ‘PG 확정 전 미완료’라는 것과 다음 행동 [다시 확인] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O06.png`)
- [ ] **QA:** 미확정 PG 주문을 성공으로 표시하지 않음

### O07 조직·사이트 전환기 · `고객/관리자` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 조직 선택, 사이트 선택 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: organization, site, role, unsaved_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 저장되지 않은 변경 / axe 위반 0
- [ ] **이벤트:** `o07_organization_change`, `o07_site_change`, `o07_switch_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 현재 역할이 ‘권한’이라는 것과 다음 행동 [전환하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O07.png`)
- [ ] **QA:** 조직 전환 뒤 이전 고객 데이터 잔상 없음

### O08 접근 제한·권한 안내 · `고객/관리자` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: required_action
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 제한 사유, 해결 방법 / axe 위반 0
- [ ] **이벤트:** `o08_request_access_click`, `o08_close_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 제한 사유가 ‘권한 부족’이라는 것과 다음 행동 [권한 요청하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O08.png`)
- [ ] **QA:** 버튼 숨김만으로 권한 검사 대체하지 않음

### O09 Studio 상단 글로벌 바 ST-01 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 편집 환경, 페이지 경로, PC·태블릿·모바일, 원본/변경안 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: studio_site, page_selector, source_preview, connection_indicator
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 연결 상태 / axe 위반 0
- [ ] **이벤트:** `o09_target_environment_change`, `o09_page_selector_change`, `o09_viewport_switch_change`, `o09_source_preview_change`, `o09_exit_studio_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 연결 상태가 ‘끊김 시 편집 정지’라는 것과 다음 행동 [Studio 나가기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O09.png`)
- [ ] **QA:** 프로덕션/스테이징 잘못 선택 불가

### O10 Studio 요소 선택 경계 ST-02 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 4개 시각 위계 / 위험 조작 확인 단계: 선택 해제
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: hovered_node
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 선택 가능 여부 / axe 위반 0
- [ ] **이벤트:** `o10_select_parent_click`, `o10_clear_selection_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 요소 종류가 ‘텍스트’라는 것과 다음 행동 [상위 요소로 이동] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O10.png`)
- [ ] **QA:** sticky/transform/iframe 스크롤 선택 검증

### O11 Ghost Mini Dock ST-03 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 3·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 명령 입력 / 실패 문구 3건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: dock_location, target_pill, command_draft
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 진행 중 작업 / axe 위반 0
- [ ] **이벤트:** `o11_voice_button_click`, `o11_send_instruction_click`, `o11_collapse_change`, `o11_open_history_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 진행 중 작업이 ‘단계’라는 것과 다음 행동 [음성으로 입력] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O11.png`)
- [ ] **QA:** 390px에서 주요 CTA 가림 없음

### O12 명령 입력/의도 확인 ST-04 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 7·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 수정 요청, 수정 유형, 적용 범위 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: selected_target, source_text, instruction, new_text, style_value, impact_summary
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o12_instruction_mode_change`, `o12_apply_scope_change`, `o12_style_property_change`, `o12_preview_request_click`, `o12_reset_draft_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 적용 대상이 ‘없으면 생성 차단’이라는 것과 다음 행동 [변경안 생성] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O12.png`)
- [ ] **QA:** 대상 누락 명령 실행 금지·차감 전 확인

### O13 요소 계층 Breadcrumb ST-05 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: hierarchy_path, current_element
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o13_parent_select_click`, `o13_child_select_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 동일 패턴 요소 수가 ‘1,240’이라는 것과 다음 행동 [상위 요소 선택] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O13.png`)
- [ ] **QA:** 중첩된 동일 문구 복수 대상 구분

### O14 원본 매핑 근거/모호성 ST-06 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 3·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 3건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: selected_candidate
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o14_selected_candidate_change`, `o14_rerun_mapping_click`, `o14_expert_escalation_click`, `o14_proceed_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 소스 매핑 수준이 ‘HIGH’라는 것과 다음 행동 [전문가 도움 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O14.png`)
- [ ] **QA:** 출처 불확실한 상태에서 쓰기 명령 비활성

### O15 전후 비교 패널 ST-07 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 1·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 보기 방식, 화면 크기 / 실패 문구 1건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 캡처 상태 / axe 위반 0
- [ ] **이벤트:** `o15_comparison_mode_change`, `o15_viewport_change`, `o15_sync_scroll_change`, `o15_back_to_edit_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 캡처 상태가 ‘오류’라는 것과 다음 행동 [명령 수정] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O15.png`)
- [ ] **QA:** 스크린샷 누락 시 HTML 변경 요약 대체 제공

### O16 검증 결과 Drawer ST-08 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 7개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 7건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: postcheck_state
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 정적 검사, 빌드·타입 검사, 반응형 화면 검사, 기능 동작 검사, 승인 상태, 배포 후 점검 / axe 위반 0
- [ ] **이벤트:** `o16_rerun_validation_click`, `o16_request_approval_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 정적 검사가 ‘PASS’라는 것과 다음 행동 [승인 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O16.png`)
- [ ] **QA:** 부분검증 성공을 전체검증 성공으로 표시하지 않음

### O17 실제 운영 배포 승인 Dialog ST-09 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 8개 시각 위계 / 위험 조작 확인 단계: 운영 사이트에 반영
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 검증 결과, 도메인·운영환경 확인, 변경 내용 검토 완료 / 실패 문구 2건·대체 문구 8건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: target_domain, target_environment, original_hash, approval_by, self_approval_notice, validation_passed, rollback_possible
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 본인 승인 안내, 되돌리기 가능 여부 / axe 위반 0
- [ ] **이벤트:** `o17_validation_passed_change`, `o17_final_deploy_click`, `o17_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 운영 반영 대상이 ‘bluedental.co.kr · 운영’이라는 것과 다음 행동 [운영 사이트에 반영] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O17.png`)
- [ ] **QA:** 권한/원본 해시 다른 상태 운영 배포 불가

### O18 복원·롤백 패널 ST-10 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 4개 시각 위계 / 위험 조작 확인 단계: 되돌리기 실행
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 복구할 버전, 복원 사유 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: rollback_version, reason, rollback_ready
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 복구 가능 상태 / axe 위반 0
- [ ] **이벤트:** `o18_rollback_version_change`, `o18_confirm_rollback_click`, `o18_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 복구 가능 상태가 ‘검증 완료 전 차단’이라는 것과 다음 행동 [되돌리기 실행] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O18.png`)
- [ ] **QA:** 후속 패치 충돌시 자동 완료 표시 금지

### O19 이미지 교체/대체텍스트 ST-11 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 4·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 교체할 이미지 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: dimensions, alt_text, metadata_notice
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 위치정보 제거 안내 / axe 위반 0
- [ ] **이벤트:** `o19_crop_mode_change`, `o19_preview_asset_click`, `o19_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 새 이미지 크기가 ‘픽셀/비율’이라는 것과 다음 행동 [이미지 교체 미리보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O19.png`)
- [ ] **QA:** 업로드 실패 시 기존 이미지 유지·alt 입력 검증

### O20 작업 진행 타임라인 ST-12 · `고객 Studio` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 3·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 3건·대체 문구 5건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: stepper, progress_status, message
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 현재 상태 / axe 위반 0
- [ ] **이벤트:** `o20_retry_if_safe_click`, `o20_cancel_if_safe_click`, `o20_go_job_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 현재 상태가 ‘서버 이벤트’라는 것과 다음 행동 [안전한 재시도] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O20.png`)
- [ ] **QA:** 리프레시 후 동일 Job 진행 상황 복구

### O21 사이트 연결 에러·재진단 모달 · `고객 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: error_code, error_reason, repair_steps
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o21_retry_click`, `o21_change_mode_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 연결 실패 코드가 ‘민감정보 제외’라는 것과 다음 행동 [연결 방식 변경] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O21.png`)
- [ ] **QA:** 토큰 만료/권한 부족/네트워크 실패 서로 다른 설명

### O22 크레딧 HOLD·환급 확인 · `고객 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 5개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 5건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: charge_policy
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 거래 상태, 차감 확정 조건 / axe 위반 0
- [ ] **이벤트:** `o22_open_history_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 사용 가능 크레딧이 ‘120 크레딧’이라는 것과 다음 행동 [원장 보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O22.png`)
- [ ] **QA:** 실패 작업의 HOLD 상태를 사용으로 표시하지 않음

### O23 지원요청 Trace·화면 첨부 확인 · `고객 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 전송 데이터 목록, 첨부내용 확인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: included_data
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o23_redaction_click`, `o23_included_data_change`, `o23_attach_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 2개 · 전송 데이터 목록 외’라는 것과 다음 행동 [민감부분 가리기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O23.png`)
- [ ] **QA:** 사용자 확인 전 이미지가 운영 CS로 전송되지 않음

### O24 관리자 전역 통합 검색 · `관리자 콘솔` · **MVP-β**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 전체 검색어 / 실패 문구 2건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: query
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o24_type_filter_change`, `o24_open_result_click`, `o24_close_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 입력할 항목이 ‘필수 1개 · 전체 검색어 외’라는 것과 다음 행동 [상세 이동] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O24.png`)
- [ ] **QA:** 미권한 검색 결과 제목/미리보기 비노출

### O25 고위험 조작 재확인 Dialog · `관리자 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 업무 사유, 확인 문구 입력 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: target, action, impact, reason, verification_phrase, reauth
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 영향 범위, 재인증 상태 / axe 위반 0
- [ ] **이벤트:** `o25_approve_click`, `o25_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 조작이 ‘배포 일시중지 · 전 사이트’라는 것과 다음 행동 [고위험 조치 실행] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O25.png`)
- [ ] **QA:** 위험 동작 1회 실행·취소시 변경 없음

### O26 환불 심사·승인 Sheet · `관리자 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 4개 시각 위계 / 위험 조작 확인 단계: 환불 승인 요청
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 이번 환불액, 환불 심사 사유 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: original_payment, reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 승인 상태 / axe 위반 0
- [ ] **이벤트:** `o26_submit_refund_click`, `o26_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 환불 가능액이 ‘55,000원 중 55,000원’이라는 것과 다음 행동 [환불 승인 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O26.png`)
- [ ] **QA:** PG UNKNOWN 재제출로 이중 환불 없음

### O27 권한 승격·세션회수 Dialog · `관리자 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 변경 역할, 변경 사유 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: staff, role_before, role_after, reason
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o27_role_after_change`, `o27_confirm_click`, `o27_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 달라지는 권한이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [변경 승인 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O27.png`)
- [ ] **QA:** 현재 세션 역할이 변경 즉시 재평가됨

### O28 P0 사고 배너·긴급 동작 · `관리자 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: incident_id, affected_scope, deploy_lock
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 배포 중지 상태 / axe 위반 0
- [ ] **이벤트:** `o28_ack_click`, `o28_open_incident_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** P1 사고가 ‘영향 사이트 12 · 배포 잠금’이라는 것과 다음 행동 [사고 상세 보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O28.png`)
- [ ] **QA:** P0 중 배포 재개 위험 CTA 제한

### O29 고객 발송 vs 내부 메모 편집기 · `관리자 콘솔` · **MVP-α**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 3·조작 3·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 작성 구분, 본문 / 실패 문구 3건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: recipient, message
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o29_visibility_change`, `o29_preview_click`, `o29_send_customer_click`, `o29_save_internal_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 실제 발송 대상이 ‘고객 응답 시만’이라는 것과 다음 행동 [고객에게 답변 전송] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O29.png`)
- [ ] **QA:** 내부 메모가 어떤 고객 응답 API에도 포함되지 않음

### O30 감사자료 추출·다운로드 승인 · `관리자 콘솔` · **MVP-β**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 2·조작 2·표시 4개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 내보내기 목적, 제한적 이용 확인 / 실패 문구 2건·대체 문구 4건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: export_scope, purpose, sensitive_data, approver
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 민감정보 포함 여부 / axe 위반 0
- [ ] **이벤트:** `o30_export_click`, `o30_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 민감정보 포함 여부가 ‘자동 표시’라는 것과 다음 행동 [승인 후 다운로드] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O30.png`)
- [ ] **QA:** 다운로드 URL 만료·승인자 외 접근 금지

### O31 동시 편집 Presence·잠금 안내 · `고객 Studio` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 요소 잠금 상태 / axe 위반 0
- [ ] **이벤트:** `o31_request_handover_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 요소 잠금 상태가 ‘잠금자’라는 것과 다음 행동 [편집 넘겨받기 요청] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O31.png`)
- [ ] **QA:** 2개 브라우저 동시 편집 시 경고 표시, lock TTL 만료 해제, 배포 직전 해시 충돌 차단

### O32 운영 반영 직후 결과 확인·복원 요청 토스트 · `고객 Studio·콘솔` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 2개 시각 위계 / 위험 조작 확인 단계: 복원 요청
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 반영 결과, 사후 점검 / axe 위반 0
- [ ] **이벤트:** `o32_open_live_nav`, `o32_request_rollback_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 반영 결과가 ‘확인됨 · 사후 점검 중’이라는 것과 다음 행동 [운영 페이지 열기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O32.png`)
- [ ] **QA:** 사후검증 미완료 시 '완료' 미표시, 후속 배포 존재 시 원클릭 복원 비활성, 중복 복원 요청 1건만 생성

### O33 Studio 키보드 단축키·접근성 도움말 · `고객 Studio` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: disable_shortcuts
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o33_disable_shortcuts_change`, `o33_remap_click` (PII 미포함 검증)
- [ ] **성능:** 셸 초기 JS ≤ 250KB(gzip), 고객 페이지 주입 런타임 ≤ 50KB(gzip), hover 하이라이트 1프레임 내(16ms 예산), INP ≤ 200ms — 내부 예산이며 고객 SLA 아님
- [ ] **3초 테스트:** 단축키 목록이 ‘128건 · 확인 필요 3건’이라는 것과 다음 행동 [단축키 바꾸기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O33.png`)
- [ ] **QA:** IME 조합 중 단축키 미발동, 입력창 포커스 중 미발동, 스크린리더로 표 읽기

### O34 K1 레이어 진입 · 번호로 고르기 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: tap_hint
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 바꿀 곳을 누르세요 / axe 위반 0
- [ ] **이벤트:** `o34_mic_main_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 바꿀 수 있는 곳이 ‘번호 1~12’라는 것과 다음 행동 [말로 바꾸기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O34.png`)
- [ ] **QA:** 번호 30개 이하 표시, 스크롤 후 번호 갱신, “8번” 발화 시 정확한 요소 선택

### O35 K2 요소 선택 · 맞춤 제안 칩 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 1·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 필수 입력: 추천 작업 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: selected_element
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o35_suggestion_chips_change`, `o35_speak_click`, `o35_type_fallback_nav` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 선택한 곳이 ‘8번 · 스케일링 가격 30,000원’이라는 것과 다음 행동 [말로 말하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O35.png`)
- [ ] **QA:** 가격 요소 선택 시 “가격 수정” 칩이 첫 번째, 칩 탭만으로 다음 단계 진입

### O36 K3 듣는 중 · 실시간 자막 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 2개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: live_caption
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 음성 입력 상태 / axe 위반 0
- [ ] **이벤트:** `o36_stop_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 들린 말이 ‘“8번 가격을 3만 5천 원으로”’라는 것과 다음 행동 [그만 듣기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O36.png`)
- [ ] **QA:** 숫자 발화 정규화 정확, 2초 침묵 자동 종료, 권한 거부 시 텍스트 대안

### O37 K4 확인 카드 · 예/다시 말하기 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: before_value, after_value
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o37_confirm_yes_click`, `o37_retry_voice_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 바꿀 내용이 ‘30,000원 → 35,000원’이라는 것과 다음 행동 [예, 미리보기 만들기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O37.png`)
- [ ] **QA:** 확인 없이 생성 금지, 단어 탭 교체 동작, 비용 표시와 실제 차감 상한 일치

### O38 K5 미리보기 · 사이트 위에서 바로 확인 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 3·표시 2개 시각 위계 / 위험 조작 확인 단계: 반영하기, 되돌리기
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 3건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 자동 검사 / axe 위반 0
- [ ] **이벤트:** `o38_publish_click`, `o38_toggle_before_click`, `o38_discard_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 미리보기가 ‘변경 1개 · 자동 검사 통과’라는 것과 다음 행동 [반영하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O38.png`)
- [ ] **QA:** 변경 요소만 강조, 모바일 전환 시 같은 요소 유지, 검증 실패 시 반영하기 비활성

### O39 K6 원탭 반영 · 길게 눌러 확인 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 2개 시각 위계 / 위험 조작 확인 단계: 길게 눌러 반영
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: target_site
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o39_hold_publish_click`, `o39_cancel_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 반영 대상이 ‘bluedental.co.kr · 운영’이라는 것과 다음 행동 [길게 눌러 반영] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O39.png`)
- [ ] **QA:** 짧은 탭으로 반영 불가, 패스키 실패 시 반영 중단, 해시 불일치 시 차단

### O40 K7 반영 완료 · 말로 되돌리기 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 1개 시각 위계 / 위험 조작 확인 단계: 되돌리기
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 반영 상태 / axe 위반 0
- [ ] **이벤트:** `o40_view_site_nav`, `o40_undo_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 반영 상태가 ‘반영 완료 · 방금’이라는 것과 다음 행동 [사이트 보기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O40.png`)
- [ ] **QA:** 사후 점검 전 완료 미표시, 되돌리기 1회만 생성

### O41 K8 이미지 교체 · 휴대폰으로 찍어서 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: alt_suggestion
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o41_qr_upload_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 새 사진 받는 방법이 ‘휴대폰으로 찍기 · QR 5분 유효’라는 것과 다음 행동 [휴대폰으로 찍기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O41.png`)
- [ ] **QA:** QR 만료·재발급, 비율 자동 맞춤, alt 제안 확정 동작

### O42 K9 변경 묶음 · 한 번에 반영 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 2개 시각 위계 / 위험 조작 확인 단계: 모두 반영
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 2건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o42_publish_all_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 모아 둔 변경이 ‘4개 · 최대 6크레딧’이라는 것과 다음 행동 [모두 반영] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O42.png`)
- [ ] **QA:** 묶음 내 1개 실패 시 나머지 반영 여부 선택, 합계 크레딧 일치

### O43 K10 AI가 먼저 제안 · 지난 정보 정리 · `고객 Studio · 키보드리스` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 2·표시 1개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 1건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import)
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o43_accept_click`, `o43_later_click`, `o43_mute_nav` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** AI 제안이 ‘지난 이벤트 배너 1개’라는 것과 다음 행동 [예, 정리하기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O43.png`)
- [ ] **QA:** 오탐 시 “다시 보지 않기”, 제안은 하루 최대 3개, 수락 시 K4 확인 카드로 연결

### O44 K11 자동 처리 불가 · 전문가에게 맡기기 · `고객 Studio · 키보드리스` · **MVP-α** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 0·조작 1·표시 3개 시각 위계
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 1건·대체 문구 3건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: fail_reason, credit_refund
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / aria-live: 크레딧 반환 / axe 위반 0
- [ ] **이벤트:** `o44_order_expert_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 전문가 견적이 ‘33,000원 · 내일 18시 완료’라는 것과 다음 행동 [전문가에게 맡기기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O44.png`)
- [ ] **QA:** 실패 시 크레딧 반환 확인, 견적 금액=결제 금액, 맥락 자동 첨부

### O45 K12 모바일 레이어 · 휴대폰에서 바로 · `고객 Studio · 키보드리스` · **MVP-β** · **v5.6 신규**
- [ ] **UI:** 프레임 부모 화면 기준 + 390 하단 Sheet / 상태 6종(기본·로딩·빈·오류·권한 없음·오프라인) / 입력 1·조작 2·표시 0개 시각 위계 / 위험 조작 확인 단계: 길게 눌러 반영
- [ ] **UX:** 문구 확정 — 안내·상시안내·빈 상태·성공 + 로딩·오류·권한 없음·오프라인 / 실패 문구 2건·대체 문구 0건 검토
- [ ] **DEV:** API `부모 화면 API 사용` / 오류 코드 `INTERNAL_RETRYABLE` / 렌더링 부모 화면 내 지연 로드 컴포넌트(lazy import) / 예시값 TBD 해소: m_numbers
- [ ] **A11y:** 키보드 순서·포커스 표시·대상 크기 24px+ / axe 위반 0
- [ ] **이벤트:** `o45_m_mic_click`, `o45_m_numbers_change`, `o45_m_publish_click` (PII 미포함 검증)
- [ ] **성능:** 열기 ≤ 100ms(지연 로드 시 프리페치), 포커스 이동 즉시
- [ ] **3초 테스트:** 선택한 곳이 ‘8번 · 스케일링 가격’이라는 것과 다음 행동 [말로 바꾸기] 버튼을 3초 안에 찾는다. — 비개발자 80% 이상 정답 (목업 `mockups/O45.png`)
- [ ] **QA:** 390px에서 버튼 가림 없음, 한 손 조작 완료, 음성 권한 거부 대안
