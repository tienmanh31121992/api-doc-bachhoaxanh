"""
    @api {post} /customers/register Đăng ký
    @apiName Đăng_ký
    @apiGroup Khách_hàng
    @apiVersion 1.0.0
    @apiDescription Khách hàng đăng ký tài khoản


    @apiHeader {String} Content-Type <mark>application/json</mark>


    @apiParam (Body) {String} Object.data.ten_khach_hang Tên khách hàng
    @apiParam (Body) {Number} Object.data.gioi_tinh Giới tính khách hàng
    @apiParam (Body) {String} Object.data.so_dien_thoai Số điện thoại
    @apiParam (Body) {String} Object.data.mat_khau Mật khẩu
    @apiParam (Body) {String} Object.data.dia_chi Địa chỉ khách hàng
    @apiParam (Body) {Date}   Object.data.ngay_sinh Ngày sinh
    @apiParam (Body) {String} Object.data.email Địa chỉ thư điện tử
    @apiParam (Body) {String} Object.data.ten_nguoi_giam_ho Tên người giám hộ
    @apiParam (Body) {String} Object.data.so_cmnd Số chứng minh thư, căn cước, hộ chiếu
    @apiParam (Body) {Date}   Object.data.ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
    @apiParam (Body) {String} Object.data.noi_cap_cmnd Nơi cấp CMT, CCCD, HC
    @apiParam (Body) {Number} Object.data.tinh_tp_id ID tỉnh/thành phố
    @apiParam (Body) {Number} Object.data.quan_huyen_id ID quận/huyện
    @apiParam (Body) {Number} Object.data.xa_phuong_id ID xã/phường

    @apiParamExample {JSON} JSON - Body request:
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


    @apiSuccess {String} code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    @apiSuccess {String} message Thông báo kết quả

    @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Đăng ký tài khoản thành công!"
    }


    @apiError 412-PreconditionFailed Lỗi kiểm tra điều kiện
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
        "message": "Thông báo lỗi cụ thể"
    }
"""

"""
    @api {get} /customers/login Đăng nhập
    @apiName Đăng_nhập
    @apiGroup Khách_hàng
    @apiVersion  1.0.0
    @apiDescription Khách hàng đăng nhập vào hệ thống


    @apiHeader {String} Content-Type <mark>application/json</mark>


    @apiParam (Body) {String} so_dien_thoai Số điện thoại khách hàng
    @apiParam (Body) {String} mat_khau Mật khẩu đăng nhập

    @apiParamExample {JSON} JSON - Body request:
    {
        "so_dien_thoai": "0123456789",
        "mat_khau": "a1b2c3A@"
    }

    
    @apiSuccess {Object} data Thông tin của khách hàng
    @apiSuccess {Number} data.id ID khách hàng
    @apiSuccess {String} data.ma_khach_hang Mã khách hàng
    @apiSuccess {String} data.ten_khach_hang Tên khách hàng
    @apiSuccess {String} data.so_dien_thoai Số điện thoại
    @apiSuccess {String} data.dia_chi Địa chỉ khách hàng
    @apiSuccess {Date}   data.ngay_sinh Ngày sinh
    @apiSuccess {String} data.link_anh_dai_dien Đường dẫn lưu ảnh đại diện
    @apiSuccess {String} data.email Địa chỉ thư điện tử
    @apiSuccess {Number} data.gioi_tinh Giới tính khách hàng
    @apiSuccess {String} data.ten_nguoi_giam_ho Tên người giám hộ
    @apiSuccess {String} data.so_cmnd Số chứng minh thư, căn cước, hộ chiếu
    @apiSuccess {Date}   data.ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
    @apiSuccess {String} data.noi_cap_cmnd Nơi cấp CMT, CCCD, HC
    @apiSuccess {Number} data.tinh_tp_id ID tỉnh/thành phố
    @apiSuccess {Number} data.quan_huyen_id ID quận/huyện
    @apiSuccess {Number} data.xa_phuong_id ID xã/phường
    @apiSuccess {String} mesage Thông báo kết quả
    @apiSuccess {String} token Chuỗi Token
    @apiSuccess {String} code Mã trạng thái HTTP
    <br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark><br>
    
    @apiSuccessExample {JSON} Success 200:
    {
        "code": 200,
        "message": "Đăng nhập thành công!",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
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

   
    @apiError (Error 4xx) 403-Forbidden Truy cập dữ liệu bị từ chối
    <ul>
        <li><code>code:</code> 403</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
    @apiError (Error 4xx) 404-NotFound Lỗi truy cập dữ liệu không tồn tại
    <ul>
        <li><code>code:</code> 404</li>
        <li><code>message:</code> Thông báo lỗi</li>
    </ul>
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

    @apiErrorExample {JSON} Error 403:
    {
        "code": 403,
        "message": "Tài khoản đang bị khóa!"
    }
    @apiErrorExample {JSON} Error 404:
    {
        "code": 404,
        "message": "Tài khoản không tồn tại!"
    }
    @apiErrorExample {JSON} Error 412:
    {
        "code": 412,
        "message": "Mật khẩu không đúng!"
    }
    @apiErrorExample {JSON} Lỗi hệ thống:
    {
        "code": 500,
        "message": "Xảy ra lỗi khi đăng nhập!"
    }
"""

