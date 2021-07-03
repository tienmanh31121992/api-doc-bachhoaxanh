"""
   @api {get} /cart Xem giỏ hàng
   @apiName Xem_giỏ_hàng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng vào xem giỏ hàng

   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object[]} Object.data Đối tượng trả về
   @apiSuccess {Number} Object.data.cart_items_count đếm số sản phẩm trong giỏ hàng
   @apiSuccess {Number} Object.data.cart_total_price tổng tiền trong giỏ hàng
   @apiSuccess {Number} Object.data.ship_fee phí giao hàng dự kiến
   @apiSuccess {Number} Object.data.voucher_count đếm số lượng voucher
   @apiSuccess {Object} Object.data.product Đối tượng sản phẩm
   @apiSuccess {Number} Object.data.product.product_id Sản phẩm id
   @apiSuccess {String} Object.data.product.product_code mã sản phẩm
   @apiSuccess {String} Object.data.product.product_name tên sản phẩm
   @apiSuccess {String} Object.data.product.quantity mua với số lượng
   @apiSuccess {Number} Object.data.product.price giá
   @apiSuccess {Number} Object.data.product.cart_product_total_price tổng tiền sản phẩm trong giỏ hàng
   @apiSuccess {Object} Object.data.product.promotion Đối tượng khuyến mãi
   @apiSuccess {Number} Object.data.product.promotion.promotion_id id khuyến mãi
   @apiSuccess {Number} Object.data.product.promotion.promotion_name tên khuyến mãi
   @apiSuccess {Number} Object.data.product.promotion.content nội dung khuyến mãi
   @apiSuccess {Object} Object.data.customer_voucher Đối tượng voucher của khách hàng
   @apiSuccess {Number} Object.data.customer_voucher.id id đếm số lượng
   @apiSuccess {Number} Object.data.customer_voucher.voucher_id id voucher


   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Giỏ hàng load thành công!",
       "data": {
          "cart_items_count": 2,
          "cart_total_price": 640000,
          "ship_fee": 5000,
          "voucher_count": 5,
          "product": [
            {
              "product_id": 1,
              "product_code": "SP001",
              "product_name": "Thùng 20 lon bia",
              "thumbnail_link": "product1.png",
              "quantity": 1,
              "price": 280000,
              "cart_product_total_price": 280000,
              "promotion": null
            },
            {
              "product_id": 2,
              "product_code": "SP002",
              "product_name": "Thùng 12 gói mì tôm",
              "thumbnail_link": "product2.png",
              "quantity": 2,
              "price": 180000,
              "cart_product_total_price": 360000,
              "promotion": {
                    "promotion_id": 1,
                    "promotion_name": "Mua 2 tặng 1",
                    "content": "Mua 2 thùng 12 gói mì tôm được tặng thêm 1 thùng mì tôm"
              }
            }
          ],
            "customer_voucher": [
              {
                  "id": 1,
                  "voucher_id": 1
              },
              {
                  "id": 2,
                  "voucher_id": 1
              },
              {
                  "id": 3,
                  "voucher_id": 1
              },
              {
                  "id": 4,
                  "voucher_id": 1
              },
              {
                  "id": 5,
                  "voucher_id": 1
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
   @api {post} /cart/add-item Thêm sản phẩm
   @apiName Thêm_sản_phẩm
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng thêm sản phẩm vào giỏ hàng

   @apiParam  {Number} cart_id id giỏ hàng
   @apiParam  {Number} product_id id Sản phẩm

   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/cart/add-item?cart_id=1&product_id=1

   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object[]} Object.data Đối tượng trả về
   @apiSuccess {Number} Object.data.cart_items_count Đếm số sản phẩm trong giỏ hàng
   @apiSuccess {Number} Object.data.cart_total_price tổng tiền giỏ hàng
   @apiSuccess {Object} Object.data.product Đối tượng sản phẩm
   @apiSuccess {String} Object.data.product.product_name tên sản phẩm
   @apiSuccess {String} Object.data.product.thumbnail_link ảnh thumbnail sản phẩm
   @apiSuccess {Number} Object.data.product.cart_product_total_price tổng tiền sản phẩm

   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Thêm sản phẩm vào giỏ hàng thành công",
       "data": {
           "cart_items_count": 1,
           "cart_total_price": 196000,
           "product": [
              {
                 "product_name": "Thịt ba chỉ bò Úc Pacow khay",
                 "thumbnail_link": "product1.png",
                 "cart_product_total_price": 196000
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
  @api {delete} /cart/delete-item xóa sản phẩm
   @apiName Xóa_sản_phẩm
   @apiGroup Giỏ_hàng
   @apiVersion 1.0.0
   @apiDescription Khách hàng xóa sản phẩm khỏi giỏ hàng
   
   @apiParam  {Number} cartproduct_id id của row table nối giữa giỏ hàng và sản phẩm
   
   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/cart/delete-item?cartproduct_id=1
   
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
   @api {put} /cart/update-item-quantity Cập nhật số lượng của một sản phẩm
   @apiName Cập_nhật_số_lượng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng tăng hoặc giảm bớt số lượng một sản phẩm

   @apiParam  {Number} cartproduct_id id của row table nối giữa giỏ hàng và sản phẩm
   @apiParam  {Number} quantity số lượng sản phẩm

   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/cart/update-item-quantity?cartproduct_id=1&quantity=5
   
   @apiSuccess {Object} Object Kết quả trả về
   @apiSuccess {String} Object.code Mã trạng thái HTTP
   @apiSuccess {String} Object.message Thông báo kết quả
   @apiSuccess {Object} Object.data Đối tượng trả về
   @apiSuccess {Number} Object.data.quantity mua với số lượng
   
   
   @apiSuccessExample {JSON} Success 200:
   {
       "code": 200,
       "message": "Cập nhật số lượng thành công!",
       "data": {
            "quantity": 5
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
   @api {delete} /cart/delete-cart Xóa giỏ hàng
   @apiName Xóa_giỏ_hàng
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng xóa giỏ hàng


   @apiParam {Number} cart_id Giỏ hàng id 

   @apiParamExample {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/cart/delete-cart?cart_id=1
   
   @apiSuccess {Object} Object Kết quả trả về 
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
