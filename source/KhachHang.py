"""
    @api {post} /customers/register Đăng ký
    @apiName Đăng_ký
    @apiGroup Tài_khoản
    @apiVersion 1.0.0
    @apiDescription Khách hàng đăng ký tài khoản


    @apiHeader {String} Content-Type application/json


    @apiParam (Body) {String} Object.data.ten_khach_hang Tên khách hàng
    @apiParam (Body) {Number} Object.data.gioi_tinh Giới tính khách hàng
    @apiParam (Body) {String} Object.data.so_dien_thoai Số điện thoại
    @apiParam (Body) {String} Object.data.mat_khau Mật khẩu
    @apiParam (Body) {String} Object.data.dia_chi Địa chỉ khách hàng
    @apiParam (Body) {Date}   [Object.data.ngay_sinh] Ngày sinh
    @apiParam (Body) {String} [Object.data.email] Địa chỉ thư điện tử
    @apiParam (Body) {String} [Object.data.ten_nguoi_giam_ho] Tên người giám hộ
    @apiParam (Body) {String} [Object.data.so_cmnd] Số chứng minh thư, căn cước, hộ chiếu
    @apiParam (Body) {Date}   [Object.data.ngay_cap_cmnd] Ngày cấp CMT, CCCD, HC
    @apiParam (Body) {String} [Object.data.noi_cap_cmnd] Nơi cấp CMT, CCCD, HC
    @apiParam (Body) {Number} Object.data.tinh_tp_id ID tỉnh/thành phố
    @apiParam (Body) {Number} Object.data.quan_huyen_id ID quận/huyện
    @apiParam (Body) {Number} Object.data.xa_phuong_id ID xã/phường

    @apiParamExample  {JSON} JSON - Body request:
    {
        "ten_khach_hang": "Tiến Mạnh",
        "so_dien_thoai": "0123456789",
        "mat_khau": "a1b2c3A@",
        "dia_chi": "Số 9, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
        "ngay_sinh": "31/12/1992",
        "email": "asdasdasf@gmail.com",
        "gioi_tinh": 1,
        "ten_nguoi_giam_ho": null,
        "so_cmnd": "HC000001VN",
        "ngay_cap_cmnd": "12/12/2009",
        "noi_cap_cmnd": "Hải Dương",
        "tinh_tp_id": 1,
        "quan_huyen_id": 2,
        "xa_phuong_id": 3
    }


    @apiSuccess (Success 2xx) 200-OK Yêu cầu được tiếp nhận và xử lý thành công
    <ul>
        <li><code>code:</code> 200</li>
        <li><code>message:</code> Thông báo kết quả</li>
    </ul>

    @apiSuccessExample {JSON} 200 OK:
    {
        "code": 200,
        "message": "Đăng ký tài khoản thành công!"
    }


    @apiError (Error 4xx) 412-PreconditionFailed Lỗi khi kiểm tra dữ liệu
    <ul>
        <li><code>code:</code> 412</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
    @apiError (Error 5xx) 500-InternalServerError Lỗi Server
    <ul>
        <li><code>code:</code> 500</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>

    @apiErrorExample {JSON} Error 412:
    {
        "code": 412,
        "message": "Tài khoản đã tồn tại!"
    }

    @apiErrorExample {JSON} Error 500:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi đăng ký tài khoản!"
    }
"""

