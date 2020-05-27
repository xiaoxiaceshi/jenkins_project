import pytest

class TestLogin:
    @pytest.fixture(params=[1,2,3])
    def before(self,request):   #普通函数
        return request.param
    @pytest.mark.parametrize("name",[4,5])
    def test_a(self,before,name):
        print(before)
        print(name)
    def test_b(self):
        print("b")