"""
@api {post} /customer-register Đăng ký
@apiName Đăng_ký
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng đăng ký tài khoản


@apiHeader {String} Content-Type <mark>application/json</mark>


@apiParam (Body) {String} customer_name Tên khách hàng
@apiParam (Body) {Number} gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiParam (Body) {String} phone Số điện thoại
@apiParam (Body) {String} password Mật khẩu
@apiParam (Body) {String} address Địa chỉ khách hàng
@apiParam (Body) {Date}   [date_birth] Ngày sinh
@apiParam (Body) {String} [email] Địa chỉ thư điện tử
@apiParam (Body) {String} [avatar_link] Đường dẫn lưu ảnh đại diện
@apiParam (Body) {String} [guardian_name] Tên người giám hộ
@apiParam (Body) {String} [indentity_id] Số chứng minh thư, căn cước, hộ chiếu
@apiParam (Body) {Date}   [certify_date] Ngày cấp CMT, CCCD, HC
@apiParam (Body) {String} [certify_place] Nơi cấp CMT, CCCD, HC
@apiParam (Body) {Number} province_id ID tỉnh/thành phố
@apiParam (Body) {Number} district_id ID quận/huyện
@apiParam (Body) {Number} block_id ID xã/phường

@apiParamExample {JSON} Body request:
{
    "customer_name": "Tiến Mạnh",
    "gender": 1,
    "phone": "0123456789",
    "password": "a1b2c3A@",
    "address": "Số 9, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
    "date_birth": "31/12/1992",
    "email": "asdasdasf@gmail.com",
    "avatar_link": "avatar.jpg",
    "guardian_name": null,
    "indentity_id": "HC000001VN",
    "certify_date": "12/12/2009",
    "certify_place": "Hải Dương",
    "province_id": 1,
    "district_id": 2,
    "block_id": 3
}


@apiSuccess {String} code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
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
    "message": "Xảy ra lỗi khi đăng ký: Mô tả lỗi."
}
"""

"""
@api {post} /customer-login Đăng nhập
@apiName Đăng_nhập
@apiGroup Khách_hàng
@apiVersion  1.0.0
@apiDescription Khách hàng đăng nhập vào hệ thống


@apiHeader {String} Content-Type <mark>application/json</mark>


@apiParam (Body) {String} phone Số điện thoại khách hàng
@apiParam (Body) {String} password Mật khẩu đăng nhập

@apiParamExample {JSON} Body request:
{
    "phone": "0123456789",
    "password": "a1b2c3A@"
}


@apiSuccess {Object} data Thông tin của khách hàng
@apiSuccess {Number} data.id ID khách hàng
@apiSuccess {String} data.customer_code Mã khách hàng
@apiSuccess {String} data.customer_name Tên khách hàng
@apiSuccess {Number} data.gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiSuccess {String} data.customer_phone Số điện thoại
@apiSuccess {String} data.customer_address Địa chỉ khách hàng
@apiSuccess {Date}   data.date_birth Ngày sinh
@apiSuccess {String} data.avatar_link Đường dẫn lưu ảnh đại diện
@apiSuccess {String} data.email Địa chỉ thư điện tử
@apiSuccess {String} data.guardian_name Tên người giám hộ
@apiSuccess {String} data.indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiSuccess {Date}   data.certify_date Ngày cấp CMT, CCCD, HC
@apiSuccess {String} data.certify_place Nơi cấp CMT, CCCD, HC
@apiSuccess {Number} data.province_id ID tỉnh/thành phố
@apiSuccess {Number} data.district_id ID quận/huyện
@apiSuccess {Number} data.block_id ID xã/phường
@apiSuccess {String} mesage Thông báo kết quả
@apiSuccess {String} token Chuỗi Token
@apiSuccess {String} code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đăng nhập thành công!",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
    "data": {
        "id": 1,
        "customer_code": "A0000001",
        "customer_name": "Tiến Mạnh",
        "gender": 1,
        "customer_phone": "0123456789",
        "customer_address": "Số 9, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
        "date_birth": "31/12/1992",
        "email": "asdasdasf@gmail.com",
        "avatar_link": "avatar.jpg",
        "guardian_name": null,
        "indentity_id": "HC000001VN",
        "certify_date": "12/12/2009",
        "certify_place": "Hải Dương",
        "province_id": 1,
        "district_id": 2,
        "block_id": 3
    }
}


@apiError 403-Forbidden Truy cập dữ liệu bị từ chối
<ul>
    <li><code>code:</code> 403</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Lỗi truy cập dữ liệu không tồn tại
<ul>
    <li><code>code:</code> 404</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 412-PreconditionFailed Lỗi khi kiểm tra dữ liệu
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
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đăng nhập: Mô tả lỗi."
}
"""

