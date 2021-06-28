"""
   @api {post} /khach_hang/dang_nhap Khách hàng đăng nhập
   @apiName Khách hàng đăng nhập
   @apiGroup Khách hàng
   @apiVersion  1.0.0
   
   @apiExample Ví dụ cách sử dụng:
   http://bachhoaxanh.com/khach_hang/dang_nhap
   
   @apiParam  {String} so_dien_thoai Số điện thoại khách hàng
   @apiParam  {String} mat_khau Mật khẩu đăng nhập

    @apiParamExample {JSON} Ví dụ gửi yêu cầu:
   {
       "so_dien_thoai" : "0123456789",
       "mat_khau" : "a1b2c3A@"
   }
   
   @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
   @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
   @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả
   @apiSuccess (Thành công 200) {Object} Object.data Đối tượng khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.ma_khach_hang Mã khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.ten_khach_hang Tên khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.so_dien_thoai Số điện thoại
   @apiSuccess (Thành công 200) {String} Object.data.mat_khau Mật khẩu
   @apiSuccess (Thành công 200) {Date}   Object.data.ngay_sinh Ngày sinh

   
   
   @apiSuccessExample {JSON} Đăng nhập thành công:
   {
       "code" : 200,
       "message" : "Đăng nhập thành công",
       "data" : {
           "ma_khach_hang" : "KH00001",
           "ten_khach_hang" : "Tiến Mạnh"
       }
   }

   @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
   @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
   @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

   @apiErrorExample {JSON} Đăng nhập thất bại:
   {
       "code" : 400,
       "message" : "Mật khẩu không đúng (không tồn tại khách hàng)",
   }

   @apiErrorExample {JSON} Lỗi hệ thống:
   {
       "code" : 500,
       "message" : "Xảy ra lỗi khi đăng nhập",
   }

"""
