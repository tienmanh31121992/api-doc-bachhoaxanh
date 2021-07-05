"""
@api {post} /feedback Gửi bình luận đánh giá
@apiName Gửi_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Gửi bình luận đánh giá

@apiHeader {String} Content-Type <mark>application/json</mark>


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {Number} product_id ID sản phẩm
@apiParam (Body) {Number} article_id ID bài viết
@apiParam (Body) {Number} admin_id ID quản trị viên
@apiParam (Body) {Number} parent_id ID bài viết gốc
@apiParam (Body) {String} name Tên người viết bài
@apiParam (Body) {String} phone Số điện thoại
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
    "article_id": null,
    "admin_id": null,
    "parent_id": 0,
    "name": "Hòa",
    "phone": "123123123",
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
@apiParam {Number} [product_id] <mark>ID sản phẩm</mark>
@apiParam {Number} [article_id] <mark>ID bài viết</mark>
@apiParam {Number} feedback_type <mark>Loại bình luận, đánh giá</mark>
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiParam {String} sort_by=created_at <mark>Sắp xếp theo</mark>
@apiParam {String} sort_order=desc <mark>Kiểu sắp xếp</mark>
@apiParam {Number} page=1 <mark>Vị trí trang cần lấy dữ liệu</mark>
@apiParam {Number} per_page=2 <mark>Số bài viết trên một trang</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/product?product_id=10&feedback_type=1&sort_by=created_at&sort_order=desc&page=1&per_page=2


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
@apiSuccess {Number}    Object.data.customer.id Mã khách hàng
@apiSuccess {String}    Object.data.customer.customer_name Tên khách hàng
@apiSuccess {Object}    Object.data.customer Thông tin khách hàng
@apiSuccess {Number}    Object.data.admin.id Mã quản trị viên
@apiSuccess {String}    Object.data.admin.admin_name Tên quản trị viên
@apiSuccess {Object}    Object.data.admin Thông tin quản trị viên
@apiSuccess {Object[]}  Object.data.child Danh sách các bình luận, đánh giá con
@apiSuccess {Number}    Object.data.child.id ID bình luận, đánh giá
@apiSuccess {Number}    Object.data.child.parent_id ID bài viết gốc
@apiSuccess {Number}    Object.data.child.feedback_type ID bình luận, đánh giá
@apiSuccess {Date}      Object.data.child.created_at Ngày gửi bài viết
@apiSuccess {String}    Object.data.child.content Nội dung
@apiSuccess {String[]}  Object.data.child.media Danh sách đường dẫn lưu phương tiện của bài viết
@apiSuccess {Number}    Object.data.child.likes Lượt thích
@apiSuccess {Object}    Object.data.child.customer Thông tin khách hàng
@apiSuccess {Number}    Object.data.child.customer.id Mã khách hàng
@apiSuccess {String}    Object.data.child.customer.customer_name Tên khách hàng
@apiSuccess {Object}    Object.data.child.admin Thông tin quản trị viên
@apiSuccess {Number}    Object.data.child.admin.id Mã quản trị viên
@apiSuccess {String}    Object.data.child.admin.admin_name Tên quản trị viên
@apiSuccess {Object}    Object.paging Thông tin phân trang
@apiSuccess {Number}    Object.paging.page Vị trí trang yêu cầu
@apiSuccess {Number}    Object.paging.per_page Số  bài viết trên một trang
@apiSuccess {Number}    Object.paging.total_page Tổng số trang
@apiSuccess {Number}    Object.paging.total_count Tổng số bài viết
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
    ],
    "paging":{
        "page": 1,
        "per_page": 2,
        "page_count": 10,
        "total_count": 20
    }
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