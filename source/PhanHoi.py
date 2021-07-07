"""
@api {post} /feedbacks Gửi bình luận đánh giá
@apiName Gửi_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Gửi bình luận đánh giá


@apiHeader {String} Content-Type <mark>application/json</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json"
}


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {Number} product_id ID sản phẩm
@apiParam (Body) {Number} article_id ID bài viết
@apiParam (Body) {Number} admin_id ID quản trị viên
@apiParam (Body) {Number} parent_id ID bình luận, nhận xét gốc
@apiParam (Body) {String} name Tên người viết bài
@apiParam (Body) {String} phone Số điện thoại người viết bài
@apiParam (Body) {Number=1,2,3,4,5} rating=5 Số sao đánh giá
@apiParam (Body) {Number=1,2} feedback_type Loại bình luận, đánh giá
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiParam (Body) {String} content Nội dung bình luận, đánh giá
@apiParam (Body) {String[]} media Danh sách đường dẫn ảnh của bình luận, đánh giá

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

@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

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
@api {get} /feedbacks Lấy bình luận đánh giá
@apiName Lấy_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Lấy bình luận đánh giá


@apiParam {String} [keywork] <mark>Từ khóa tìm kiếm</mark>
@apiParam {Number} [product_id] <mark>ID sản phẩm</mark>
@apiParam {Number} [article_id] <mark>ID bài viết</mark>
@apiParam {Number=1,2} feedback_type <mark>Loại bình luận, đánh giá</mark>
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiParam {String=created_at} sort=-created_at <mark>Sắp xếp dữ liệu</mark>
<ul>
    <li><code>+:</code> Tăng dần</li>
    <li><code>-:</code> Giảm dần</li>
</ul>
@apiParam {Number=≥0} page=0 <mark>Vị trí trang yêu cầu</mark>
@apiParam {Number=≥1} per_page=1 <mark>Số item trên một trang</mark>

@apiParamExample URL request:
{host}/api/v1.0/feedbacks?product_id=10&feedback_type=1&sort_by=-created_at&page=0&per_page=2


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách bình luận, đánh giá
@apiSuccess {Number}    O.data.id ID bình luận, đánh giá
@apiSuccess {Number}    O.data.parent_id ID bình luận, đánh giá gốc
@apiSuccess {Number}    O.data.feedback_type Loại bình luận, đánh giá
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiSuccess {Date}      O.data.created_at Ngày gửi bài viết
@apiSuccess {String}    O.data.content Nội dung
@apiSuccess {String[]}  O.data.media Danh sách đường dẫn lưu phương tiện của bài viết
@apiSuccess {Number}    O.data.likes Lượt thích
@apiSuccess {String}    O.data.author_name Tên tác giả
@apiSuccess {Object[]}  O.data.child Danh sách các bình luận, đánh giá con
@apiSuccess {Number}    O.data.child.id ID bình luận, đánh giá
@apiSuccess {Number}    O.data.child.parent_id ID bài viết gốc
@apiSuccess {Number}    O.data.child.feedback_type Loại bình luận, đánh giá
<ul>
    <li><code>1:</code> Đánh giá</li>
    <li><code>2:</code> Bình luận</li>
</ul>
@apiSuccess {Date}      O.data.child.created_at Ngày gửi bài viết
@apiSuccess {String}    O.data.child.content Nội dung
@apiSuccess {String[]}  O.data.child.media Danh sách đường dẫn lưu phương tiện của bài viết
@apiSuccess {Number}    O.data.child.likes Lượt thích
@apiSuccess {String}    O.data.child.author_name Tên tác giả
@apiSuccess {Object}    O.paging Thông tin phân trang
@apiSuccess {Number}    O.paging.page Vị trí trang yêu cầu
@apiSuccess {Number}    O.paging.per_page Số  bài viết trên một trang
@apiSuccess {Number}    O.paging.total_page Tổng số trang
@apiSuccess {Number}    O.paging.total_item Tổng số item

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
            "author_name": "Quy",
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
            "author_name": "Hoa"
            "child": null
        }
    ],
    "paging":{
        "page": 0,
        "per_page": 2,
        "total_page": 11,
        "total_item": 21
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

"""
@api {post} /feedbacks/<id>/likes Thích bình luận đánh giá
@apiName Thích_bình_luận_đánh_giá
@apiGroup Bình_luận_đánh_giá
@apiVersion 1.0.0
@apiDescription Thích một bình luận đánh giá


@apiParam (Path) {Number} id <mark>ID bình luận, đánh giá</mark>

@apiParamExample {String} URL request:
{host}/api/v1.0/feedbacks/10/likes


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Thích bài viết thành công!"
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
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
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi thích bài viết: Mô tả lỗi."
}
"""