"""
@api {get} /sector Lấy danh sách khu vực
@apiName Lấy_danh_sách_khu_vực
@apiGroup Địa_chỉ
@apiVersion 1.0.0
@apiDescription Lấy danh sách khu vực


@apiParamExample {JSON} URL request:
https://www.bachhoaxanh.com/api/v1/sector


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin khu vực
@apiSuccess {Number}    data.id ID khu vực
@apiSuccess {Number}    data.parent_id ID khu vực cha
@apiSuccess {String}    data.code Mã nhóm sản phẩm
@apiSuccess {String}    data.name Tên nhóm sản phẩm
@apiSuccess {Number}    data.level Cấp khu vực
@apiSuccess {Object[]}  data.child Danh sách thông tin khu vực con
@apiSuccess {Number}    data.child.id ID khu vực
@apiSuccess {Number}    data.child.parent_id ID khu vực cha
@apiSuccess {String}    data.child.code Mã nhóm sản phẩm
@apiSuccess {String}    data.child.name Tên nhóm sản phẩm
@apiSuccess {Number}    data.child.level Cấp khu vực
@apiSuccess {Object[]}  data.child.child Danh sách thông tin khu vực con
@apiSuccess {Number}    data.child.child.id ID khu vực
@apiSuccess {Number}    data.child.child.parent_id ID khu vực cha
@apiSuccess {String}    data.child.child.code Mã nhóm sản phẩm
@apiSuccess {String}    data.child.child.name Tên nhóm sản phẩm
@apiSuccess {Number}    data.child.child.level Cấp khu vực

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách khu vực thành công!",
    "data": [
        {
            "id": 1,
            "parent_id": 0,
            "code": "NSP0001",
            "name": "TP. Hồ Chí Minh",
            "level": 1,
            "child": [
                {
                    "id": 68,
                    "parent_id": 1,
                    "code": "NSP0068",
                    "name": "Quận 1",
                    "level": 2,
                    "child": [
                         {
                            "id": 70,
                            "parent_id": 68,
                            "code": "NSP0068",
                            "name": "An Khánh",
                            "level": 3
                        }
                    ]
                },
                {
                    "id": 69,
                    "parent_id": 1,
                    "code": "NSP0069",
                    "name": "Quận 2",
                    "level": 2,
                    "child": [
                         {
                            "id": 71,
                            "parent_id": 69,
                            "code": "NSP0071",
                            "name": "Nhà Thờ",
                            "level": 3
                        }
                    ]
                }
            ]
        },
        {
            "id": 2,
            "parent_id": 0,
            "code": "NSP0001",
            "name": "An Giang",
            "level": 1,
            "child": [
                {
                    "id": 80,
                    "parent_id": 2,
                    "code": "NSP0069",
                    "name": "TP. Châu Đốc",
                    "level": 2,
                    "child": [
                         {
                            "id": 82,
                            "parent_id": 80,
                            "code": "NSP0071",
                            "name": "Hòa An",
                            "level": 3
                        }
                    ]
                }                
            ]
        }
    ]
}


@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
<ul>
    <li><code>code:</code> 416</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy quảng cáo: Mô tả lỗi."
}
"""