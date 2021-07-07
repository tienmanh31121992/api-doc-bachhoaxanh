"""
@api {get} /promotions Lấy danh sách khuyến mãi
@apiName Lấy_danh_sách_khuyến_mãi
@apiGroup Khuyến_mãi
@apiVersion 1.0.0
@apiDescription Lấy danh sách khuyến mãi


@apiParam {Number} [customer_id] <mark>ID khách hàng</mark>
@apiParam {Number} [product_group_id] <mark>ID nhóm sản phẩm</mark>
@apiParam {Number} [brand_id] <mark>ID thương hiệu</mark>
@apiParam {Number=≥0} [page=0] <mark>Vị trí trang yêu cầu</mark>
@apiParam {Number=≥1} [per_page=1] <mark>Số item trên một trang</mark>

@apiParamExample {String} URL request:
{host}/api/v1.0/promotions?customer_id=10?page=0&per_page=4


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object}    O.data Danh sách thông tin khuyến mãi
@apiSuccess {Number}    O.data.id ID sản phẩm
@apiSuccess {String}    O.data.promotion_code Mã khuyến mãi
@apiSuccess {String}    O.data.promotion_name Tên khuyến mãi
@apiSuccess {String}    O.data.content Nội dung khuyến mãi
@apiSuccess {String}    O.data.image_link Link lưu ảnh khuyến mãi
@apiSuccess {Number}    O.data.promotion_type Loại khuyến mãi

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách khuyến mãi!",
    "data": [
        {
            "id": 1,
            "promotion_code": "KM0001",
            "promotion_name": "Miễn phí giao",
            "content": "Miễn phí giao cho 5 đơn đầu tiên từ 100.000đ, không áp dụng hàng to, nặng",
            "image_link": "image1.png",
            "rule_id": 1
        },
        {
            "id": 2,
            "promotion_code": "KM0002",
            "promotion_name": "Khuyến mãi đến 50%",
            "content": "Hàng ngàn sản phẩm có giá khuyến mãi cực sốc, giảm đến 50%",
            "image_link": "image2.png",
            "rule_id": 2
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
    "message": "Xảy ra lỗi khi lấy thông tin khuyễn mãi: Mô tả lỗi."
}
"""