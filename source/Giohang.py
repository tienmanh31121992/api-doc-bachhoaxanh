"""
   @api {get} /cart/<cart_id> Xem giỏ hàng
   @apiName Xem_giỏ_hàng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng vào xem giỏ hàng

   @apiParamExample {JSON} Cách gọi URL:
   {host}/api/v1.0/cart/1

   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object} Object.data Đối tượng trả về
   @apiSuccess {Number} Object.data.ship_fee phí giao hàng dự kiến
   @apiSuccess {Number} Object.data.voucher_id id voucher
   @apiSuccess {Object[]} Object.data.product Đối tượng sản phẩm
   @apiSuccess {Number} Object.data.product.id Sản phẩm id
   @apiSuccess {String} Object.data.product.product_code mã sản phẩm
   @apiSuccess {String} Object.data.product.product_name tên sản phẩm
   @apiSuccess {String} Object.data.product.quantity mua với số lượng
   @apiSuccess {Number} Object.data.product.price giá
   @apiSuccess {Object} Object.data.product.promotion Đối tượng khuyến mãi
   @apiSuccess {Number} Object.data.product.promotion.id id khuyến mãi
   @apiSuccess {Number} Object.data.product.promotion.promotion_name tên khuyến mãi
   @apiSuccess {Number} Object.data.product.promotion.content nội dung khuyến mãi

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Giỏ hàng hiển thị thành công!",
       "data": {
          "ship_fee": 5000,
          "voucher_id": 1,
          "product": [
            {
              "id": 1,
              "product_code": "SP001",
              "product_name": "Thùng 20 lon bia",
              "thumbnail_link": "product1.png",
              "quantity": 1,
              "price": 280000,
              "promotion": null
            },
            {
              "id": 2,
              "product_code": "SP002",
              "product_name": "Thùng 12 gói mì tôm",
              "thumbnail_link": "product2.png",
              "quantity": 2,
              "price": 180000,
              "promotion": {
                    "id": 1,
                    "promotion_name": "Mua 2 tặng 1",
                    "content": "Mua 2 thùng 12 gói mì tôm được tặng thêm 1 thùng mì tôm"
              }
            }
          ]
       }
   }

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
    <ul>
        <li><code>code:</code> 400</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
   @apiError (Error 4xx) 404-NotFound Lỗi không tìm thấy dữ liệu
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
        "message": "Yêu cầu không hợp lệ!"
    }
    @apiErrorExample {JSON} Error 404:
    {
        "code": 404,
        "message": "Giỏ hàng không tồn tại!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Lỗi load giỏ hàng!"
    }
"""
"""
   @api {post} /cart/actions/add-cart Thêm giỏ hàng
   @apiName Thêm_giỏ_hàng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng thêm sản phẩm, giỏ hàng được thêm vào DB
   
   @apiHeader {String} Content-Type <mark>application/json</mark>

   @apiParam  {Number} product_id id Sản phẩm
   @apiParam  {Number} quantity số lượng mua
   
   @apiParamExample {JSON} Body Request:
   {
       "product_id": 1,
       "quantity": 1
   }
   
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object[]} Object.data Đối tượng trả về
   @apiSuccess {Object[]} Object.data.product Đối tượng sản phẩm
   @apiSuccess {String} Object.data.product.product_name Đối tượng sản phẩm
   @apiSuccess {String} Object.data.product.thumbnail_link ảnh sản phẩm
   
   
   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Thêm giỏ hàng thành công",
       "data": {
                 "product_name": "Thịt ba chỉ bò Úc Pacow khay",
                 "thumbnail_link": "product1.png"  
       }
   }

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
    <ul>
        <li><code>code:</code> 400</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
   @apiError (Error 4xx) 412-PreconditionFailed Lỗi kiểm tra điều kiện
    <ul>
        <li><code>code:</code> 412</li>
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
    @apiErrorExample {JSON} Error 412:
    {
        "code": 412,
        "message": "Hàng đang tạm hết!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Thêm sản phẩm vào giỏ hàng thất bại!"
    }
"""
"""
   @api {post} /cart/actions/add-item Thêm sản phẩm
   @apiName Thêm_sản_phẩm
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng thêm sản phẩm vào giỏ hàng

   @apiHeader {String} Content-Type <mark>application/json</mark>

   @apiParam  {Number} cart_id id giỏ hàng
   @apiParam  {Number} product_id id Sản phẩm
   @apiParam  {Number} quantity số lượng mua
   
   @apiParamExample  {JSON} Body request:
   {
       "cart_id": 1,
       "product_id": 2,
       "quantity": 1
   }

   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object[]} Object.data Đối tượng trả về
   @apiSuccess {Object} Object.data.product Đối tượng sản phẩm
   @apiSuccess {String} Object.data.product.product_name tên sản phẩm
   @apiSuccess {String} Object.data.product.thumbnail_link ảnh thumbnail sản phẩm

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Thêm sản phẩm vào giỏ hàng thành công",
       "data": {
           "product": [
              {
                 "product_name": "Thịt ba chỉ bò Úc Pacow khay",
                 "thumbnail_link": "product1.png"
              },
              {
                 "product_name": "Hộp phô mai que 300g",
                 "thumbnail_link": "product2.png"
              }
           ]      
       }
   }
   
   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
    <ul>
        <li><code>code:</code> 400</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
   @apiError (Error 4xx) 412-PreconditionFailed Lỗi kiểm tra điều kiện
    <ul>
        <li><code>code:</code> 412</li>
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
    @apiErrorExample {JSON} Error 412:
    {
        "code": 412,
        "message": "Hàng đang tạm hết!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Thêm sản phẩm vào giỏ hàng thất bại!"
    }
"""

