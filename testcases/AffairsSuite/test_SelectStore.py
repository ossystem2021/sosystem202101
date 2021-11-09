from httprunner import HttpRunner, RunRequest, Step, Config
import pytest
from httprunner import Parameters
class TestSmokeSelectStore(HttpRunner):
    @pytest.mark.parametrize(
        "param", Parameters({
            "usr-pwd": "${P(.csv)}"
        })
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("查询店铺")
        .verify(False)
        .base_url("${ENV(host)}")     #引用env文件，全局常量
    )
    teststeps = [
        Step(
            RunRequest("正常登录")
                .post("/test/oms/auth")
                .with_headers(**{
                "accept": "application/json, text/plain, */*"
            })
                .with_json({
                "username": "$usr",
                "password": "$pwd"
            })
                .extract().with_jmespath("body.data.accessToken", "Associate_Token")    #抛出token
                .validate().assert_equal("status_code", 200)
                .assert_equal("body.message","OK!")
                .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("查询店铺")
            .get("/test/oms/basic/shop?pageSize=20&totalCount=39&pageIndex=1&shopName="+
                 ""+
                 "&master="+"}"+
                 "&channel="+"")
            .with_headers(**{
                "accept": "application/json, text/plain, */*",
                "authorization": "$Associate_Token"
            })
            .validate().assert_equal("status_code",200)

        )
    ]

if __name__ == "__main__":
    pytest.main()
