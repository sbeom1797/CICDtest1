from app import greet


def test_greet():
    assert greet("승범") == "안녕하세요, 승범님! CI/CD 배포 성공입니다."