"""
  @api {delete} /cart/<cartproduct_id> xóa sản phẩm
   @apiName Xóa_sản_phẩm
   @apiGroup Giỏ_hàng
   @apiVersion 1.0.0
   @apiDescription Khách hàng xóa sản phẩm khỏi giỏ hàng
   
   @apiParamExample  {JSON} Cách gọi URL:
   {host}/api/v1.0/cart/1
   
   @apiSuccess {String} code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
   @apiSuccess {String} message Thông báo kết quả

   @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Xóa sản phẩm thành công!",
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
        "message": "Xóa sản phẩm thất bại!"
    }
"""

"""
   @api {patch} /cart/<cart_id> Cập nhật số lượng của một sản phẩm
   @apiName Cập_nhật_số_lượng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng thay đổi số lượng một sản phẩm
   
   @apiHeader {String} Content-Type <mark>application/json</mark>

   @apiParam  {Number} product_id id sản phẩm
   @apiParam  {Number} quantity số lượng mua
   
   @apiParamExample  {JSON} Cách gọi URL:
   {host}/api/v1.0/cart/1
   @apiParamExample  {JSON} Body Request:
   { 
       "product_id": 1,
       "quantity": 2
   }
   
   @apiSuccess {String} code Mã trạng thái HTTP
   @apiSuccess {String} message Thông báo kết quả
   
   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Cập nhật số lượng thành công!" 
   }    
   
   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
    <ul>
        <li><code>code:</code> 400</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
   @apiError (Error 4xx) 412-PreconditionFailed Lỗi kiểm tra điều kiện
    <ul>
        <li><code>code:</code> 412</li>
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
    @apiErrorExample {JSON} Error 412:
    {
        "code": 412,
        "message": "Sản phẩm không còn đủ số lượng!"
    }
    @apiErrorExample {JSON} Error 412:
    {
        "code": 412,
        "message": "Vượt quá số lượng được cho phép mua!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi cập nhật số lượng!"
    }
"""
"""
   @api {delete} /cart/<cart_id> Xóa giỏ hàng
   @apiName Xóa_giỏ_hàng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng xóa giỏ hàng
   
   @apiParamExample  {JSON} Cách gọi URL:
   {host}/api/v1.0/cart/1
   
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   
   @apiSuccessExample {JSON} Success 200:
   {
      "code": 200,
      "message": "Xóa giỏ hàng thành công!"
   }
   
   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
    <ul>
        <li><code>code:</code> 400</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>   
   @apiError (Error 4xx) 404-NotFound Lỗi không tìm thấy dữ liệu
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
        "message": "Yêu cầu không hợp lệ!"
    }
    @apiErrorExample {JSON} Error 404:
    {
        "code": 404,
        "message": "Giỏ hàng không tồn tại!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Xóa giỏ hàng thất bại!"
    }
"""
