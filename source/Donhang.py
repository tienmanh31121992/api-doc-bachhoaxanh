"""
   @api {post} /bill/post-bill Xác nhận đơn hàng
   @apiName Tạo_đơn_hàng
   @apiGroup Đơn_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng ấn xác nhận đơn hàng, đơn hàng được tạo trong database

   @apiHeader {String} Content-Type <mark>application/json</mark>
   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

   @apiHeaderExample  {JSON} Header mẫu:
   {
       "Content-Type": "application/json",
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }

   @apiParam (Body) {String} Object.data.customer_name tên khách hàng
   @apiParam (Body) {String} Object.data.customer_phone số điện thoại khách hàng
   @apiParam (Body) {String} Object.data.receiver_address địa chỉ nhận
   @apiParam (Body) {String} Object.data.receiver_phone số điện thoại người nhận
   @apiParam (Body) {String} Object.data.province_id id tỉnh, thành phố
   @apiParam (Body) {String} Object.data.district_id id quận, huyện
   @apiParam (Body) {String} Object.data.block_id id xã, phường
   @apiParam (Body) {String} Object.data.appointment_date ngày hẹn giao hàng
   @apiParam (Body) {String} Object.data.delivery_note ghi chú vận chuyển
   @apiParam (Body) {String} Object.data.bill_note ghi chú đơn hàng
   @apiParam (Body) {String} Object.data.ship_fee phí ship
   @apiParam (Body) {String} Object.data.total_price tổng tiền đơn hàng
   @apiParam (Body) {Number} Object.data.status Trạng thái đơn hàng
    <ul>
        <li><code>0:</code> đã hủy</li>
        <li><code>1:</code> chờ xác nhận</li>
        <li><code>2:</code> đang xuất hàng</li>
        <li><code>3:</code> đang giao hàng</li>
        <li><code>4:</code> đã nhận hàng</li>
    </ul>
   @apiParam (Body) {Object} Object.data.product Đối tượng sản phẩm trong đơn hàng
   @apiParam (Body) {String} Object.data.product.product_name tên sản phẩm
   @apiParam (Body) {String} Object.data.product.quantity mua với số lượng
   @apiParam (Body) {String} Object.data.product.expired_at ngày hết hạn
   @apiParam (Body) {String} Object.data.product.price giá sản phẩm
   @apiParam (Body) {String} Object.data.product.total_price tổng tiền sản phẩm

   @apiParamExample {JSON} JSON - Body request:
    {
        "customer_name": "Nguyễn Hoàng Sơn",
        "customer_phone": "0353395973",
        "receiver_name": "Phạm Tiến Mạnh",
        "receiver_phone": "0973456233",
        "province_id": 1,
        "district_id": 8,
        "block_id": 6,
        "appointment_date": "2/7/2021",
        "delivery_note": "mang lên lầu, gọi trước khi giao",
        "bill_note": "tôi muốn lưu số người giao hàng",
        "ship_fee": 19000,
        "total_price": 288000,
        "status": 1,
        "product": [
              {
                  "product_name": "snack Dorito bịch 64g",
                  "quantity": 3,
                  "expired_at": "30/10/2021",
                  "price": 32000,
                  "total_price": 96000
              },
              {
                  "product_name": "Hải sản ngũ sắc SG Food gói 300g",
                  "quantity": 4,
                  "expired_at": "30/4/2021",
                  "price": 48000,
                  "total_price": 192000
              }
        ]
    }


    @apiSuccess {String} code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    @apiSuccess {String} message Thông báo kết quả

    @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Đơn hàng tiếp nhận thành công!"
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
        "message": "Tiếp nhận đơn hàng không thành công!"
    }
"""
"""
   @api {delete} /bill/cancel-bill Hủy đơn hàng
   @apiName Hủy_đơn_hàng
   @apiGroup Đơn_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng hủy đơn hàng

   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>
   @apiHeaderExample  {JSON} Header mẫu:
   {   
       "Content-Type": "application/json",
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }

   @apiParam {Number} bill_id id đơn hàng
   
   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/bill/cancel-bill?bill_id=1

    @apiSuccess {Object} Object Kết quả trả về
    @apiSuccess {String} Object.code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    @apiSuccess {String} Object.message Thông báo kết quả
    @apiSuccess {Object} Object.data Đối tượng trả về
    @apiSuccess {Number} Object.data.status Trạng thái đơn hàng
    <ul>
        <li><code>0:</code> đã hủy</li>
        <li><code>1:</code> chờ xác nhận</li>
        <li><code>2:</code> đang xuất hàng</li>
        <li><code>3:</code> đang giao hàng</li>
        <li><code>4:</code> đã nhận hàng</li>
    </ul>

    @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Hủy đơn hàng thành công!"
        "data" {
            "status": 0
        }
    }

   @apiError (Error 4xx) 400-BadRequest Lỗi Request từ phía Client
    <ul>
        <li><code>code:</code> 400</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
   @apiError (Error 4xx) 404-NotFound Lỗi Không tìm thấy dữ liệu
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
        "code": 400,
        "message": "Không tìm thấy đơn hàng!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Hủy đơn hàng không thành công!"
    }
"""
"""
   @api {get} /bill/get-customer-bills Lịch sử mua hàng
   @apiName lịch_sử_mua_hàng
   @apiGroup Đơn_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng xem lịch sử mua hàng

   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>
   @apiHeaderExample  {JSON} Header mẫu:
   {   
       "Content-Type": "application/json",
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }
   
   @apiParam {Number} customer_id id khách hàng
   
   @apiParamExample  {JSON} Cách truyền parameter:
   https://www.bachhoaxanh.com/api/v1/bill/get-customer-bills?customer_id=1
   

    @apiSuccess {Object} Object Kết quả trả về
    @apiSuccess {String} Object.code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    @apiSuccess {String} Object.message Thông báo kết quả
    @apiSuccess {Object[]} Object.data Đối tượng trả về
    @apiSuccess {Object} Object.data.list_bill Đối tượng danh sách đơn hàng
    @apiSuccess {String} Object.data.list_bill.receiver_name người nhận hàng
    @apiSuccess {String} Object.data.list_bill.receiver_phone số điện thoại người nhận
    @apiSuccess {Number} Object.data.list_bill.province_id mã tỉnh, thành phố
    @apiSuccess {Number} Object.data.list_bill.district_id mã quận, huyện
    @apiSuccess {Number} Object.data.list_bill.block_id mã phường, xã
    @apiSuccess {String} Object.data.list_bill.appointment_date ngày hẹn giao hàng
    @apiSuccess {String} Object.data.list_bill.finished_at ngày hoàn thành đơn hàng
    @apiSuccess {String} Object.data.list_bill.delivery_note chú thích về giao hàng
    @apiSuccess {String} Object.data.list_bill.bill_note chú thích riêng của khách hàng
    @apiSuccess {Number} Object.data.list_bill.ship_fee phí giao hàng
    @apiSuccess {Number} Object.data.list_bill.total_price tổng tiền của đơn hàng
    @apiSuccess {Number} Object.data.list_bill.status Trạng thái đơn hàng
    <ul>
        <li><code>0:</code> đã hủy</li>
        <li><code>1:</code> chờ xác nhận</li>
        <li><code>2:</code> đang xuất hàng</li>
        <li><code>3:</code> đang giao hàng</li>
        <li><code>4:</code> đã nhận hàng</li>
    </ul>
    @apiSuccess {Object} Object.data.list_bill.product Đối tượng sản phẩm
    @apiSuccess {Object} Object.data.list_bill.product.product_name tên sản phẩm
    @apiSuccess {Object} Object.data.list_bill.product.quantity mua với số lượng
    @apiSuccess {Object} Object.data.list_bill.product.expired_at ngày hết hạn
    @apiSuccess {Object} Object.data.list_bill.product.price giá sản phẩm
    @apiSuccess {Object} Object.data.list_bill.product.total_price tổng tiền sản phẩm      
    
    
    @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Lấy danh sách đơn hàng thành công!",
        "data": {
            "list_bill": [
                  { 
                      "receiver_name": "Đinh Văn Hiệp",
                      "receiver_phone": "0368498298",
                      "province_id": 2,
                      "district_id": 10,
                      "block_id": 9,
                      "appointment_date": "1/7/2021",
                      "finished_at": "1/7/2021",
                      "delivery_note": "mang lên lầu",
                      "bill_note": "tôi muốn lấy hóa đơn",
                      "ship_fee": 17000,
                      "total_price": 202000,
                      "status": 0,
                      "product": [
                               {
                                   "product_name": "Phô mai que hương sữa Tân Việt Sin gói 400g",
                                   "quantity": 2,
                                   "expired_at": "30/10/2021",
                                   "price": 101000,
                                   "total_price": 202000
                               }
                      ]
                  },
                  { 
                      "receiver_name": "Phạm Tiến Mạnh",
                      "receiver_phone": "0973456233",
                      "province_id": 1,
                      "district_id": 8,
                      "block_id": 6,
                      "appointment_date": "2/7/2021",
                      "finished_at": "",
                      "delivery_note": "mang lên lầu, gọi trước khi giao",
                      "bill_note": "tôi muốn lưu số người giao hàng",
                      "ship_fee": 19000,
                      "total_price": 288000,
                      "status": 1,
                      "product": [
                               {
                                   "product_name": "snack Dorito bịch 64g",
                                   "quantity": 3,
                                   "expired_at": "30/10/2021",
                                   "price": 32000,
                                   "total_price": 96000
                               },
                               {
                                   "product_name": "Hải sản ngũ sắc SG Food gói 300g",
                                   "quantity": 4,
                                   "expired_at": "30/4/2021",
                                   "price": 48000,
                                   "total_price": 192000
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
   @apiError (Error 4xx) 404-NotFound Lỗi Không tìm thấy dữ liệu
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
        "message": "Không tìm thấy danh sách đơn hàng!"
    }
    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Lấy danh sách đơn hàng không thành công!"
    }
"""