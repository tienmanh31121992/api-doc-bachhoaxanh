"""
   @api {post} /san-pham/them-gio-hang/id Thêm bớt sản phẩm
   @apiName thêm_bớt_sản_phẩm
   @apiGroup Giỏ_hàng
   @apiVersion  1.0.0
   @apiDescription Khách hàng thêm bớt sản phẩm trong giỏ hàng

   
   @apiParam  {Number} san_pham_id Sản phẩm id Giỏ hàng

    @apiParamExample {JSON} Dữ liệu mẫu:
   {
       "san_pham_id": "1"
   }

   
   @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
   @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
   @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả
   @apiSuccess (Thành công 200) {Object} Object.data Đối tượng trả về
   @apiSuccess (Thành công 200) {Number} Object.data.so_luong_sp số lượng sản phẩm trong giỏ hàng
   @apiSuccess (Thành công 200) {Object} Object.data.san_pham Đối tượng sản phẩm
   @apiSuccess (Thành công 200) {String} Object.data.san_pham.id id sản phẩm
   @apiSuccess (Thành công 200) {String} Object.data.san_pham.link_thumbnail ảnh thumbnail sản phẩm
   @apiSuccess (Thành công 200) {Number} Object.data.san_pham.so_luong số lượng mua của 1 sản phẩm



   @apiSuccessExample {JSON} Thêm giỏ hàng thành công:
   {
       "code" : 200,
       "message" : "Thêm sản phẩm vào giỏ hàng thành công",
       "data" : {
           "san_pham": {
              "id": 1,
              "link_thumbnail": "image.png",
              "so_luong" : 8;
           }

           "so_luong_sp" : 1
       }
   }
   

   @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
   @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
   @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

   @apiErrorExample {JSON} Thêm giỏ hàng thất bại:
   {
       "code" : 400,
       "message" : "Vượt quá số lượng cho phép mua! | Sản phẩm đang hết hàng!"
   }

   @apiErrorExample {JSON} Lỗi hệ thống:
   {
       "code" : 500,
       "message" : "Thêm sản phẩm không thành công!"
   }
"""
