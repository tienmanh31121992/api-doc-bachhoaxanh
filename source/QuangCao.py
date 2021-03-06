"""
@api {get} /ads Lấy quảng cáo
@apiName Lấy_quảng_cáo
@apiGroup Quảng_cáo
@apiVersion 1.0.0
@apiDescription Quảng cáo


@apiParam {Number} [product_group_id] <mark>ID nhóm sản phẩm</mark>
@apiParam {Number} [brand_id] <mark>ID thương hiệu</mark>
@apiParam {Number} [product_id] <mark>ID sản phẩm</mark>
@apiParam {Number} [sector_id] <mark>ID khu vực</mark>
@apiParam {Number} [campaign_id] <mark>ID chiến dịch quảng cáo</mark>
@apiParam {String} position <mark>Vị trí đặt quảng cáo trên trang web</mark>

@apiParamExample URL request:
{host}/api/v1.0/ads?campaign_id=1&position=banner


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object}    O.data Thông tin quảng cáo
@apiSuccess {Number}    O.data.promotion_id ID quảng cáo
@apiSuccess {String}    O.data.promotion_code Mã quảng cáo
@apiSuccess {String}    O.data.promotion_name Tên quảng cáo
@apiSuccess {String}    O.data.position Vị trí đặt quảng cáo
@apiSuccess {Object[]}  O.data.media Danh sách phương tiện cho quảng cáo
@apiSuccess {String}    O.data.media.media_link Đường dẫn đến phương tiện
@apiSuccess {String}    O.data.media.page_link Đường dẫn khi click vào phương tiện


@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy quảng cáo thành công!",
    "data": {
        "promotion_id": 1,
        "promotion_code": "BANNER0001",
        "promotion_name": "Quảng cáo banner 1",
        "position": "banner",
        "media": [
            {
                "media_link": "image1.jpg",
                "page_link": "page_link1"
            },
            {
                "media_link": "image2.jpg",
                "page_link": "page_link2"
            },
            {
                "media_link": "image3.jpg",
                "page_link": "page_link3"
            }
        ]
    }
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