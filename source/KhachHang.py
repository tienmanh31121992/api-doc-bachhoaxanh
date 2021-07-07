"""
@api {post} /customers/actions/register Đăng ký
@apiName Đăng_ký
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng đăng ký tài khoản


@apiHeader {String} Content-Type <mark>application/json</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json"
}


@apiParam (Body) {String} customer_name Tên khách hàng
@apiParam (Body) {Number=0,1} gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiParam (Body) {String} phone Số điện thoại
@apiParam (Body) {String} password Mật khẩu
@apiParam (Body) {String} address Địa chỉ khách hàng
@apiParam (Body) {Date}   [date_of_birth] Ngày sinh
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
    "avatar_link": "avatar1.jpg",
    "guardian_name": null,
    "indentity_id": "HC000001VN",
    "certify_date": "12/12/2009",
    "certify_place": "Hải Dương",
    "province_id": 1,
    "district_id": 2,
    "block_id": 3
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

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
@api {post} /customers/actions/login Đăng nhập
@apiName Đăng_nhập
@apiGroup Khách_hàng
@apiVersion  1.0.0
@apiDescription Khách hàng đăng nhập vào hệ thống


@apiHeader {String} Content-Type <mark>application/json</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json"
}


@apiParam (Body) {String} phone Số điện thoại khách hàng
@apiParam (Body) {String} password Mật khẩu đăng nhập

@apiParamExample {JSON} Body request:
{
    "phone": "0123456789",
    "password": "a1b2c3A@"
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.mesage Thông báo kết quả
@apiSuccess {String} O.token Chuỗi Token
@apiSuccess {Object} O.data Thông tin của khách hàng
@apiSuccess {Number} O.data.id ID khách hàng
@apiSuccess {String} O.data.customer_code Mã khách hàng
@apiSuccess {String} O.data.customer_name Tên khách hàng
@apiSuccess {Number} O.data.gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiSuccess {String} O.data.customer_phone Số điện thoại
@apiSuccess {String} O.data.customer_address Địa chỉ khách hàng
@apiSuccess {Date}   O.data.date_birth Ngày sinh
@apiSuccess {String} O.data.avatar_link Đường dẫn lưu ảnh đại diện
@apiSuccess {String} O.data.email Địa chỉ thư điện tử
@apiSuccess {String} O.data.guardian_name Tên người giám hộ
@apiSuccess {String} O.data.indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiSuccess {Date}   O.data.certify_date Ngày cấp CMT, CCCD, HC
@apiSuccess {String} O.data.certify_place Nơi cấp CMT, CCCD, HC
@apiSuccess {Number} O.data.province_id ID tỉnh/thành phố
@apiSuccess {Number} O.data.district_id ID quận/huyện
@apiSuccess {Number} O.data.block_id ID xã/phường


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
        "avatar_link": "avatar1.jpg",
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
@api {patch} /customers/actions/updateinfo Cập nhật thông tin
@apiName Cập_nhật_thông_tin
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng cập nhật thông tin tài khoản


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Body) {Number} id ID khách hàng
@apiParam (Body) {String} customer_code Mã khách hàng
@apiParam (Body) {String} customer_name Tên khách hàng
@apiParam (Body) {String} customer_phone Số điện thoại
@apiParam (Body) {String} customer_address Địa chỉ khách hàng
@apiParam (Body) {Date}   date_birth Ngày sinh
@apiParam (Body) {String} avatar_link Đường dẫn lưu ảnh đại diện
@apiParam (Body) {String} email Địa chỉ thư điện tử
@apiParam (Body) {Number=0,1} gender Giới tính khách hàng
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
    "avatar_link": "avatar1.jpg",
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


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả
@apiSuccess {Object} O.data Thông tin khách hàng
@apiSuccess {Number} O.data.id ID khách hàng
@apiSuccess {String} O.data.customer_code Mã khách hàng
@apiSuccess {String} O.data.customer_name Tên khách hàng
@apiSuccess {String} O.data.customer_phone Số điện thoại
@apiSuccess {String} O.data.customer_address Địa chỉ khách hàng
@apiSuccess {Date}   O.data.date_birth Ngày sinh
@apiSuccess {String} O.data.avatar_link Đường dẫn lưu ảnh đại diện
@apiSuccess {String} O.data.email Địa chỉ thư điện tử
@apiSuccess {Number} O.data.gender Giới tính khách hàng
<ul>
    <li><code>0:</code> Nữ</li>
    <li><code>1:</code> Nam</li>
</ul>
@apiSuccess {String} O.data.guardian_name Tên người giám hộ
@apiSuccess {String} O.data.indentity_id Số chứng minh thư, căn cước, hộ chiếu
@apiSuccess {Date}   O.data.certify_date Ngày cấp CMT, CCCD, HC
@apiSuccess {String} O.data.certify_place Nơi cấp CMT, CCCD, HC
@apiSuccess {Number} O.data.province_id ID tỉnh/thành phố
@apiSuccess {Number} O.data.district_id ID quận/huyện
@apiSuccess {Number} O.data.block_id ID xã/phường

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
        "avatar_link": "avatar2.jpg",
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
@api {patch} /customers/actions/changepassword Đổi mật khẩu
@apiName Đổi_mật_khẩu
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng thay đổi mật khẩu


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Body) {Number} id ID khách hàng
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


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

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
@api {post} /customers/actions/buyvoucher Đặt mua phiếu mua hàng điện tử
@apiName Mua_phiếu_mua_hàng
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Khách hàng đặt mua phiếu mua hàng điện tử


@apiHeader {String} Content-Type <mark>application/json</mark>
@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam (Body) {Number} customer_id ID khách hàng
@apiParam (Body) {Number} voucher_id ID voucher
@apiParam (Body) {Number} quantity Số lượng

@apiParamExample  {JSON} Body request:
{
    "customer_id": 10,
    "voucher_id": 1,
    "quantity": 2
}


@apiSuccess {Number} O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String} O.message Thông báo kết quả

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Đặt mua phiếu mua hàng điện tử thành công!"
}


@apiError 400-BadRequest Không thể xử lý yêu cầu.
<ul>
    <li><code>code:</code> 400</li>
    <li><code>message:</code> Thông báo lỗi</li>
</ul>
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

@apiErrorExample {JSON} Error 400:
{
    "code": 400,
    "message": "Sai định dạng URL!"
}
@apiErrorExample {JSON} Error 401:
{
    "code": 401,
    "message": "Token hết hạn hoặc không hợp lệ. Vui lòng đăng nhập lại!"
}
@apiErrorExample {JSON} Error 500:
{
    "code": 500,
    "message": "Xảy ra lỗi khi đặt mua phiếu mua hàng: Mô tả lỗi."
}
"""