"""
    @api {put} /customers/update-info Cập nhật thông tin
    @apiName Cập_nhật_thông_tin
    @apiGroup Khách_hàng
    @apiVersion 1.0.0
    @apiDescription Khách hàng cập nhật thông tin tài khoản

    
    @apiHeader {String} Content-Type <mark>application/json</mark>
    @apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>


    @apiParam (Body) {Number} id ID khách hàng
    @apiParam (Body) {String} ten_khach_hang Tên khách hàng
    @apiParam (Body) {String} so_dien_thoai Số điện thoại
    @apiParam (Body) {String} dia_chi Địa chỉ khách hàng
    @apiParam (Body) {Date}   ngay_sinh Ngày sinh
    @apiParam (Body) {String} link_anh_dai_dien Đường dẫn lưu ảnh đại diện
    @apiParam (Body) {String} email Địa chỉ thư điện tử
    @apiParam (Body) {Number} gioi_tinh Giới tính khách hàng
    @apiParam (Body) {String} ten_nguoi_giam_ho Tên người giám hộ
    @apiParam (Body) {String} so_cmnd Số chứng minh thư, căn cước, hộ chiếu
    @apiParam (Body) {Date}   ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
    @apiParam (Body) {String} noi_cap_cmnd Nơi cấp CMT, CCCD, HC
    @apiParam (Body) {Number} tinh_tp_id ID tỉnh/thành phố
    @apiParam (Body) {Number} quan_huyen_id ID quận/huyện
    @apiParam (Body) {Number} xa_phuong_id ID xã/phường

    @apiParamExample {JSON} JSON - Body request:
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


    @apiSuccess {Object} Object Kết quả trả về 
    @apiSuccess {String} Object.code Mã trạng thái HTTP
    @apiSuccess {String} Object.message Thông báo kết quả
    @apiSuccess {Object} Object.data Đối tượng khách hàng
    @apiSuccess {Number} Object.data.id ID khách hàng
    @apiSuccess {String} Object.data.ma_khach_hang Mã khách hàng
    @apiSuccess {String} Object.data.ten_khach_hang Tên khách hàng
    @apiSuccess {String} Object.data.so_dien_thoai Số điện thoại
    @apiSuccess {String} Object.data.dia_chi Địa chỉ khách hàng
    @apiSuccess {Date}   Object.data.ngay_sinh Ngày sinh
    @apiSuccess {String} Object.data.link_anh_dai_dien Đường dẫn lưu ảnh đại diện
    @apiSuccess {String} Object.data.email Địa chỉ thư điện tử
    @apiSuccess {Number} Object.data.gioi_tinh Giới tính khách hàng
    @apiSuccess {String} Object.data.ten_nguoi_giam_ho Tên người giám hộ
    @apiSuccess {String} Object.data.so_cmnd Số chứng minh thư, căn cước, hộ chiếu
    @apiSuccess {Date}   Object.data.ngay_cap_cmnd Ngày cấp CMT, CCCD, HC
    @apiSuccess {String} Object.data.noi_cap_cmnd Nơi cấp CMT, CCCD, HC
    @apiSuccess {Number} Object.data.tinh_tp_id ID tỉnh/thành phố
    @apiSuccess {Number} Object.data.quan_huyen_id ID quận/huyện
    @apiSuccess {Number} Object.data.xa_phuong_id ID xã/phường

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
    @apiGroup Khách_hàng
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


    @apiSuccess {Object} Object Kết quả trả về 
    @apiSuccess {String} Object.code Mã trạng thái HTTP
    @apiSuccess {String} Object.message Thông báo kết quả

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