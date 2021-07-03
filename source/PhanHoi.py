"""
@api {post} /feedback Gửi bình luận đánh giá
@apiName Gửi_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Gửi bình luận đánh giá

@apiHeader {String} Content-Type <mark>application/json</mark>


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {Number} product_id ID sản phẩm
@apiParam (Body) {Number} admin_id ID quản trị viên
@apiParam (Body) {Number} parent_id ID bài viết gốc
@apiParam (Body) {Number} rating Số sao đánh giá
@apiParam (Body) {Number} feedback_type Loại bình luận, đánh giá
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiParam (Body) {String} content Nội dung bình luận, đánh giá
@apiParam (Body) {String[]} media Ảnh, video của bình luận, đánh giá

@apiParamExample {JSON} Body request:
{
    "customer_id": 12,
    "product_id": 22,
    "admin_id": null,
    "parent_id": 0,
    "rating": 5,
    "feedback_type": 1,
    "content": "Sản phẩm chất lượng",
    "media": [
        "anh_1",
        "anh_2"
    ]
}

@apiSuccess {String} code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Gửi bài viết thành công!"
}

@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi gửi bài viết: Mô tả lỗi."
}
"""

"""
@api {get} /feedback Lấy bình luận đánh giá
@apiName Lấy_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Lấy bình luận đánh giá


@apiParam {String} [keywork] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} product_id <mark>ID nhóm sản phẩm</mark>
@apiParam {Number} feedback_type <mark>ID nhóm sản phẩm</mark>
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiParam {String} sort_by <mark>Sắp xếp theo: Mặc định là created_at</mark>
@apiParam {String} sort_order <mark>Kiểu sắp xếp: Mặc định desc</mark>
@apiParam {Number} limit <mark>Giới hạn số lượng bản ghi</mark>
@apiParam {Number} offset <mark>Số phần tử bỏ qua</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/product?product_id=10&feedback_type=1&sort_by=created_at&sort_order=desc&limit=2&offset=0


@apiSuccess {String}    Object.code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    Object.message Thông báo kết quả
@apiSuccess {Object[]}  Object.data Danh sách bình luận, đánh giá
@apiSuccess {Number}    Object.data.id ID bình luận, đánh giá
@apiSuccess {Number}    Object.data.parent_id ID bài viết gốc
@apiSuccess {Number}    Object.data.feedback_type ID bình luận, đánh giá
@apiSuccess {Date}      Object.data.created_at Ngày gửi bài viết
@apiSuccess {String}    Object.data.content Nội dung
@apiSuccess {String[]}  Object.data.media Danh sách đường dẫn lưu phương tiện của bài viết
@apiSuccess {Number}    Object.data.likes Lượt thích
@apiSuccess {Object}    Object.data.customer Thông tin khách hàng đã gửi bài viết
@apiSuccess {Object}    Object.data.admin Thông tin quản trị viên đã gửi bài viết
@apiSuccess {Object[]}  Object.data.child Danh sách các bình luận, đánh giá con

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy danh sách đánh giá thành công!",
    "data": [
        {
            "id": 1,
            "parent_id": 0,
            "rating": 5,
            "feedback_type": 1,
            "created_at": "01/07/2021",
            "content": "Sản phẩm chất lượng",
            "media": [
                "anh_1",
                "anh_2"
            ],
            "likes": 10,
            "customer": {
                "customer_id": 12,
                "customer_name": "Quy"
            },
            "admin": null,
            "child": null
        },
        {
            "id": 2,
            "parent_id": 0,
            "rating": 5,
            "feedback_type": 1,
            "created_at": "01/07/2021",
            "content": "Sản phẩm tốt",
            "media": [
                "anh_3",
                "anh_4"
            ],
            "likes": 12,
            "customer": {
                "customer_id": 13,
                "customer_name": "Hoa"
            },
            "admin_id": null,
            "child": null
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
    "message": "Xảy ra lỗi khi lấy thông tin sản phẩm: Mô tả lỗi."
}
"""