"""
@api {put} /customer-update-info Cập nhật thông tin
@apiName Cập_nhật_thông_tin
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng cập nhật thông tin tài khoản


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>


@apiParam (Body) {Number} id ID khách hàng
@apiParam (Body) {String} customer_code Mã khách hàng
@apiParam (Body) {String} customer_name Tên khách hàng
@apiParam (Body) {String} customer_phone Số điện thoại
@apiParam (Body) {String} customer_address Địa chỉ khách hàng
@apiParam (Body) {Date}   date_birth Ngày sinh
@apiParam (Body) {String} avatar_link Đường dẫn lưu ảnh đại diện
@apiParam (Body) {String} email Địa chỉ thư điện tử
@apiParam (Body) {Number} gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiParam (Body) {String} guardian_name Tên người giám hộ
@apiParam (Body) {String} indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiParam (Body) {Date}   certify_date Ngày cấp CMT, CCCD, HC
@apiParam (Body) {String} certify_place Nơi cấp CMT, CCCD, HC
@apiParam (Body) {Number} province_id ID tỉnh/thành phố
@apiParam (Body) {Number} district_id ID quận/huyện
@apiParam (Body) {Number} block_id ID xã/phường

@apiParamExample {JSON} Body request:
{
    "id": 1,
    "customer_code": "A0000001",
    "customer_name": "Phạm Tiến Mạnh",
    "customer_phone": "0123456789",
    "customer_address": "Số 11, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
    "date_birth": "31/12/1992",
    "avatar_link": "avatar.jpg",
    "email": "asdasdasf@gmail.com",
    "gender": 1,
    "guardian_name": null,
    "indentity_id": "HC000001VN",
    "certify_date": "10/10/2010",
    "certify_place": "Hải Dương",
    "province_id": 4,
    "district_id": 5,
    "block_id": 6
}


@apiSuccess {Object} data Thông tin khách hàng
@apiSuccess {Number} data.id ID khách hàng
@apiSuccess {String} data.customer_code Mã khách hàng
@apiSuccess {String} data.customer_name Tên khách hàng
@apiSuccess {String} data.customer_phone Số điện thoại
@apiSuccess {String} data.customer_address Địa chỉ khách hàng
@apiSuccess {Date}   data.date_birth Ngày sinh
@apiSuccess {String} data.avatar_link Đường dẫn lưu ảnh đại diện
@apiSuccess {String} data.email Địa chỉ thư điện tử
@apiSuccess {Number} data.gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiSuccess {String} data.guardian_name Tên người giám hộ
@apiSuccess {String} data.indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiSuccess {Date}   data.certify_date Ngày cấp CMT, CCCD, HC
@apiSuccess {String} data.certify_place Nơi cấp CMT, CCCD, HC
@apiSuccess {Number} data.province_id ID tỉnh/thành phố
@apiSuccess {Number} data.district_id ID quận/huyện
@apiSuccess {Number} data.block_id ID xã/phường
@apiSuccess {String} message Thông báo kết quả
@apiSuccess {String} code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Cập nhật thông tin thành công!",
    "data": {
        "id": 1,
        "customer_code": "A0000001",
        "customer_name": "Phạm Tiến Mạnh",
        "customer_phone": "0123456789",
        "customer_address": "Số 11, ngõ 11 đường Cầu Diễn, Phường Minh Khai, Quận Bắc Từ Liêm, Hà Nội",
        "date_birth": "31/12/1992",
        "avatar_link": "avatar.jpg",
        "email": "asdasdasf@gmail.com",
        "gender": 1,
        "guardian_name": null,
        "indentity_id": "HC000001VN",
        "certify_date": "10/10/2010",
        "certify_place": "Hải Dương",
        "province_id": 4,
        "district_id": 5,
        "block_id": 6
    }
}


@apiError 401-Unauthorized Token hết hạn hoặc không hợp lệ.
<ul>
    <li><code>code:</code> 401</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError (Error 5xx) 500-InternalServerError Lỗi Server
<ul>
    <li><code>code:</code> 500</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>

@apiErrorExample {JSON} Error 401:
{
    "code": 401,
    "message": "Token hết hạn hoặc không hợp lệ. Vui lòng đăng nhập lại!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi cập nhật thông tin: Mô tả lỗi."
}
"""

