"""
   @api {get} /articles Lấy danh sách bài viết theo nhóm bài viết
   @apiName Lấy_danh_sách_bài_viết_theo_nhóm
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Hiển thị danh sách các bài viết (mẹo vặt) theo nhóm bài viết

   @apiParam {String} sort_by điều kiện sắp xếp <p>(ví dụ sắp xếp theo ngày tạo)</p>
   @apiParam {String} sort_type kiểu sắp xếp <p>(Tăng dần hoặc giảm dần)</p>
   @apiParam {String} article_group.id id nhóm bài viết
   @apiParam {Number} page thứ tự trang <p>(page=0 là trang đầu tiên, page=1 là trang thứ 2)</p>
   @apiParam {Number} per_page số lượng phần tử trong 1 trang

   @apiParamExample {JSON} Body Request:
   {
       "sort_by": "date_created",
       "sort_type": "desc",
       "id": 1,
       "page": 0,
       "per_page": 10
   }

   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object} Object.data Đối tượng trả về
   @apiSuccess {String} Object.data.group_name tên nhóm bài viết
   @apiSuccess {Object[]} Object.data.article Đối tượng bài viết
   @apiSuccess {String} Object.data.article.article_name tên bài viết
   @apiSuccess {String} Object.data.article.title tiêu đề bài viết
   @apiSuccess {String} Object.data.article.thumbnail_link ảnh đại diện bài viết
   @apiSuccess {Number} Object.data.article.views_count Đếm số lượt xem
   @apiSuccess {Object} Object.data.paging Đối tượng phân trang
   @apiSuccess {String} Object.data.paging.page Số thứ tự trang
   @apiSuccess {String} Object.data.paging.per_page số lượng phần tử mỗi trang
   @apiSuccess {String} Object.data.paging.total_items tổng số lượng phần tử
   @apiSuccess {String} Object.data.paging.total_pages tổng số trang

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Hiển thị danh sách bài viết thành công!",
       "data": {
             "group_name": "Mẹo hay mới",
             "article": [
                {
                    "article_name": "Vì sao lấy mẫu xét nghiệm Covid lúc nào cũng lấy nhóm 10 hoặc 15 người?",
                    "title": "Nhiều người khi đi xét nghiệm luôn thắc mắc câu hỏi vì sao...",
                    "thumbnail_link": "article1.png",
                    "views_count": 450,
                    "comments_count": 0
                },
                {
                    "article_name": "Nấm mối là nấm gì mà giá 1 triệu/kg vẫn có người sẵn sàng mua?",
                    "title": "Nấm mối là nguyên liệu không thể thiếu trong các món ăn ngon, hấp dẫn...",
                    "thumbnail_link": "article2.png",
                    "views_count": 550,
                    "comments_count": 1
                }
             ],
             "paging": {
                    "page":0,
                    "per_page": 10,
                    "total_items": 1000,
                    "total_pages": 100
             }
       }
   }

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
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
        "message": "Yêu cầu không hợp lệ!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Lỗi hiển thị danh sách bài viết!"
    }
"""
"""
   @api {get} /articles Lấy danh sách bài viết theo tag
   @apiName Lấy_danh_sách_bài_viết_theo_tag
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Hiển thị danh sách các bài viết (mẹo vặt) theo tag

   @apiParam {String} sort_by điều kiện sắp xếp <p>(ví dụ sắp xếp theo ngày tạo)</p>
   @apiParam {String} sort_type kiểu sắp xếp <p>(Tăng dần hoặc giảm dần)</p>
   @apiParam {String} tag.id id tag bài viết
   @apiParam {Number} page thứ tự trang <p>(page=0 là trang đầu tiên, page=1 là trang thứ 2)</p>
   @apiParam {Number} per_page số lượng phần tử trong 1 trang

   @apiParamExample {JSON} Body Request:
   {
       "sort_by": "date_created",
       "sort_type": "desc",
       "id": 1,
       "page": 0,
       "per_page": 10
   }

   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object} Object.data Đối tượng trả về
   @apiSuccess {String} Object.data.tag_name tên tag
   @apiSuccess {Object[]} Object.data.article Đối tượng bài viết
   @apiSuccess {String} Object.data.article.article_name tên bài viết
   @apiSuccess {String} Object.data.article.title tiêu đề bài viết
   @apiSuccess {String} Object.data.article.thumbnail_link ảnh đại diện bài viết
   @apiSuccess {Number} Object.data.article.views_count Đếm số lượt xem
   @apiSuccess {Object} Object.data.paging Đối tượng phân trang
   @apiSuccess {String} Object.data.paging.page Số thứ tự trang
   @apiSuccess {String} Object.data.paging.per_page số lượng phần tử mỗi trang
   @apiSuccess {String} Object.data.paging.total_items tổng số lượng phần tử
   @apiSuccess {String} Object.data.paging.total_pages tổng số trang

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Hiển thị danh sách bài viết thành công!",
       "data": {
             "group_name": "bạch tuộc",
             "article": [
                {
                    "article_name": "Cách chế biến món bạch tuộc chiên giòn",
                    "title": "Có rất nhiều cách chế biến món bạch tuộc chiên giòn...",
                    "thumbnail_link": "article1.png",
                    "views_count": 450,
                    "comments_count": 0
                },
                {
                    "article_name": "Các cách chọn bạch tuộc ngon",
                    "title": "Hiện nay trên thị trường có rất nhiều loại bạch tuộc...",
                    "thumbnail_link": "article2.png",
                    "views_count": 550,
                    "comments_count": 1
                }
             ],
             "paging": {
                    "page":0,
                    "per_page": 10,
                    "total_items": 1000,
                    "total_pages": 100
             }
       }
   }

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
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
        "message": "Yêu cầu không hợp lệ!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Lỗi hiển thị danh sách bài viết!"
    }
"""
"""
   @api {get} /articles/view-article Xem bài viết
   @apiName Xem_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng vào xem bài viết

   @apiParam  {Number} article.id id bài viết

   @apiParamExample  {JSON} Cách truyền parameter:
   {host}/api/v1.0/articles/view-article?id=1
   
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object} Object.data Đối tượng trả về
   @apiSuccess {String} Object.data.article_name tên bài viết
   @apiSuccess {String} Object.data.title tiêu đề bài viết
   @apiSuccess {String} Object.data.content_html nội dung bài viết với định dạng html
   @apiSuccess {String} Object.data.created_at ngày tạo bài viết
   @apiSuccess {String} Object.data.updated_at ngày sửa bài viết
   @apiSuccess {Object[]} Object.data.tag Đối tượng tag bài viết
   @apiSuccess {Number} Object.data.tag.tag_id id tag bài viết
   @apiSuccess {String} Object.data.tag.tag_name tên tag

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Hiển thị bài viết thành công!",
       "data": {
            "article_name": "Nấm mối là nấm gì mà giá 1 triệu/kg vẫn có người sẵn sàng mua?",
            "title": "Nấm mối là nguyên liệu không thể thiếu trong các món ăn ngon...",
            "content_html": "<html>...</html>",
            "created_at": "2/7/2021",
            "updated_at": "3/7/2021",
            "tag": [
                 {  
                     "tag_id": 1,
                     "tag_name": "nấm"
                 },
                 {  
                     "tag_id": 2,
                     "tag_name": "nấm mối"
                 },
                 {  
                     "tag_id": 3,
                     "tag_name": "các món ngon từ nấm"
                 }
            ]   
       }
   }

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
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
        "message": "Yêu cầu không hợp lệ!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Lỗi không hiển thị được dữ liệu bài viết!"
    }
"""
"""
   @api {post} /articles/send-article Đăng bài viết
   @apiName Đăng_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng đăng bài viết

   @apiParam (Body) {Number} Object.customer_id id khách hàng
   @apiParam (Body) {Number} Object.title tiêu đề bài viết
   @apiParam (Body) {Number} Object.content nội dung bài viết
   @apiParam (Body) {Object[]} Object.article_image Đối tượng ảnh bài viết
   @apiParam (Body) {String} Object.article_image.image_link Đối tượng ảnh bài viết
        
   @apiParamExample  {JSON} Body Request:
   {            
         "customer_id": 1,
         "title": "Chia sẻ cách bảo quản thịt trong tủ lạnh",
         "content": "Để bảo quản thịt trong tủ lạnh bạn cần phải...",
         "article_image": [
                {
                   "image_link": "image1.png"
                },
                {
                   "image_link": "image2.png"
                },
                {
                   "image_link": "image3.png"
                }
         ]
   }
   
   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   
   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Gửi bài viết thành công!",
   }    

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
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
        "message": "Yêu cầu không hợp lệ!"
    }    
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Không thể gửi bài viết!"
    }  
"""
"""
   @api {post} /articles/update-article Sửa bài viết
   @apiName Sửa_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng đăng bài viết

   @apiParam (Body) {Number} Object.article_id id bài viết
   @apiParam (Body) {Number} Object.title tiêu đề bài viết
   @apiParam (Body) {Number} Object.content nội dung bài viết
   @apiParam (Body) {Object[]} Object.article_image Đối tượng ảnh bài viết
   @apiParam (Body) {String} Object.article_image.image_link Đối tượng ảnh bài viết

   @apiParamExample  {JSON} Body Request:
   {            
         "aritcle_id": 1,
         "title": "Chia sẻ cách bảo quản cá trong tủ lạnh",
         "content": "Để bảo quản cá trong tủ lạnh bạn cần phải...",
         "article_image": [
                {
                   "image_link": "image1.png"
                },
                {
                   "image_link": "image2.png"
                },
                {
                   "image_link": "image3.png"
                }
         ]
   }

   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Gửi yêu cầu cập nhật bài viết thành công!",
   }    

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
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
        "message": "Yêu cầu không hợp lệ!"
    }    
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Không thể gửi yêu cầu cập nhật bài viết!"
    }  
"""
"""
   @api {delete} /articles/delete-article Xóa bài viết
   @apiName Xóa_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng xóa bài viết

   @apiParam {Number} article_id id bài viết

   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/articles/delete-article?article_id=1
   
   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Xóa bài viết thành công!",
   }    

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
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
        "message": "Yêu cầu không hợp lệ!"
    }    
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Không thể xóa bài viết!"
    }  
"""