"""
   @api {post} /customers/login Đăng nhập
   @apiName Đăng_nhập
   @apiGroup Tài_khoản
   @apiVersion  1.0.0
   @apiDescription Khách hàng đăng nhập vào hệ thống


   @apiHeader {String} Content-Type application/json

   
   @apiParam (Body) {String} so_dien_thoai Số điện thoại khách hàng
   @apiParam (Body) {String} mat_khau Mật khẩu đăng nhập

    @apiParamExample {JSON} JSON - Body request:
    {
       "so_dien_thoai": "0123456789",
       "mat_khau": "a1b2c3A@"
    }

   
   @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
   @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
   @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả
   @apiSuccess (Thành công 200) {Object} Object.data Đối tượng khách hàng
   @apiSuccess (Thành công 200) {Number} Object.data.id ID khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.ma_khach_hang Mã khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.ten_khach_hang Tên khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.so_dien_thoai Số điện thoại
   @apiSuccess (Thành công 200) {String} Object.data.dia_chi Địa chỉ khách hàng
   @apiSuccess (Thành công 200) {Date}   Object.data.ngay_sinh Ngày sinh
   @apiSuccess (Thành công 200) {String} Object.data.link_anh_dai_dien Đường dẫn lưu ảnh đại diện
   @apiSuccess (Thành công 200) {String} Object.data.email Địa chỉ thư điện tử
   @apiSuccess (Thành công 200) {Number} Object.data.gioi_tinh Giới tính khách hàng
   @apiSuccess (Thành công 200) {String} Object.data.ten_nguoi_giam_ho Tên người giám hộ
   @apiSuccess (Thành công 200) {String} Object.data.so_cmnd Số chứng minh thư, căn cước, hộ chiếu
   @apiSuccess (Thành công 200) {Date}   Object.data.ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
   @apiSuccess (Thành công 200) {String} Object.data.noi_cap_cmnd Nơi cấp CMT, CCCD, HC
   @apiSuccess (Thành công 200) {Number} Object.data.tinh_tp_id ID tỉnh/thành phố
   @apiSuccess (Thành công 200) {Number} Object.data.quan_huyen_id ID quận/huyện
   @apiSuccess (Thành công 200) {Number} Object.data.xa_phuong_id ID xã/phường

   @apiSuccessExample {JSON} Đăng nhập thành công:
    {
        "code": 200,
        "message": "Đăng nhập thành công!",
        "data": {
            "id": 1,
            "ma_khach_hang": "A0000001",
            "ten_khach_hang": "Tiến Mạnh",
            "so_dien_thoai": "0123456789",
            "dia_chi": "Số 9, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
            "ngay_sinh": "31/12/1992",
            "link_anh_dai_dien": "avatar.jpg",
            "email": "asdasdasf@gmail.com",
            "gioi_tinh": 1,
            "ten_nguoi_giam_ho": null,
            "so_cmnd": "HC000001VN",
            "ngay_cap_cmnd": "12/12/2009",
            "noi_cap_cmnd": "Hải Dương",
            "tinh_tp_id": 1,
            "quan_huyen_id": 2,
            "xa_phuong_id": 3
        }
    }
   

   @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
   @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
   @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

   @apiErrorExample {JSON} Đăng nhập thất bại:
   {
       "code": 400,
       "message": "Mật khẩu không đúng! | Tài khoản không tồn tại! | Tài khoản đã bị khóa!"
   }

   @apiErrorExample {JSON} Lỗi hệ thống:
   {
       "code": 500,
       "message": "Xảy ra lỗi khi đăng nhập!"
   }
"""

