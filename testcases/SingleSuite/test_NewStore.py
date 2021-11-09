from httprunner import HttpRunner, RunRequest, Step, Config

class SmokeNewStore(HttpRunner):
    config = (
        Config("店铺域名")
        .verify(False)
        .base_url("https://apitest.fandow.com")
    )
    teststeps = [
        Step(
            RunRequest("新增店铺")
            .post("/test/oms/basic/shop")
            .with_headers(**{
                "accept": "application/json, text/plain, */*",
                "authorization": "$Associate_Token"
            })
            .with_json({
                "accountName": "$accountName",
                "accountNumber": "$accountNumber",
                "appKey": "$appKey",
                "appSecret": "$appSecret",
                "channel": "$channel",
                "description": "$description",
                "master": "$master",
                "phone": "$phone",
                "platform": "$platform",
                "sendExpired": "$sendExpired",
                "shopName": "$shopName",
                "warehouse": "$warehouse",
                "warehouseAddress": "$warehouseAddress",
                "warehouseId": "$warehouseId"    #注意这个id
            })
            .validate().assert_equal("body.msg", "OK!")
            .assert_equal("body.message", "OK!")
        )
    ]