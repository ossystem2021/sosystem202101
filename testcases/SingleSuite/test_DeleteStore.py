from httprunner import HttpRunner, RunRequest, Step, Config

class SmokeDeleteStore(HttpRunner):
    config = (
        Config("店铺域名")
            .verify(False)
            .base_url("https://apitest.fandow.com")
    )
    teststeps = [
        Step(
            RunRequest("删除店铺")
            .delete("/test/oms/basic/shop?idList="+"$Associate_StoreId")
            .with_headers(**{
                "accept": "application/json, text/plain, */*",
                "authorization": "$Associate_Token"
            })
        )
    ]
