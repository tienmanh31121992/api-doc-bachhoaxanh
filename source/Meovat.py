"""
   @api {get} /articles Xem danh sách mẹo vặt (bài viết)
   @apiName Xem_danh_sách_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Hiển thị danh sách các mẹo vặt (bài viết)

   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object[]} Object.data Đối tượng trả về
   @apiSuccess {Object} Object.data.aritcle_group Đối tượng nhóm bài viết
   @apiSuccess {String} Object.data.aritcle_group.group_name tên nhóm bài viết
   @apiSuccess {Object} Object.data.aritcle_group.article Đối tượng bài viết
   @apiSuccess {String} Object.data.aritcle_group.article.article_name tên bài viết
   @apiSuccess {String} Object.data.aritcle_group.article.title tiêu đề bài viết
   @apiSuccess {String} Object.data.aritcle_group.article.thumbnail_link ảnh đại diện bài viết
   @apiSuccess {String} Object.data.aritcle_group.article.views_count Đếm số lượt xem
   @apiSuccess {String} Object.data.aritcle_group.article.comments_count Đếm số lượt comment


   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Load danh sách bài viết thành công!",
       "data": {
            "article_group": [
                   {
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
                       ]
                   },
                   {
                       "group_name": "Bạn đọc chia sẻ",
                       "article": [
                             {
                                 "article_name": "Chàng sinh viên chia sẻ cách làm trắng răng đơn giản bằng nguyên liệu nhà nào cũng có",
                                 "title": "Làm trắng răng tại nhà vô cùng đơn giản chỉ bằng những nguyên liệu tự nhiên...",
                                 "thumbnail_link": "article3.png",
                                 "views_count": 650,
                                 "comments_count": 1
                             }
                       ]
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
        "message": "Lỗi load danh sách bài viết!"
    }
"""
"""
   @api {get} /articles/view-article Xem bài viết
   @apiName Xem_bài_viết
   @apiGroup Mẹo_vặt
   @apiVersion  1.0.0
   @apiDescription Khách hàng vào xem bài viết

   @apiParam  {Number} article_id id bài viết

   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/articles/view-article?article_id=1
   
   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object[]} Object.data Đối tượng trả về
   @apiSuccess {String} Object.data.article_name tên bài viết
   @apiSuccess {String} Object.data.title tiêu đề bài viết
   @apiSuccess {String} Object.data.content_html nội dung bài viết với định dạng html
   @apiSuccess {String} Object.data.created_at ngày tạo bài viết
   @apiSuccess {String} Object.data.updated_at ngày sửa bài viết
   @apiSuccess {Object} Object.data.tag Đối tượng tag bài viết
   @apiSuccess {Object} Object.data.same_tag_suggestion Đối tượng gợi ý cùng tag
   @apiSuccess {Object} Object.data.similar_tag_suggestion Đối tượng gợi ý giống tag
   @apiSuccess {Number} Object.data.tag_id id tag bài viết
   @apiSuccess {String} Object.data.tag_name tên tag
   @apiSuccess {Number} Object.data.thumbnail_link ảnh đại diện bài viết

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Load bài viết thành công!",
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
            ],
            "similar_tag_suggestion": [
                 {  
                      "tag_id": 1,
                      "article_name": "Cách phân biệt nấm ăn được và nấm độc"
                 },
                 {  
                      "tag_id": 3,
                      "article_name": "Đi mua nấm nên chú ý điều này!"
                 }
            ],
            "same_tag_suggestion": [
                  {
                      "tag_id": 2,
                      "article_name": "Cách làm nấm mối xào ngon nhất",
                      "thumbnail_link": "article1.png"
                  },
                  {
                      "tag_id": 2,
                      "article_name": "Cách sơ chế nấm mối",
                      "thumbnail_link": "article2.png"
                  },
                  {
                      "tag_id": 2,
                      "article_name": "Cách làm nấm mối hấp ngon, bổ, rẻ",
                      "thumbnail_link": "article3.png"
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
        
   @apiParamExample  {JSON} Success 200:
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

   @apiParamExample  {JSON} Success 200:
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