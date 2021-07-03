"""
@api {post} /feedback Viết bình luận đánh giá
@apiName Viết_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Viết bình luận đánh giá

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
@api {get} /feedback Lấy luận đánh giá
@apiName Lấy_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Lấy bình luận đánh giá
"""