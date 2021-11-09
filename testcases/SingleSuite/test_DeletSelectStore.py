from httprunner import HttpRunner, RunRequest, Step, Config

class SmokeDeleteSelectStore(HttpRunner):
    config = (
        Config("店铺域名")
            .verify(False)
            .base_url("https://apitest.fandow.com")
    )
    teststeps = [
        Step(
            RunRequest("查询店铺")
                .get("/test/oms/basic/shop?pageSize=20&totalCount=39&pageIndex=1&shopName="+
                     "${urlcode($shopName)}"+
                     "&master="+"${urlcode($accountName)}"+
                     "&channel="+"${urlcode($channel)}")
                .with_headers(**{
                "accept": "application/json, text/plain, */*",
                "authorization": "$Associate_Token"
            })
             .validate().assert_not_equal("body.data.list[0].id", "$Associate_StoreId")
        )
    ]