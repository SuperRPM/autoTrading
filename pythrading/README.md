pythrading/
├── internal/
│   ├── gui/              # GUI 관련 코드
│   │   ├── __init__.py
│   │   ├── qt.py
│   │   └── widgets/     # 커스텀 위젯들
│   │
│   ├── scraper/         # 웹 스크래핑 관련 코드
│   │   ├── __init__.py
│   │   ├── upbit.py     # 업비트 스크래핍
│   │   ├── binance.py   # 바이낸스 스크래핑
│   │   └── common.py    # 공통 스크래핑 유틸리티
│   │
│   ├── models/          # 데이터 모델
│   │   ├── __init__.py
│   │   ├── ticker.py    # 시세 데이터 모델
│   │   └── trade.py     # 거래 데이터 모델
│   │
│   └── database/        # 데이터 저장소
│       ├── __init__.py
│       └── repository.py # 데이터 저장/조회 로직
│
├── config/              # 설정 파일들
│   ├── __init__.py
│   └── settings.py      # 환경 설정
│
└── utils/              # 유틸리티 함수들
    ├── __init__.py
    ├── logger.py      # 로깅
    └── formatter.py   # 데이터 포맷팅