"""
    @api {put} /khach-hang/cap-nhat-thong-tin Cập nhật thông tin
    @apiName Cập_nhật_thông_tin
    @apiGroup Tài_khoản
    @apiVersion 1.0.0
    @apiDescription Khách hàng cập nhật thông tin tài khoản

    @apiParam {Object} Object Đối tượng khách hàng
    @apiParam {String} Object.data.id ID khách hàng
    @apiParam {String} Object.data.ten_khach_hang Tên khách hàng
    @apiParam {String} Object.data.so_dien_thoai Số điện thoại
    @apiParam {String} Object.data.dia_chi Địa chỉ khách hàng
    @apiParam {Date}   Object.data.ngay_sinh Ngày sinh
    @apiParam {String} Object.data.link_anh_dai_dien Đường dẫn lưu ảnh đại diện
    @apiParam {String} Object.data.email Địa chỉ thư điện tử
    @apiParam {Number} Object.data.gioi_tinh Giới tính khách hàng
    @apiParam {String} Object.data.ten_nguoi_giam_ho Tên người giám hộ
    @apiParam {String} Object.data.so_cmnd Số chứng minh thư, căn cước, hộ chiếu
    @apiParam {Date}   Object.data.ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
    @apiParam {String} Object.data.noi_cap_cmnd Nơi cấp CMT, CCCD, HC
    @apiParam {Number} Object.data.tinh_tp_id ID tỉnh/thành phố
    @apiParam {Number} Object.data.quan_huyen_id ID quận/huyện
    @apiParam {Number} Object.data.xa_phuong_id ID xã/phường

    @apiParamExample  {JSON} Dữ liệu mẫu:
    {
        "id": 1,
        "ten_khach_hang": "Phạm Tiến Mạnh",
        "so_dien_thoai": "0123456789",
        "dia_chi": "Số 11, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
        "ngay_sinh": "31/12/1992",
        "link_anh_dai_dien": "avatar.jpg",
        "email": "asdasdasf@gmail.com",
        "gioi_tinh": 1,
        "ten_nguoi_giam_ho": null,
        "so_cmnd": "HC000001VN",
        "ngay_cap_cmnd": "10/10/2010",
        "noi_cap_cmnd": "Hải Dương",
        "tinh_tp_id": 4,
        "quan_huyen_id": 5,
        "xa_phuong_id": 6
    }


    @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
    @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
    @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả
    @apiSuccess (Thành công 200) {Object} Object.data Đối tượng khách hàng
    @apiSuccess (Thành công 200) {Number} Object.data.id ID khách hàng
    @apiSuccess (Thành công 200) {String} Object.data.ma_khach_hang Mã khách hàng
    @apiSuccess (Thành công 200) {String} Object.data.ten_khach_hang Tên khách hàng
    @apiSuccess (Thành công 200) {String} Object.data.so_dien_thoai Số điện thoại
    @apiSuccess (Thành công 200) {String} Object.data.dia_chi Địa chỉ khách hàng
    @apiSuccess (Thành công 200) {Date}   Object.data.ngay_sinh Ngày sinh
    @apiSuccess (Thành công 200) {String} Object.data.link_anh_dai_dien Đường dẫn lưu ảnh đại diện
    @apiSuccess (Thành công 200) {String} Object.data.email Địa chỉ thư điện tử
    @apiSuccess (Thành công 200) {Number} Object.data.gioi_tinh Giới tính khách hàng
    @apiSuccess (Thành công 200) {String} Object.data.ten_nguoi_giam_ho Tên người giám hộ
    @apiSuccess (Thành công 200) {String} Object.data.so_cmnd Số chứng minh thư, căn cước, hộ chiếu
    @apiSuccess (Thành công 200) {Date}   Object.data.ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
    @apiSuccess (Thành công 200) {String} Object.data.noi_cap_cmnd Nơi cấp CMT, CCCD, HC
    @apiSuccess (Thành công 200) {Number} Object.data.tinh_tp_id ID tỉnh/thành phố
    @apiSuccess (Thành công 200) {Number} Object.data.quan_huyen_id ID quận/huyện
    @apiSuccess (Thành công 200) {Number} Object.data.xa_phuong_id ID xã/phường

    @apiSuccessExample {JSON} Cập nhật thông tin thành công:
    {
        "code": 200,
        "message": "Cập nhật thông tin thành công!",
        "data": {
            "id": 1,
            "ma_khach_hang": "A0000001",
            "ten_khach_hang": "Phạm Tiến Mạnh",
            "so_dien_thoai": "0123456789",
            "dia_chi": "Số 11, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
            "ngay_sinh": "31/12/1992",
            "link_anh_dai_dien": "avatar.jpg",
            "email": "asdasdasf@gmail.com",
            "gioi_tinh": 1,
            "ten_nguoi_giam_ho": null,
            "so_cmnd": "HC000001VN",
            "ngay_cap_cmnd": "10/10/2010",
            "noi_cap_cmnd": "Hải Dương",
            "tinh_tp_id": 4,
            "quan_huyen_id": 5,
            "xa_phuong_id": 6
        }
    }


    @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
    @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
    @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

    @apiErrorExample {JSON} Cập nhật thông tin thất bại:
    {
        "code": 400,
        "message": "Cập nhật thông tin thất bại!"
    }

    @apiErrorExample {JSON} Lỗi hệ thống:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi cập nhật thông tin!"
    }
"""

"""
    @api {put} /khach-hang/doi-mat-khau Đổi mật khẩu
    @apiName Đổi_mật_khẩu
    @apiGroup Tài_khoản
    @apiVersion 1.0.0
    @apiDescription Khách hàng thay đổi mật khẩu

    @apiParam {Object} Object Đối tượng khách hàng
    @apiParam {String} Object.data.id ID khách hàng
    @apiParam {String} Object.data.so_dien_thoai Số điện thoại
    @apiParam {String} Object.data.mat_khau_cu Mật khẩu hiện tại
    @apiParam {String} Object.data.mat_khau_moi Mật khẩu mới

    @apiParamExample  {JSON} Dữ liệu mẫu:
    {
        "id": 1,
        "so_dien_thoai": "0123456789",
        "mat_khau_cu": "a1b2c3A@",
        "mat_khau_moi": "9m8n7b#"
    }


    @apiSuccess (Thành công 200) {Object} Object Kết quả trả về 
    @apiSuccess (Thành công 200) {String} Object.code Mã trạng thái HTTP
    @apiSuccess (Thành công 200) {String} Object.message Thông báo kết quả

    @apiSuccessExample {JSON} Đổi mật khẩu thành công:
    {
        "code": 200,
        "message": "Đổi mật khẩu thành công!"
    }


    @apiError (Thất bại 400/500) {Object} Object Kết quả trả về 
    @apiError (Thất bại 400/500) {String} Object.code Mã trạng thái HTTP
    @apiError (Thất bại 400/500) {String} Object.message Thông báo kết quả

    @apiErrorExample {JSON} Đổi mật khẩu thất bại:
    {
        "code": 400,
        "message": "Mật khẩu cũ không đúng!"
    }

    @apiErrorExample {JSON} Lỗi hệ thống:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi đổi mật khẩu!"
    }
"""