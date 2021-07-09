"""
@api {get} /sectors Lấy danh sách khu vực
@apiName Lấy_danh_sách_khu_vực
@apiGroup Địa_chỉ
@apiVersion 1.0.0
@apiDescription Lấy danh sách khu vực


@apiParam {Number} parent_id <mark>ID khu vực cha
<br><code>parent_id=0:</code> Lấy khu vực cấp tỉnh</mark>

@apiParam {String=id,sector_code,sector_name} sort=+id <mark>Sắp xếp dữ liệu. Ví dụ: <code>sort=+field_1,-field_2,field_3</code></mark>
<ul>
    <li><code>+:</code> Sắp xếp tăng dần</li>
    <li><code>-:</code> Sắp xếp giảm dần</li>
    <li><code>Mặc định:</code> Sắp xếp tăng dần</li>
</ul>

@apiParamExample URL request:
{host}/api/v1.0/sectors?parent_id=0&sort=+id


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin khu vực
@apiSuccess {Number}    O.data.sector_id ID khu vực
@apiSuccess {Number}    O.data.parent_id ID khu vực cha
@apiSuccess {String}    O.data.sector_code Mã khu vực
@apiSuccess {String}    O.data.sector_name Tên khu vực
@apiSuccess {Number}    O.data.level Cấp khu vực


@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách khu vực thành công!",
    "data": [
        {
            "sector_id": 1,
            "parent_id": 0,
            "sector_code": "TINH001",
            "sector_name": "TP. Hồ Chí Minh",
            "level": 1
        },
        {
            "sector_id": 2,
            "parent_id": 0,
            "sector_code": "TINH002",
            "sector_name": "An Giang",
            "level": 1
        },
        {
            "sector_id": 3,
            "parent_id": 0,
            "sector_code": "TINH003",
            "sector_name": "Bạc Liêu",
            "level": 1
        },
        {
            "sector_id": 4,
            "parent_id": 0,
            "sector_code": "TINH004",
            "sector_name": "Bến Tre",
            "level": 1
        },
        {
            "sector_id": 5,
            "parent_id": 0,
            "sector_code": "TINH005",
            "sector_name": "Bình Dương",
            "level": 1
        },
        {
            "sector_id": 6,
            "parent_id": 0,
            "sector_code": "TINH006",
            "sector_name": "Bình Phước",
            "level": 1
        },
        {
            "sector_id": 7,
            "parent_id": 0,
            "sector_code": "TINH007",
            "sector_name": "Bình Thuận",
            "level": 1
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