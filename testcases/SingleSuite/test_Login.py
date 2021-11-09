from httprunner import HttpRunner,RunRequest,Step,Config

class SmokeLogin(HttpRunner):
    config = (
        Config("登录")
            .verify(False)
            .base_url("https://apitest.fandow.com")
    )
    teststeps = [
        Step(
            RunRequest("正常登录")
                .post("/test/oms/auth")
                .with_headers(**{
                "accept": "application/json, text/plain, */*"
            })
                .with_json({
                "username": "fd-0001",
                "password": "123456"
            })
                .extract().with_jmespath("body.data.accessToken", "Associate_Token")    #抛出token
                .validate().assert_equal("status_code", 200)
        )
    ]

if __name__ == "__main__":
    SmokeLogin().test_start()