"""
@api {get} /customers/actions/viewvoucher Xem phiếu mua hàng đang sở hữu
@apiName Xem_phiếu_mua_hàng
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách phiếu mua hàng khách hàng đang sở hữu


@apiHeader {String} Authorization <code>Bearer</code> <mark>Chuỗi Token</mark>

@apiHeaderExample {JSON} Header request:
{
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"
}


@apiParam {Number} customer_id <mark>ID khách hàng</mark>
@apiParam {String=end_time} sort=end_time:asc <mark>Sắp xếp dữ liệu theo cú pháp sau
<br><code>Trường dữ liệu:Kiểu sắp xếp</code></mark>

@apiParamExample URL request:
{host}/api/v1.0/customers/actions/viewvoucher?customer_id=10&sort=end_time:asc


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin voucher
@apiSuccess {Number}    O.data.id ID voucher <code>(Thuộc bảng CustomerVoucher)</code>
@apiSuccess {String}    O.data.voucher_code Mã voucher
@apiSuccess {String}    O.data.voucher_name Tên voucher
@apiSuccess {String}    O.data.content Nội dung
@apiSuccess {Date}      O.data.end_time Thời hạn voucher <code>(Thuộc bảng CustomerVoucher)</code>

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin phiếu mua hàng thành công!",
    "data": [
        {
            "id": 1,
            "voucher_code": "PHM1000K",
            "voucher_name": "Phiếu mua hàng 1 triệu",
            "content": "Phiếu mua hàng trị  giá 1.000.000đ",
            "end_time": "31/12/2022"
        },
        {
            "id": 2,
            "voucher_code": "PHM2000K",
            "voucher_name": "Phiếu mua hàng 2 triệu",
            "content": "Phiếu mua hàng trị  giá 2.000.000đ"
            "end_time": "31/12/2022"
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
@api {get} /customers/actions/historysearch Lịch sử tìm kiếm sản phẩm
@apiName Lịch_sử_tìm_kiếm
@apiGroup Khách_hàng
@apiVersion 1.0.0
@apiDescription Lấy danh sách từ khóa khách hàng đã tìm kiếm


@apiParam {Number} customer_id <mark>ID khách hàng</mark>
@apiParam {String=search_string,search_number,searched_at} sort=searched_at:desc <mark>Sắp xếp dữ liệu theo cú pháp sau
<br><code>Trường dữ liệu:Kiểu sắp xếp</code></mark>
@apiParam {Number=≥1} top <mark>Giới hạn số lượng bản ghi

@apiParamExample URL request:
{host}/api/v1.0/customer/actions/historysearch?customer_id=10&sort=searched_at:desc&top=4


@apiSuccess {Number}    O.code Mã trạng thái HTTP
<br><mark><code>200:</code> Yêu cầu được tiếp nhận và xử lý thành công</mark>
@apiSuccess {String}    O.message Thông báo kết quả
@apiSuccess {Object[]}  O.data Danh sách thông tin chuỗi tìm kiếm
@apiSuccess {Number}    O.data.id ID chuỗi tìm kiếm
@apiSuccess {String}    O.data.search_string Chuỗi tìm kiếm
@apiSuccess {String}    O.data.search_number Số lần tìm kiếm
@apiSuccess {Date}      O.data.searched_at Thời điểm tìm kiếm gần nhất

@apiSuccessExample {JSON} Success 200:
{
    "code": 200,
    "message": "Lấy thông tin lịch sử tìm kiếm sản phẩm thành công!",
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