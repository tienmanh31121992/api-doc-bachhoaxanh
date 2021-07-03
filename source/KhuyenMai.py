"""
@api {get} /promotion Lấy số lượng hàng đang khuyến mãi
@apiName Số_lượng_khuyến_mãi
@apiGroup Khuyến_mãi
@apiVersion 1.0.0
@apiDescription Lấy số lượng sản phẩm đang được khuyến mãi

@apiParam {String} sum_of <mark>Loại đối tượng cần tính số lượng khuyến mãi</mark>
<ul>
    <li><code>product:</code> Sản phẩm</li>
    <li><code>product_group:</code> Nhóm sản phẩm</li>
    <li><code>brand:</code> Thương hiệu</li>
</ul>

@apiParamExample {String} URL request:
https://www.bachhoaxanh.com/api/v1/promotion?sum_of=product


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Number}    data Tổng số sản phẩm đang được khuyễn mãi

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy số lượng hàng khuyến mãi thành công!",
    "data": 1234
}


@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
<ul>
    <li><code>code:</code> 404</li>
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
    "message": "Xảy ra lỗi khi lấy số lượng hàng đang khuyễn mãi: Mô tả lỗi."
}
"""