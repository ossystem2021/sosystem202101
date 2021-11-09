from httprunner import HttpRunner, RunTestCase, Step, Config
from testcases.SingleSuite.test_Login import SmokeLogin
from testcases.SingleSuite.test_NewStore import SmokeNewStore
from testcases.SingleSuite.test_SelectStore import SmokeSelectStore
from testcases.SingleSuite.test_DeleteStore import SmokeDeleteStore
from testcases.SingleSuite.test_DeletSelectStore import SmokeDeleteSelectStore
class TestStoreMangement(HttpRunner):
    config = (
        Config("店铺管理")
        .variables(**{
            "accountName": "1",
            "accountNumber": "1",
            "appKey": "1",
            "appSecret": "1",
            "channel": "1",
            "description": "1",
            "master": "1",
            "phone": "1",
            "platform": "淘宝网",
            "sendExpired": 1,
            "shopName": "linsw店铺2021",
            "warehouse": "linsw仓库2021",
            "warehouseAddress": "北京",
            "warehouseId": 1769
        })
    )
    teststeps = [
        Step(
            RunTestCase("管理员登录")
            .call(SmokeLogin)
            .export("Associate_Token")
        ),
        Step(
            RunTestCase("新建店铺")
            .call(SmokeNewStore)
        ),
        Step(
            RunTestCase("查询新建的店铺")
            .call(SmokeSelectStore)
            .export("Associate_StoreId")
        ),
        Step(
            RunTestCase("删除店铺")
            .call(SmokeDeleteStore)
        ),
        Step(
            RunTestCase("查询被删除的店铺")
            .call(SmokeDeleteSelectStore)
        )
    ]

if __name__ == "__main__":
    TestStoreMangement().test_start()