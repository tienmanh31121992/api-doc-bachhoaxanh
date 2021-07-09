"""
   @api {get} /articles Lấy danh sách bài viết
   @apiName Lấy_danh_sách_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Hiển thị danh sách các bài viết (mẹo vặt)

   @apiParam (Body) {Number} article_group_id id nhóm bài viết
   @apiParam (Body) {Number} tag_id id tag bài viết
   @apiParam (Body) {String} sort_by điều kiện sắp xếp <p>(ví dụ sắp xếp theo ngày tạo)</p>
   @apiParam (Body) {String} sort_type kiểu sắp xếp <p>(Tăng dần hoặc giảm dần)</p>
   @apiParam (Body) {Number} page thứ tự trang <p>(page=0 là trang đầu tiên, page=1 là trang thứ 2)</p>
   @apiParam (Body) {Number} per_page số lượng phần tử trong 1 trang

   @apiParamExample {JSON} Body Request:
   {
       "article_group_id": 1,
       "tag_id": null,
       "sort_by": "date_created",
       "sort_type": "desc",
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
   @api {get} /articles/<article_id> Xem bài viết
   @apiName Xem_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng vào xem bài viết

   @apiParamExample  {JSON} Cách gọi URL:
   {host}/api/v1.0/articles/1
   
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
   @api {post} /articles Đăng bài viết
   @apiName Đăng_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng đăng bài viết
   
   @apiHeader {String} Content-Type <mark>application/json</mark>
   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>


   @apiHeaderExample  {JSON} Header mẫu:
   {
       "Content-Type": "application/json",
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }

   @apiParam (Body) {String} customer_id id khách hàng
   @apiParam (Body) {String} title tiêu đề bài viết
   @apiParam (Body) {String} content nội dung bài viết
   @apiParam (Body) {String} image_link link ảnh bài viết
          
   @apiParamExample  {JSON} Body Request:
   {     
         "customer_id": 1,       
         "title": "Chia sẻ cách bảo quản thịt trong tủ lạnh",
         "content": "Để bảo quản thịt trong tủ lạnh bạn cần phải...",
         "articleimage": [
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
   
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   
   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Gửi bài viết thành công,đang chờ xét duyệt!",
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
   @api {delete} /articles/<article_id> Xóa bài viết
   @apiName Xóa_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng xóa bài viết
   
   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

   @apiHeaderExample  {JSON} Header mẫu:
   {
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }

   @apiParamExample  {JSON} Cách gọi URL:
   {host}/api/v1.0/articles/1
   
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
"""
   @api {get} /articles/<customer_id> Lấy danh sách bài viết khách hàng đã đăng
   @apiName Lấy_danh_sách_bài_viết_đã_đăng
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Lấy ra danh sách bài viết đã đăng của khách hàng

   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

   @apiHeaderExample  {JSON} Header mẫu:
   {
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }

   @apiParamExample  {JSON} Cách gọi URL:
   {host}/api/v1.0/articles/1

   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object} Object.data Kết quả trả về
   @apiSuccess {Object[]} Object.data.article Đối tượng bài viết
   @apiSuccess {String} Object.data.article.article_name tên bài viết
   @apiSuccess {String} Object.data.article.title tiêu đề
   @apiSuccess {String} Object.data.article.content nội dung
   @apiSuccess {String} Object.data.article.thumbnail_link ảnh đại diện bài viết
   @apiSuccess {String} Object.data.article.status trạng thái bài viết
   <ul>
        <li><code>0:</code>Đang chờ duyệt</li>
        <li><code>1:</code>Đã bị từ chối</li>
        <li><code>2:</code>Khách hàng đã xóa</li>
        <li><code>3:</code>Đã được duyệt</li>
    </ul>

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Lấy danh sách thành công!",
       "data": {
            "articles": [
                {
                    "article_name": "Tên bài viết 1",
                    "title": "Tiêu đề 1",
                    "content": "Nội dung 1",
                    "thumbnail_link": "image1.png",
                    "status": 0
                },
                {
                    "article_name": "Tên bài viết 2",
                    "title": "Tiêu đề 2",
                    "content": "Nội dung 2",
                    "thumbnail_link": "image2.png"
                    "status": 1
                },
                {
                    "article_name": "Tên bài viết 3",
                    "title": "Tiêu đề 3",
                    "content": "Nội dung 3",
                    "thumbnail_link": "image3.png"
                    "status": 2
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
        "message": "Không thể xóa bài viết!"
    }  
"""