"""
@api {put} /customer-change-password Đổi mật khẩu
@apiName Đổi_mật_khẩu
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng thay đổi mật khẩu


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>


@apiParam (Body) {String} id ID khách hàng
@apiParam (Body) {String} customer_code Mã khách hàng
@apiParam (Body) {String} customer_phone Số điện thoại
@apiParam (Body) {String} password Mật khẩu hiện tại
@apiParam (Body) {String} new_password Mật khẩu mới

@apiParamExample  {JSON} Body request:
{
    "id": 1,
    "customer_code": "A0000001",
    "customer_phone": "0123456789",
    "password": "a1b2c3A@",
    "new_password": "9m8n7b#"
}


@apiSuccess {String} code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đổi mật khẩu thành công. Vui lòng đăng nhập lại!"
}

@apiError 401-Unauthorized Token hết hạn hoặc không hợp lệ.
<ul>
    <li><code>code:</code> 401</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
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

@apiErrorExample {JSON} Error 401:
{
    "code": 401,
    "message": "Token hết hạn hoặc không hợp lệ. Vui lòng đăng nhập lại!"
}
@apiErrorExample {JSON} Error 412:
{
    "code": 412,
    "message": "Mật khẩu hiện tại không đúng!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đổi mật khẩu: Mô tả lỗi."
}
"""

"""
@api {get} /customer/<id>/history-search Lịch sử tìm kiếm
@apiName Lịch_sử_tìm_kiếm
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách từ khóa khách hàng đã tìm kiếm


@apiParam (Path) {Number} id <mark>ID khách hàng</mark>
@apiParam {String} sort_by <mark>Sắp xếp theo: Mặc định là id</mark>
@apiParam {String} sort_order <mark>Kiểu sắp xếp: Mặc định asc</mark>
@apiParam {Number} [limit] <mark>Giới hạn số lượng bản ghi</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/customer/<id>/history-search?sort_by=id&sort_order=asc&limit=4


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin chuỗi tìm kiếm
@apiSuccess {Number}    data.id ID chuỗi tìm kiếm
@apiSuccess {String}    data.search_string Chuỗi tìm kiếm
@apiSuccess {String}    data.search_number Số lần tìm kiếm
@apiSuccess {Date}      data.searched_at Thời điểm tìm kiếm gần nhất

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin sản phẩm thành công!",
    "data": [
        {
            "id": 1,
            "search_string": "thit ga",
            "search_number": 10,
            "searched_at": "01/06/2021"
        },
        {
            "id": 2,
            "search_string": "trung",
            "search_number": 30,
            "searched_at": "01/06/2021"
        },
        {
            "id": 3,
            "search_string": "pepsi",
            "search_number": 15,
            "searched_at": "01/06/2021"
        },
        {
            "id": 1,
            "search_string": "banh keo",
            "search_number": 10,
            "searched_at": "01/06/2021"
        }
    ]
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
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
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""

"""
@api {get} /customer/<id>/voucher Phiếu mua hàng
@apiName Phiếu_mua_hàng
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách phiếu mua hàng khách hàng đang sở hữu


@apiParam (Path) {Number} id <mark>ID khách hàng</mark>
@apiParam {String} sort_by=id <mark>Sắp xếp theo cột</mark>
@apiParam {String} sort_order=asc <mark>Kiểu sắp xếp</mark>

@apiParamExample URL request:
https://www.bachhoaxanh.com/api/v1/customer/<id>/voucher?sort_by=id&sort_order=asc


@apiSuccess {String}    code Mã trạng thái HTTP
<br><mark>200-OK: Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    message Thông báo kết quả
@apiSuccess {Object[]}  data Danh sách thông tin voucher
@apiSuccess {Number}    data.id ID voucher
@apiSuccess {String}    data.voucher_code Mã voucher
@apiSuccess {String}    data.voucher_name Tên voucher
@apiSuccess {String}    data.content Nội dung

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin phiếu mua hàng thành công!",
    "data": [
        {
            "id": 1,
            "voucher_code": "PHM1000K",
            "voucher_name": Phiếu mua hàng 1 triệu,
            "content": "Phiếu mua hàng trị  giá 1.000.000đ"
        },
        {
            "id": 2,
            "voucher_code": "PHM2000K",
            "voucher_name": Phiếu mua hàng 2 triệu,
            "content": "Phiếu mua hàng trị  giá 2.000.000đ"
        }
    ]
}

@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
@apiError 404-NotFound Không tìm thấy dữ liệu.
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
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 404:
{
    "code": 404,
    "message": "Không tìm thấy dữ liệu!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi lấy lịch sử tìm kiếm: Mô tả lỗi."
}
"""