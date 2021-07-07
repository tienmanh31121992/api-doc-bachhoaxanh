"""
   @api {post} /bill/actions/add-bill Xác nhận đơn hàng (Thêm đơn hàng)
   @apiName Tạo_đơn_hàng
   @apiGroup Đơn_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng ấn xác nhận đơn hàng, đơn hàng được thêm vào database

   @apiHeader {String} Content-Type <mark>application/json</mark>
   @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

   @apiHeaderExample  {JSON} Header mẫu:
   {
       "Content-Type": "application/json",
       "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
   }

   @apiParam (Body) {Number} customer.id id khách hàng
   @apiParam (Body) {String} receiver_name tên người nhận
   @apiParam (Body) {String} receiver_phone số điện thoại người nhận
   @apiParam (Body) {String} receiver_address địa chỉ nhận
   @apiParam (Body) {Number} province_id id tỉnh, thành phố
   @apiParam (Body) {Number} district_id id quận, huyện
   @apiParam (Body) {Number} block_id id xã, phường
   @apiParam (Body) {String} appointment_date ngày hẹn giao hàng
   @apiParam (Body) {String} delivery_note ghi chú vận chuyển
   @apiParam (Body) {String} bill_note ghi chú đơn hàng
   @apiParam (Body) {Number} ship_fee phí ship
   @apiParam (Body) {Number} delivery_fee phí ship
   @apiParam (Body) {Number} total_price tổng tiền đơn hàng
   @apiParam (Body) {Number} status Trạng thái đơn hàng
    <ul>
        <li><code>0:</code> đã hủy</li>
        <li><code>1:</code> chờ xác nhận</li>
        <li><code>2:</code> đang xuất hàng</li>
        <li><code>3:</code> đang giao hàng</li>
        <li><code>4:</code> đã nhận hàng</li>
    </ul>
   @apiParam (Body) {Number} voucher_id id phiếu mua hàng
   @apiParam (Body) {String} product.id id sản phẩm
   @apiParam (Body) {Number} product.quantity số lượng mua
   @apiParam (Body) {Number} product.price giá sản phẩm

   @apiParamExample {JSON} JSON - Body request:
    {
        "customer": {
            "id": 1
        },
        "bill": {
           "receiver_name": "Phạm Tiến Mạnh",
           "receiver_phone": "0973456233",
           "receiver_address": "Số 8, ngách 141",
           "province_id": 1,
           "district_id": 8,
           "block_id": 6,
           "appointment_date": "2/7/2021",
           "delivery_note": "mang lên lầu, gọi trước khi giao",
           "bill_note": "tôi muốn lưu số người giao hàng",
           "ship_fee": 19000,
           "delivery_fee": 1000,
           "total_price": 257000,
           "status": 1,
           "voucher_id": 1,
           "product": [
              {
                  "id": 1,
                  "quantity": 3,
                  "price": 32000
              },
              {
                  "id": 2,
                  "quantity": 4,
                  "price": 40000
              }
           ]
        }
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
   @api {delete} /bill/actions/cancel-bill Hủy đơn hàng
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

   @apiParam {Number} bill.id id đơn hàng
   
   @apiParamExample  {JSON} Cách truyền parameter:
   {host}/api/v1.0/bill/cancel-bill?id=1

    @apiSuccess {String} Object.code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    @apiSuccess {String} Object.message Thông báo kết quả
    @apiSuccess {Object} Object.data Đối tượng trả về
    @apiSuccess {Object} Object.data.bill Đối tượng đơn hàng
    @apiSuccess {Number} Object.data.bill.status Trạng thái đơn hàng
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
        "data": {
           "bill": { "status": 0 }      
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
   @api {get} /bill/actions/get-bills Lịch sử mua hàng
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
   
   
   @apiParam {Number} customer.id id khách hàng
   
   @apiParamExample  {JSON} Body request:
   {host}/api/v.1.0/bill/actions/get-bills?id=1

    @apiSuccess {String} Object.code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    @apiSuccess {String} Object.message Thông báo kết quả
    @apiSuccess {Object[]} Object.list_bill Đối tượng danh sách đơn hàng
    @apiSuccess {String} Object.list_bill.receiver_name người nhận hàng
    @apiSuccess {String} Object.list_bill.receiver_phone số điện thoại người nhận
    @apiSuccess {Number} Object.list_bill.province_id mã tỉnh, thành phố
    @apiSuccess {Number} Object.list_bill.district_id mã quận, huyện
    @apiSuccess {Number} Object.list_bill.block_id mã phường, xã
    @apiSuccess {String} Object.list_bill.appointment_date ngày hẹn giao hàng
    @apiSuccess {String} Object.list_bill.finished_at ngày hoàn thành đơn hàng
    @apiSuccess {String} Object.list_bill.delivery_note chú thích về giao hàng
    @apiSuccess {String} Object.list_bill.bill_note chú thích riêng của khách hàng
    @apiSuccess {Number} Object.list_bill.delivery_fee phí giao hàng thực tế
    @apiSuccess {Number} Object.list_bill.total_price tổng tiền của đơn hàng
    @apiSuccess {Number} Object.list_bill.status Trạng thái đơn hàng
    <ul>
        <li><code>0:</code> đã hủy</li>
        <li><code>1:</code> chờ xác nhận</li>
        <li><code>2:</code> đang xuất hàng</li>
        <li><code>3:</code> đang giao hàng</li>
        <li><code>4:</code> đã nhận hàng</li>
    </ul>
    @apiSuccess {Object[]} Object.list_bill.product Đối tượng sản phẩm
    @apiSuccess {Object} Object.list_bill.product.product_name tên sản phẩm
    @apiSuccess {Object} Object.list_bill.product.quantity mua với số lượng
    @apiSuccess {Object} Object.list_bill.product.expired_at ngày hết hạn
    @apiSuccess {Object} Object.list_bill.product.price giá sản phẩm    
    
    @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Lấy danh sách đơn hàng thành công!",
        "data": {
            "customer_name": "Nguyễn Hoàng Sơn",
            "list_bill": [
                  { 
                      "receiver_name": "Đinh Văn Hiệp",
                      "receiver_phone": "0368498298",
                      "receiver_address": "Số 9, ngách 112",
                      "province_id": 2,
                      "district_id": 10,
                      "block_id": 9,
                      "appointment_date": "1/7/2021",
                      "finished_at": "1/7/2021",
                      "delivery_note": "mang lên lầu",
                      "bill_note": "tôi muốn lấy hóa đơn",
                      "delivery_fee": 0,
                      "total_price": 202000,
                      "status": 0,
                      "product": [
                               {
                                   "product_name": "Phô mai que hương sữa Tân Việt Sin gói 400g",
                                   "quantity": 2,
                                   "expired_at": "30/10/2021",
                                   "price": 101000
                               }
                      ]
                  },
                  { 
                      "receiver_name": "Phạm Tiến Mạnh",
                      "receiver_phone": "0973456233",
                      "receiver_address": "Số 8, ngách 141",
                      "province_id": 1,
                      "district_id": 8,
                      "block_id": 6,
                      "appointment_date": "2/7/2021",
                      "finished_at": "",
                      "delivery_note": "mang lên lầu, gọi trước khi giao",
                      "bill_note": null,
                      "delivery_fee": 19000,
                      "total_price": 307000,
                      "status": 1,
                      "product": [
                               {
                                   "product_name": "snack Dorito bịch 64g",
                                   "quantity": 3,
                                   "expired_at": "30/10/2021",
                                   "price": 32000
                               },
                               {
                                   "product_name": "Hải sản ngũ sắc SG Food gói 300g",
                                   "quantity": 4,
                                   "expired_at": "30/4/2021",
                                   "price": 48000
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