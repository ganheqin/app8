import allure
import pytest


class Test_01:
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_001(self):
        print("hello world")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("a", [1, 2, 3])
    @allure.step(title="测试步骤001")
    def test_al(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤001")
    def test_al(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="测试步骤001")
    def test_a2(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("a", [1, 2, 3])
    @allure.step(title="测试步骤001")
    def test_a3(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @pytest.mark.parametrize("a", [1, 2, 3])
    @allure.step(title="测试步骤001")
    def test_a4(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @pytest.mark.parametrize("a", [1, 2, 3])
    @allure.step(title="测试步骤001")
    def test_a5(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("a", [1, 2, 3])
    @allure.step(title="测试步骤001")
    def test_a6(self, a):
        allure.attach("登录名为:","用户名为111")
        allure.attach("登录密码为:","密码为123")
        assert False