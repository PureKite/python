# 패키지란? 모듈 여러 개 모아놓은 것(라이브러리)
# 패키지 예시
# game/
#     __init__.py  => 설정 파일
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py

# 패키지 가져왔을 때
# import game.sound.echo
# game.sound.echo.echo_test()
# from game.sound import echo
# from game.sound.echo import echo_test()
# from game.sound.echo import echo_test() as e
# from game.sound import * (* == 모두 => __init__ 에 all로 설정)
# ..sound.echo => .. 이전 폴더